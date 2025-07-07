from playwright.sync_api import expect
from data.user_data import UserData


class AccountCreation:
    def __init__(self, page):
        self.page = page

    def click_signup_login_button(self):
        signup_login_button = self.page.locator("a[href='/login']:has-text('Signup / Login')")
        expect(signup_login_button).to_be_visible()
        signup_login_button.click()

    # 5.Fill all details in Signup and create account
    def fill_details_in_signup_and_click_signup_button(self):
        input_name = self.page.locator('input[data-qa="signup-name"]')
        expect(input_name).to_be_visible()
        user = UserData()
        input_name.fill(user.first_name)
        input_email = self.page.locator('input[data-qa="signup-email"]')
        expect(input_email).to_be_visible()
        input_email.fill(user.email)
        signup_button = self.page.locator('button[data-qa="signup-button"]')
        expect(signup_button).to_be_visible()
        signup_button.click()

    # Filling in Enter Account Information form
    def filling_in_account_registration_form_and_click_create_account(self):
        radio_button = self.page.locator('input#id_gender2')
        expect(radio_button).to_be_visible()
        radio_button.check()

        password_input = self.page.locator('input[data-qa="password"]')
        expect(password_input).to_be_visible()
        user = UserData()
        password_input.fill(user.password)

        day_select = self.page.locator('select[data-qa="days"]')
        expect(day_select).to_be_visible()
        day_select.select_option("7")

        month_select = self.page.locator('select[data-qa="months"]')
        expect(month_select).to_be_visible()
        month_select.select_option("5")

        year_select = self.page.locator('select[data-qa="years"]')
        expect(year_select).to_be_visible()
        year_select.select_option("1997")

        checkbox_receive_special_offers = self.page.locator('#optin')
        expect(checkbox_receive_special_offers).to_be_visible()
        checkbox_receive_special_offers.check()

        country_select = self.page.locator('select[data-qa="country"]')
        expect(country_select).to_be_visible()
        country_select.select_option("United States")

        user = UserData()

        for selector, value in user.address_info.items():
            locator = self.page.locator(selector)
            expect(locator).to_be_visible()
            locator.fill(value)

        create_account_button = self.page.locator('button[data-qa="create-account"]')
        expect(create_account_button).to_be_visible()
        create_account_button.click()
    # 6. Verify 'ACCOUNT CREATED!' and click 'Continue' button
    def verify_that_account_created_and_click_continue_button(self):
        success_message = self.page.locator("b", has_text="Account Created!")
        expect(success_message).to_be_visible()

        continue_button = self.page.locator('a[data-qa="continue-button"]')
        expect(continue_button).to_be_visible()
        continue_button.click()

     # 7. Verify 'Logged in as username' at top
    def verify_loggeed_in_as_username(self):
        user = UserData()
        logged_in_element = self.page.locator(f"a:has-text('Logged in as {user.first_name}')")
        expect(logged_in_element).to_be_visible()