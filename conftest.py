# conftest.py
import pytest
import os
import allure

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)

    # Attach extra artifacts to the report
    if hasattr(item, "extra"):
        rep.extra = item.extra

@pytest.fixture(autouse=True)
def capture_artifacts(page, request):
    yield  # Let the test run first

    # Determine outcome
    test_name = request.node.name
    result = (
        "PASSED" if request.node.rep_call.passed
        else "FAILED" if request.node.rep_call.failed
        else "SKIPPED"
    )

    os.makedirs("screenshots", exist_ok=True)

    screenshot_path = f"screenshots/{test_name}_{result}.png"
    log_path =  f"screenshots/{test_name}_{result}.log"

    page.screenshot(path=screenshot_path)

    # Save URL log
    with open(log_path, "w") as f:
        f.write(f"Test: {test_name}\n")
        f.write(f"Outcome: {result}\n")
        f.write(f"URL: {page.url}\n")

    # Attach screenshot to Allure
    with open(screenshot_path, "rb") as image_file:
        allure.attach(image_file.read(), name=f"{test_name}_screenshot", attachment_type=allure.attachment_type.PNG)

    # Attach log to Allure
    with open(log_path, "r") as log_file:
        allure.attach(log_file.read(), name=f"{test_name}_log", attachment_type=allure.attachment_type.TEXT)

    if request.config.pluginmanager.hasplugin("html"):
        from pytest_html import extras
        extra = getattr(request.node, "extra", [])
        extra.append(extras.image(screenshot_path))
        extra.append(extras.url(log_path, name="Test Log"))
        request.node.extra = extra

def pytest_configure(config):
    if hasattr(config, "_metadata"):
        config._metadata['Project'] = 'automation-exercise'