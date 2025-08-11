from pages.base_page import BasePage
from playwright.sync_api import Page, Locator


class LoginPage(BasePage):
    SIGNUP_LOGIN_BUTTON_SELECTOR = "a[href='/login']"
    INPUT_NAME_SELECTOR = 'input[data-qa="signup-name"]'
    INPUT_EMAIL_SELECTOR = 'input[data-qa="signup-email"]'
    SIGNUP_BUTTON_SELECTOR = 'button[data-qa="signup-button"]'

    def __init__(self, page: Page) -> None:
        super().__init__(page)

    @property
    def signup_login_button(self) -> Locator:
        return self.page.locator(self.SIGNUP_LOGIN_BUTTON_SELECTOR)

    @property
    def input_name(self) -> Locator:
        return self.page.locator(self.INPUT_NAME_SELECTOR)

    @property
    def input_email(self) -> Locator:
        return self.page.locator(self.INPUT_EMAIL_SELECTOR)

    @property
    def signup_button(self) -> Locator:
        return self.page.locator(self.SIGNUP_BUTTON_SELECTOR)

    def click_signup_login_button(self) -> None:
        """Clicks the Signup/Login button."""
        self.signup_login_button.click()

    def fill_details_in_signup_and_click_signup_button(self, firstname: str, email: str) -> None:
        """Fills signup form with provided firstname and email, then clicks Signup button."""
        self.input_name.fill(firstname)
        self.input_email.fill(email)
        self.signup_button.click()