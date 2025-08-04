class AccountDeletedPage:
    def __init__(self, page):
        self.page = page
        self.account_deleted_title = page.locator('b', has_text='Account Deleted!')
        self.continue_btn = page.locator('a[data-qa="continue-button"]')

    # Click 'Continue' button on Account Deleted page
    def click_continue_on_account_deleted_page(self):
        self.continue_btn.click()