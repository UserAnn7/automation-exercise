from playwright.sync_api import expect

class DeleteAccount:
    def __init__(self, page):
        self.page = page

    # 17. Click 'Delete Account' button
    def click_delete_account(self):
        delete_account_btn = self.page.locator('a[href="/delete_account"]', has_text="Delete Account")
        expect(delete_account_btn).to_be_visible()
        delete_account_btn.click()

    # 18. Verify 'ACCOUNT DELETED!' and click 'Continue' button
    def verify_account_deleted(self):
        account_deleted = self.page.locator('b', has_text='Account Deleted!')
        expect(account_deleted).to_be_visible()

        continue_btn = self.page.locator('a[data-qa="continue-button"]')
        expect(continue_btn).to_be_visible()
        continue_btn.click()