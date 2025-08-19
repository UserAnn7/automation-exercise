from pages.base_page import BasePage
from playwright.sync_api import Page, Locator


class AccountDeletedPage(BasePage):
    ACCOUNT_DELETED_TITLE = ("b", {"has_text": "Account Deeted!"})
    CONTINUE_BTN = "a[data-qa='continue-button']"

    def __init__(self, page: Page) -> None:
        super().__init__(page)

    @property
    def account_deleted_title(self) -> Locator:
        selector, options = self.ACCOUNT_DELETED_TITLE
        return self.page.locator(selector, **options)

    @property
    def continue_btn(self) -> Locator:
        return self.page.locator(self.CONTINUE_BTN)

    def click_continue_on_account_deleted_page(self) -> None:
        """Clicks the 'Continue' button on Account Deleted page."""
        self.continue_btn.click()