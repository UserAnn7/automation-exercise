import pytest
import os
import allure
from pytest_html import extras

# Create screenshots directory once per test session
@pytest.fixture(scope="session", autouse=True)
def create_screenshot_dir():
    os.makedirs("screenshots", exist_ok=True)
    os.makedirs("logs", exist_ok=True)

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)

    if rep.when == "call":
        page = item.funcargs.get("page", None)
        if page:
            screenshot_name = f"{item.name}_{rep.outcome.upper()}.png"
            screenshot_path = os.path.join("screenshots", screenshot_name)
            allure.attach(page.screenshot(path=screenshot_path), name=screenshot_name, attachment_type=allure.attachment_type.PNG)
            extra = extras.image(screenshot_path)
            add_extras(rep, extra)

        log_name = f"{item.name}_{rep.outcome.upper()}.log"
        log_path = os.path.join("logs", log_name)
        if os.path.exists(log_path):
            with open(log_path, "r") as f:
                log_content = f.read()
                allure.attach(log_content, name=log_name, attachment_type=allure.attachment_type.TEXT)
                extra = extras.html(f"<pre>{log_content}</pre>")
                add_extras(rep, extra)

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

    log_path =  f"logs/{test_name}_{result}.log"

    # Save URL log
    with open(log_path, "w") as f:
        f.write(f"Test: {test_name}\n")
        f.write(f"Outcome: {result}\n")
        f.write(f"URL: {page.url}\n")

def add_extras(rep, extra):
    """Add extra information to the test report."""
    if hasattr(rep, 'extras'):
        rep.extras.append(extra)
    else:
        rep.extras = [extra]