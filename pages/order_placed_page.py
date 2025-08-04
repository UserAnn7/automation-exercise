class OrderPlacedPage:
    def __init__(self, page):
        self.page = page
        self.confirmation_text = page.locator('p', has_text="Congratulations! Your order has been confirmed!")