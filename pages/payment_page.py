class PaymentPage:
    def __init__(self, page):
        self.page = page
        self.name_on_card_input = page.locator('input[data-qa="name-on-card"]')
        self.card_number_input = page.locator('input[data-qa="card-number"]')
        self.cvc_input = page.locator('input[data-qa="cvc"]')
        self.expiry_month_input = page.locator('input[data-qa="expiry-month"]')
        self.expiry_year_input = page.locator('input[data-qa="expiry-year"]')
        self.pay_button = page.locator('button[data-qa="pay-button"]')

    # Enter payment details: Name on Card, Card Number, CVC, Expiration date
    def enter_payment(self):
        self.name_on_card_input.fill("Ann Skipor")
        self.card_number_input.fill("1234 5678 9012 3456")
        self.cvc_input.fill("311")
        self.expiry_month_input.fill("12")
        self.expiry_year_input.fill("2025")

    # Click 'Pay and Confirm Order' button
    def click_pay_and_confirm(self):
        self.pay_button.click()