class Header:
    def __init__(self, page):
        self.page = page
        self.logged_in_as = lambda username: page.locator(f"a:has-text('Logged in as {username}')")