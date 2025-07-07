import pytest
import os
import allure
from pytest_html import extras
import base64
from datetime import datetime
import logging
from playwright.sync_api import sync_playwright

# Uncomment these fixtures for local browser testing
@pytest.fixture(scope="function")
def browser(request):
    if "ui" in request.keywords:
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=False,
                                        args=[
                                            "--window-position=0,0",
                                            "--window-size=1680,1050"
                                        ]
                                        )
            yield browser
            browser.close()
    else:
        # For not-ui tests — fixtures are not created
        yield None

@pytest.fixture(scope="function")
def page(browser, request):
    if "ui" in request.keywords and browser is not None:
        context = browser.new_context()
        page = context.new_page()
        page.set_viewport_size({"width": 1680, "height": 1050})
        yield page
        context.close()
    else:
        yield None

# Create screenshots directory once per test session
@pytest.fixture(scope="session", autouse=True)
def create_screenshot_dir():
    os.makedirs("screenshots", exist_ok=True)

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)

    if rep.when == "call":
        # Capture logs
        log_file = f"logs/{item.name}.log"
        os.makedirs(os.path.dirname(log_file), exist_ok=True)
        with open(log_file, "w") as f:
            for handler in logger.handlers:
                if isinstance(handler, logging.FileHandler):
                    handler.stream = f
                    break
            else:
                file_handler = logging.FileHandler(log_file)
                logger.addHandler(file_handler)
                file_handler.stream = f

        # Add logs to the report
        with open(log_file, "r") as f:
            log_content = f.read()
            # Add logs to HTML report
            extra = extras.html(f'<pre>{log_content}</pre>')
            if hasattr(rep, 'extras'):
                rep.extras.append(extra)
            else:
                rep.extras = [extra]

        page = item.funcargs.get("page", None)
        if page:
            # Add timestamp to screenshot name
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            screenshot_name = f"{item.name}_{rep.outcome.upper()}_{timestamp}.png"
            screenshot_path = os.path.join("screenshots", screenshot_name)
            allure.attach(page.screenshot(path=screenshot_path), name=screenshot_name, attachment_type=allure.attachment_type.PNG)
            # Embed the image directly in the report
            image_base64 = embed_image_base64(screenshot_path)
            extra = extras.html(f'<img src="data:image/png;base64,{image_base64}" alt="{screenshot_name}" height="250px"/>')
            if hasattr(rep, 'extras'):
                rep.extras.append(extra)
            else:
                rep.extras = [extra]

# Function to convert an image file to a base64-encoded string
def embed_image_base64(image_path):
    try:
        with open(image_path, "rb") as image_file:
            return base64.b64encode(image_file.read()).decode('utf-8')
    except FileNotFoundError:
        return ""  # Return an empty string if the file is not found
    except Exception as e:
        print(f"Error encoding image to base64: {e}")
        return ""