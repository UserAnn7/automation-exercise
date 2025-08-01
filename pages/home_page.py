class HomePage:
    def __init__(self, page):
        self.page = page
        self.product_card = page.locator('div.features_items div:nth-child(5)')
        self.add_to_cart_btn = page.locator('div.product-overlay a[data-product-id="3"]')
        self.view_cart_link = page.locator("u", has_text="View Cart")
        self.consent_button = page.locator("p.fc-button-label:has-text('Consent')")

    # Navigate to url 'http://automationexercise.com and accept cookies popup
    def navigate_to_home_page(self):
        self.page.goto("http://automationexercise.com")
        self.consent_button.click()

    # Add products to cart
    def add_product_to_cart(self):
        self.product_card.hover()
        self.add_to_cart_btn.click()

    # Click 'Cart' button
    def click_cart_button(self):
        self.view_cart_link.click()