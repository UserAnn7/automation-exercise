from helpers.attach_screenshot import attach_screenshot
from playwright.sync_api import expect

class AccountDeletedPage:
    def __init__(self, page):
        self.page = page
        self.account_deleted_title = page.locator('b', has_text='Account Deleted!')
        self.continue_btn = page.locator('a[data-qa="continue-button"]')

    # Verify 'ACCOUNT DELETED!' and click 'Continue' button
    def verify_account_deleted(self):
        expect(self.account_deleted_title).to_be_visible()
        attach_screenshot(self.page, name="Account Deleted")
        self.continue_btn.click()