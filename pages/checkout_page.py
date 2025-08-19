from pages.base_page import BasePage
from playwright.sync_api import Page, Locator


class CheckoutPage(BasePage):
    SCRAPED_ADDRESS_SELECTOR = "#address_delivery li"
    PRODUCT_IN_CART_SELECTOR = "tr#product-3"
    MESSAGE_INPUT_SELECTOR = "textarea[name='message']"
    PLACE_ORDER_BUTTON_SELECTOR = "a.btn.btn-default.check_out[href='/payment']"

    def __init__(self, page: Page) -> None:
        super().__init__(page)

    @property
    def scraped_address(self) -> Locator:
        return self.page.locator(self.SCRAPED_ADDRESS_SELECTOR)

    @property
    def product_in_cart(self) -> Locator:
        return self.page.locator(self.PRODUCT_IN_CART_SELECTOR)

    @property
    def message_input(self) -> Locator:
        return self.page.locator(self.MESSAGE_INPUT_SELECTOR)

    @property
    def place_order_button(self) -> Locator:
        return self.page.locator(self.PLACE_ORDER_BUTTON_SELECTOR)

    def enter_comment_and_place_order(self, comment: str = "My comment") -> None:
        """Fill the comment field and click the 'Place Order' button."""
        self.message_input.fill(comment)
        self.place_order_button.click()