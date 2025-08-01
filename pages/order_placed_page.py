from playwright.sync_api import expect

class OrderPlacedPage:
    def __init__(self, page):
        self.page = page
        self.confirmation_text = page.locator('p', has_text="Congratulations! Your order has been confirmed!")
    # Verify success message 'Your order has been placed successfully!'
    def verify_success_message_for_placing_order(self):
        expect(self.confirmation_text).to_be_visible()