class CheckoutPage:
    def __init__(self, page, test_data):
        self.page = page
        self.scraped_address = page.locator("#address_delivery li")
        self.product_in_cart = page.locator('tr#product-3')
        self.message_input = page.locator('textarea[name="message"]')
        self.place_order_button = page.locator('a.btn.btn-default.check_out[href="/payment"]')
        self.user = test_data["user_data"]["user_for_UI_tests"]

    # Verify Address Details and Review Your Order
    def verify_address_and_product_in_chart(self):
        [_, full_name, company, street1, street2, city_state_zip, country, phone] = self.scraped_address.all_text_contents()
        assert self.user["first_name"] in full_name, f"Entered first name '{self.user['first_name']}' is not in displayed name: '{full_name}'"
        assert self.user["last_name"] in full_name, f"Entered last name '{self.user['last_name']}' is not in displayed name: '{full_name}'"
        assert self.user["company"] in company, f"Entered company '{self.user['company']}' is not in displayed: '{company}'"
        assert self.user["address"] in street1, f"Entered address '{self.user['address']}' is not in displayed: '{street1}'"
        assert self.user["address2"] in street2, f"Entered address2 '{self.user['address2']}' is not in displayed: '{street2}'"
        assert self.user["mobile_number"] in phone, f"Entered phone number '{self.user['mobile_number']}' is not in displayed: '{phone}'"

    # Enter description in comment text area and click 'Place Order'
    def enter_comment_and_place_order(self):
        self.message_input.fill("My comment")
        self.place_order_button.click()