from pages.signup_page import SignupPage
from pages.account_info_page import AccountInfoPage
from pages.header import Header
from playwright.sync_api import expect
from data.user_data import UserData

class AccountCreation:
    def __init__(self, page):
        self.page = page
        self.signup_page = SignupPage(page)
        self.account_info_page = AccountInfoPage(page)
        self.header = Header(page)
        self.user = UserData()

    def click_signup_login_button(self):
        expect(self.signup_page.signup_login_button).to_be_visible()
        self.signup_page.signup_login_button.click()

    # 5.Fill all details in Signup and create account
    def fill_details_in_signup_and_click_signup_button(self):
        expect(self.signup_page.input_name).to_be_visible()
        self.signup_page.input_name.fill(self.user.first_name)

        expect(self.signup_page.input_email).to_be_visible()
        self.signup_page.input_email.fill(self.user.email)

        expect(self.signup_page.signup_button).to_be_visible()
        self.signup_page.signup_button.click()

    # Filling in Enter Account Information form
    def filling_in_account_registration_form_and_click_create_account(self):
        expect(self.account_info_page.radio_gender_female).to_be_visible()
        self.account_info_page.radio_gender_female.check()

        expect(self.account_info_page.password_input).to_be_visible()
        self.account_info_page.password_input.fill(self.user.password)

        expect(self.account_info_page.day_select).to_be_visible()
        self.account_info_page.day_select.select_option(self.user.dayOfBirth)

        expect(self.account_info_page.month_select).to_be_visible()
        self.account_info_page.month_select.select_option(self.user.monthOfBirth)

        expect(self.account_info_page.year_select).to_be_visible()
        self.account_info_page.year_select.select_option(self.user.yearOfBirth)

        expect(self.account_info_page.checkbox_offers).to_be_visible()
        self.account_info_page.checkbox_offers.check()

        expect(self.account_info_page.country_select).to_be_visible()
        self.account_info_page.country_select.select_option(self.user.country)

        expect(self.account_info_page.input_first_name).to_be_visible()
        self.account_info_page.input_first_name.fill(self.user.first_name)

        expect(self.account_info_page.input_last_name).to_be_visible()
        self.account_info_page.input_last_name.fill(self.user.last_name)

        expect(self.account_info_page.input_company).to_be_visible()
        self.account_info_page.input_company.fill(self.user.company)

        expect(self.account_info_page.input_address).to_be_visible()
        self.account_info_page.input_address.fill(self.user.address)

        expect(self.account_info_page.input_address2).to_be_visible()
        self.account_info_page.input_address2.fill(self.user.address2)

        expect(self.account_info_page.input_state).to_be_visible()
        self.account_info_page.input_state.fill(self.user.state)

        expect(self.account_info_page.input_city).to_be_visible()
        self.account_info_page.input_city.fill(self.user.city)

        expect(self.account_info_page.input_zipcode).to_be_visible()
        self.account_info_page.input_zipcode.fill(self.user.zipcode)

        expect(self.account_info_page.input_mobile_number).to_be_visible()
        self.account_info_page.input_mobile_number.fill(self.user.mobile_number)

        expect(self.account_info_page.create_account_button).to_be_visible()
        self.account_info_page.create_account_button.click()

    # 6. Verify 'ACCOUNT CREATED!' and click 'Continue' button
    def verify_that_account_created_and_click_continue_button(self):
        expect(self.account_info_page.success_message).to_be_visible()
        self.account_info_page.continue_button.click()

    # 7. Verify 'Logged in as username' at top
    def verify_logged_in_as_username(self):
        logged_in_element = self.header.logged_in_as(self.user.first_name)
        expect(logged_in_element).to_be_visible()