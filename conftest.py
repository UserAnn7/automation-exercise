import pytest
import os
import allure
from pytest_html import extras
import base64

# Create screenshots directory once per test session
@pytest.fixture(scope="session", autouse=True)
def create_screenshot_dir():
    os.makedirs("screenshots", exist_ok=True)

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
            # Embed the image directly in the report
            image_base64 = embed_image_base64(screenshot_path)
            extra = extras.html(f'<img src="data:image/png;base64,{image_base64}" alt="{screenshot_name}"/>')
            if hasattr(rep, 'extras'):
                rep.extras.append(extra)
            else:
                rep.extras = [extra]

def embed_image_base64(image_path):
    """Convert an image file to a base64-encoded string."""
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')