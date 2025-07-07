class SignupPage:
    def __init__(self, page):
        self.page = page
        self.signup_login_button = page.locator("a[href='/login']:has-text('Signup / Login')")
        self.input_name = page.locator('input[data-qa="signup-name"]')
        self.input_email = page.locator('input[data-qa="signup-email"]')
        self.signup_button = page.locator('button[data-qa="signup-button"]')