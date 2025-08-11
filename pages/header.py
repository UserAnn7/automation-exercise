from pages.base_page import BasePage
from playwright.sync_api import Page, Locator


class Header(BasePage):
    # Locator constants
    DELETE_ACCOUNT_BTN = ('a[href="/delete_account"]', {"has_text": "Delete Account"})
    HOME_TAB_SELECTOR = "a:has-text('Home')"

    def __init__(self, page: Page):
        super().__init__(page)

    def logged_in_as(self, username: str) -> Locator:
        """Returns a locator for the 'Logged in as {username}' element."""
        return self.page.locator(f"a:has-text('Logged in as {username}')")

    @property
    def delete_account_btn(self) -> Locator:
        selector, options = self.DELETE_ACCOUNT_BTN
        return self.page.locator(selector, **options)

    @property
    def home_tab(self) -> Locator:
        return self.page.locator(self.HOME_TAB_SELECTOR)

    def click_delete_account(self) -> None:
        """Clicks on the 'Delete Account' button."""
        self.delete_account_btn.click()