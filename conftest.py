from pytest import fixture, hookimpl
import os
import allure
from allure_commons.types import AttachmentType
from pytest_html import extras
import base64
from datetime import datetime
import logging
from playwright.sync_api import sync_playwright
from helpers.data_loader import load_test_data

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


@fixture(scope="function")
def har_path_provider(request):
    if "ui" in request.keywords:
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True, args=[
                "--window-position=0,0",
                "--window-size=1680,1050"
            ])
            har_dir = "../har"
            os.makedirs(har_dir, exist_ok=True)
            har_path = os.path.join(har_dir, f"{request.node.name}.har")
            context = browser.new_context(record_har_path=har_path)
            request.node.stash["har_file_path"] = har_path
            yield context
            context.close()
            browser.close()
    else:
        yield None


@fixture(scope="function")
def page(har_path_provider, request):
    context = har_path_provider
    if "ui" in request.keywords and context is not None:
        playwright_page = context.new_page()
        playwright_page.set_viewport_size({"width": 1680, "height": 1050})
        yield playwright_page
        playwright_page.close()
    else:
        yield None

@hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, f"rep_{rep.when}", rep)

    # Скриншот — при падении на этапе выполнения теста
    if rep.when == "call" and rep.failed:
        page = item.funcargs.get("page")
        if page:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            screenshot_name = f"{item.name}_FAILED_{timestamp}.png"
            screenshot_dir = "screenshots_for_failed_cases"
            os.makedirs(screenshot_dir, exist_ok=True)
            screenshot_path = os.path.join(screenshot_dir, screenshot_name)

            try:
                page.screenshot(path=screenshot_path)
                # Прикрепляем к Allure
                allure.attach.file(screenshot_path, name=screenshot_name, attachment_type=AttachmentType.PNG)
                # Прикрепляем к html-отчету (pytest-html)
                img_base64 = embed_image_base64(screenshot_path)
                html = f'<img src="data:image/png;base64,{img_base64}" alt="{screenshot_name}" height="250px"/>'
                extra = extras.html(html)
                if hasattr(rep, "extras"):
                    rep.extras.append(extra)
                else:
                    rep.extras = [extra]
                logger.info(f"Attached screenshot for failed test {item.name}")
            except Exception as e:
                logger.error(f"Error attaching screenshot for {item.name}: {e}")

    # HAR файл — прикрепляем в teardown, когда файл гарантированно записан
    if rep.when == "teardown":
        har_path = item.stash.get("har_file_path", None)
        if har_path:
            if os.path.exists(har_path):
                size = os.path.getsize(har_path)
                if size > 50:
                    try:
                        allure.attach.file(
                            har_path,
                            name=f"{item.name}_network_log.txt",
                            attachment_type=AttachmentType.TEXT
                        )
                        logger.info(f"Attached HAR log for {item.name}")
                    except Exception as e:
                        logger.error(f"Failed to attach HAR log for {item.name}: {e}")
                else:
                    logger.warning(f"HAR file {har_path} too small ({size} bytes) for {item.name}, skipping attach.")
            else:
                logger.warning(f"HAR file {har_path} not found for {item.name}.")
        else:
            logger.debug(f"No HAR path in stash for {item.name}")


# --- Вспомогательная функция для преобразования изображения в base64 ---
def embed_image_base64(image_path):
    """
    Преобразует файл изображения в строку в формате base64 для встраивания в HTML.
    """
    try:
        with open(image_path, "rb") as image_file:
            return base64.b64encode(image_file.read()).decode('utf-8')
    except FileNotFoundError:
        logger.warning(f"Image file not found for base64 encoding: {image_path}")
        return ""
    except Exception as e:
        logger.error(f"Error encoding image to base64 from {image_path}: {e}")
        return ""

@fixture(scope="session")
def test_data():
    return load_test_data()