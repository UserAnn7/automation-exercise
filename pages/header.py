class Header:
    def __init__(self, page):
        self.page = page
        self.logged_in_as = lambda username: page.locator(f"a:has-text('Logged in as {username}')")
        self.delete_account_btn = page.locator('a[href="/delete_account"]', has_text="Delete Account")
        self.home_tab = page.locator("a:has-text('Home')")

    # Click 'Delete Account' button
    def click_delete_account(self):
        self.delete_account_btn.click()