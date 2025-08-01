import tempfile
import allure
from allure_commons.types import AttachmentType
from playwright.sync_api import Page

def attach_screenshot(page: Page, name: str = "Screenshot"):
    """Сохраняет и прикрепляет скриншот к Allure отчёту."""
    with tempfile.NamedTemporaryFile(suffix=".png", delete=False) as tmp_file:
        page.screenshot(path=tmp_file.name)
        allure.attach.file(tmp_file.name, name=name, attachment_type=AttachmentType.PNG)