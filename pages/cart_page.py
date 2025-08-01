from playwright.sync_api import expect

class CartPage:
    def __init__(self, page):
        self.page = page
        self.shopping_cart_header = page.locator("li.active", has_text="Shopping Cart")
        self.proceed_to_checkout_button = page.locator('a.btn.btn-default.check_out')

    # Verify that cart page is displayed
    def verify_cart_page_displayed(self):
        expect(self.shopping_cart_header).to_be_visible()

    # Click Proceed To Checkout
    def click_proceed_to_checkout(self):
        self.proceed_to_checkout_button.click()