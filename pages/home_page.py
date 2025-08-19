from pages.base_page import BasePage
from playwright.sync_api import Page, Locator


class HomePage(BasePage):
    PRODUCT_CARD_SELECTOR = 'div.features_items div:nth-child(5)'
    ADD_TO_CART_BTN_SELECTOR = 'div.product-overlay a[data-product-id="3"]'
    VIEW_CART_LINK_SELECTOR = "u:has-text('View Cart')"
    CONSENT_BUTTON_SELECTOR = "p.fc-button-label:has-text('Consent')"

    def __init__(self, page: Page) -> None:
        super().__init__(page)

    @property
    def product_card(self) -> Locator:
        return self.page.locator(self.PRODUCT_CARD_SELECTOR)

    @property
    def add_to_cart_btn(self) -> Locator:
        return self.page.locator(self.ADD_TO_CART_BTN_SELECTOR)

    @property
    def view_cart_link(self) -> Locator:
        return self.page.locator(self.VIEW_CART_LINK_SELECTOR)

    @property
    def consent_button(self) -> Locator:
        return self.page.locator(self.CONSENT_BUTTON_SELECTOR)

    def navigate_to_home_page(self) -> None:
        """Navigate to homepage and accept cookies popup if present."""
        self.page.goto("http://automationexercise.com")
        try:
            self.consent_button.click()
        except Exception:
            # Consent button may not always appear
            pass

    def add_product_to_cart(self) -> None:
        """Hover over product and click 'Add to Cart' button."""
        self.product_card.hover()
        self.add_to_cart_btn.click()

    def click_cart_button(self) -> None:
        """Click the 'View Cart' link."""
        self.view_cart_link.click()
