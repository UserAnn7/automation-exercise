class LoginPage:
    def __init__(self, page, test_data):
        self.page = page
        self.signup_login_button = page.locator("a[href='/login']")
        self.input_name = page.locator('input[data-qa="signup-name"]')
        self.input_email = page.locator('input[data-qa="signup-email"]')
        self.signup_button = page.locator('button[data-qa="signup-button"]')
        self.user = test_data["user_data"]["user_for_UI_tests"]

    def click_signup_login_button(self):
        self.signup_login_button.click()

    # Fill all details in Signup and create account
    def fill_details_in_signup_and_click_signup_button(self):
        self.input_name.fill(self.user["first_name"])
        self.input_email.fill(self.user["email"])

        self.signup_button.click()