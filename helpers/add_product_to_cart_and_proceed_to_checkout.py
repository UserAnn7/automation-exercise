from playwright.sync_api import expect

class AddProductToCartAndProceedToCheckout:
    def __init__(self, page):
        self.page = page

    #8. Add products to cart
    def add_product_to_cart(self):
        product_card = self.page.locator('div.features_items div:nth-child(5)')
        product_card.hover()
        add_to_cart_btn = product_card.locator('div.product-overlay a[data-product-id="3"]')
        expect(add_to_cart_btn).to_be_visible()
        add_to_cart_btn.click()

    #9. Click 'Cart' button
    def click_cart_button(self):
        view_cart_link = self.page.locator("u", has_text="View Cart")
        expect(view_cart_link).to_be_visible()
        view_cart_link.click()

    #10. Verify that cart page is displayed
    def verify_cart_page_displayed(self):
        shopping_cart_header = self.page.locator("li.active", has_text="Shopping Cart")
        expect(shopping_cart_header).to_be_visible()

    #11. Click Proceed To Checkout
    def click_proceed_to_checkout(self):
        proceed_to_checkout_button = self.page.locator('a.btn.btn-default.check_out')
        expect(proceed_to_checkout_button).to_be_visible()
        proceed_to_checkout_button.click()