from pages.base_page import BasePage
from playwright.sync_api import Page, Locator


class AccountCreatedPage(BasePage):
    SUCCESS_MESSAGE = ("b", {"has_text": "Account Created!"})
    CONTINUE_BUTTON = "a[data-qa='continue-button']"

    def __init__(self, page: Page) -> None:
        super().__init__(page)

    @property
    def success_message(self) -> Locator:
        selector, options = self.SUCCESS_MESSAGE
        return self.page.locator(selector, **options)

    @property
    def continue_button(self) -> Locator:
        return self.page.locator(self.CONTINUE_BUTTON)

    def continue_button_click(self) -> None:
        """Clicks the 'Continue' button on Account Created page."""
        self.continue_button.click()