class CheckoutPage:
    def __init__(self, page, user):
        self.page = page
        self.scraped_address = page.locator("#address_delivery li")
        self.product_in_cart = page.locator('tr#product-3')
        self.message_input = page.locator('textarea[name="message"]')
        self.place_order_button = page.locator('a.btn.btn-default.check_out[href="/payment"]')
        self.user = user

    # Enter description in comment text area and click 'Place Order'
    def enter_comment_and_place_order(self):
        self.message_input.fill("My comment")
        self.place_order_button.click()