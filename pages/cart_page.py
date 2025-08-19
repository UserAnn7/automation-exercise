from pages.base_page import BasePage
from playwright.sync_api import Page, Locator


class CartPage(BasePage):
    SHOPPING_CART_HEADER = ("li.active", {"has_text": "Shopping Cart"})
    PROCEED_TO_CHECKOUT_BTN = "a.btn.btn-default.check_out"

    def __init__(self, page: Page) -> None:
        super().__init__(page)

    @property
    def shopping_cart_header(self) -> Locator:
        selector, options = self.SHOPPING_CART_HEADER
        return self.page.locator(selector, **options)

    @property
    def proceed_to_checkout_button(self) -> Locator:
        return self.page.locator(self.PROCEED_TO_CHECKOUT_BTN)

    def click_proceed_to_checkout(self) -> None:
        """Clicks the 'Proceed To Checkout' button."""
        self.proceed_to_checkout_button.click()