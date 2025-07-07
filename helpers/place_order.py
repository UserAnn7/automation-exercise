from playwright.sync_api import expect
from data.user_data import UserData

class PlaceOrder:
    def __init__(self, page):
        self.page = page

    # 12. Verify Address Details and Review Your Order
    def verify_address_and_product_in_chart(self):
        scraped_address = self.page.locator("#address_delivery li")
        [_, full_name, company, street1, street2, city_state_zip, country, phone] = scraped_address.all_text_contents()
        user = UserData()
        assert user.first_name in full_name, f"Entered first name {user.first_name} is not in displayed name: {full_name}"
        assert user.last_name in full_name, f"Entered last name {user.last_name} is not in displayed name: {full_name}"
        assert user.company == company, f"Entered company {user.company} doesn't match displayed {company}"
        assert user.address == street1, f"Entered address {user.address} doesn't match displayed {street1}"
        assert user.address2 == street2, f"Entered address {user.address2} doesn't match displayed {street2}"
        assert user.mobile_number == phone, f"Entered phone number {user.mobile_number} doesn't match displayed {phone}"
        product_in_cart = self.page.locator('tr#product-3')
        expect(product_in_cart).to_be_visible()

    # 13. Enter description in comment text area and click 'Place Order'
    def enter_comment_and_place_order(self):
        message_input = self.page.locator('textarea[name="message"]')
        expect(message_input).to_be_visible()
        message_input.fill("My comment")

        place_order_button = self.page.locator('a.btn.btn-default.check_out[href="/payment"]')
        expect(place_order_button).to_be_visible()
        place_order_button.click()

    # 14. Enter payment details: Name on Card, Card Number, CVC, Expiration date
    def enter_payment(self):
        name_on_card_input = self.page.locator('input[data-qa="name-on-card"]')
        expect(name_on_card_input).to_be_visible()
        name_on_card_input.fill("Ann Skipor")

        card_number_input = self.page.locator('input[data-qa="card-number"]')
        expect(card_number_input).to_be_visible()
        card_number_input.fill("1234 5678 9012 3456")

        cvc_input = self.page.locator('input[data-qa="cvc"]')
        expect(cvc_input).to_be_visible()
        cvc_input.fill("311")

        expiry_month_input = self.page.locator('input[data-qa="expiry-month"]')
        expect(expiry_month_input).to_be_visible()
        expiry_month_input.fill("12")

        expiry_year_input = self.page.locator('input[data-qa="expiry-year"]')
        expect(expiry_year_input).to_be_visible()
        expiry_year_input.fill("2025")

    # 15. Click 'Pay and Confirm Order' button
    def click_pay_and_confirm(self):
        pay_button = self.page.locator('button[data-qa="pay-button"]')
        expect(pay_button).to_be_visible()
        pay_button.click()

    # 16. Verify success message 'Your order has been placed successfully!'
    def verify_success_message_for_placing_order(self):
        confirmation_text = self.page.locator('p', has_text="Congratulations! Your order has been confirmed!")
        expect(confirmation_text).to_be_visible()