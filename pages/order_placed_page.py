from pages.base_page import BasePage
from playwright.sync_api import Page, Locator


class OrderPlacedPage(BasePage):
    CONFIRMATION_TEXT_SELECTOR = 'p'

    def __init__(self, page: Page) -> None:
        super().__init__(page)

    @property
    def confirmation_text(self) -> Locator:
        return self.page.locator(self.CONFIRMATION_TEXT_SELECTOR, has_text="Congratulations! Your order has been confirmed!")