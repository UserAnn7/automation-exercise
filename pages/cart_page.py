class CartPage:
    def __init__(self, page):
        self.page = page
        self.shopping_cart_header = page.locator("li.active", has_text="Shopping Cart")
        self.proceed_to_checkout_button = page.locator('a.btn.btn-default.check_out')

    # Click Proceed To Checkout
    def click_proceed_to_checkout(self):
        self.proceed_to_checkout_button.click()