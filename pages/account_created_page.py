class AccountCreatedPage:
    def __init__(self, page):
        self.page = page
        self.success_message = page.locator("b", has_text="Account Created!")
        self.continue_button = page.locator('a[data-qa="continue-button"]')

    # Click 'Continue' button on Account Created page
    def continue_button_click(self):
        self.continue_button.click()