from pages.base_page import BasePage
from playwright.sync_api import Page, Locator


class SignupPage(BasePage):
    RADIO_GENDER_FEMALE = '#id_gender2'
    PASSWORD_INPUT = 'input[data-qa="password"]'
    DAY_SELECT = 'select[data-qa="days"]'
    MONTH_SELECT = 'select[data-qa="months"]'
    YEAR_SELECT = 'select[data-qa="years"]'
    CHECKBOX_OFFERS = '#optin'
    COUNTRY_SELECT = 'select[data-qa="country"]'
    INPUT_NAME = 'input[data-qa="first_name"]'
    INPUT_LASTNAME = 'input[data-qa="last_name"]'
    INPUT_COMPANY = 'input[data-qa="company"]'
    INPUT_ADDRESS1 = 'input[data-qa="address"]'
    INPUT_ADDRESS2 = 'input[data-qa="address2"]'
    INPUT_STATE = 'input[data-qa="state"]'
    INPUT_CITY = 'input[data-qa="city"]'
    INPUT_ZIPCODE = 'input[data-qa="zipcode"]'
    INPUT_MOBILE_NUMBER = 'input[data-qa="mobile_number"]'
    CREATE_ACCOUNT_BUTTON = 'button[data-qa="create-account"]'

    def __init__(self, page: Page) -> None:
        super().__init__(page)

    @property
    def radio_gender_female(self) -> Locator:
        return self.page.locator(self.RADIO_GENDER_FEMALE)

    @property
    def password_input(self) -> Locator:
        return self.page.locator(self.PASSWORD_INPUT)

    @property
    def day_select(self) -> Locator:
        return self.page.locator(self.DAY_SELECT)

    @property
    def month_select(self) -> Locator:
        return self.page.locator(self.MONTH_SELECT)

    @property
    def year_select(self) -> Locator:
        return self.page.locator(self.YEAR_SELECT)

    @property
    def checkbox_offers(self) -> Locator:
        return self.page.locator(self.CHECKBOX_OFFERS)

    @property
    def country_select(self) -> Locator:
        return self.page.locator(self.COUNTRY_SELECT)

    @property
    def input_name(self) -> Locator:
        return self.page.locator(self.INPUT_NAME)

    @property
    def input_lastname(self) -> Locator:
        return self.page.locator(self.INPUT_LASTNAME)

    @property
    def input_company(self) -> Locator:
        return self.page.locator(self.INPUT_COMPANY)

    @property
    def input_address1(self) -> Locator:
        return self.page.locator(self.INPUT_ADDRESS1)

    @property
    def input_address2(self) -> Locator:
        return self.page.locator(self.INPUT_ADDRESS2)

    @property
    def input_state(self) -> Locator:
        return self.page.locator(self.INPUT_STATE)

    @property
    def input_city(self) -> Locator:
        return self.page.locator(self.INPUT_CITY)

    @property
    def input_zipcode(self) -> Locator:
        return self.page.locator(self.INPUT_ZIPCODE)

    @property
    def input_mobile_number(self) -> Locator:
        return self.page.locator(self.INPUT_MOBILE_NUMBER)

    @property
    def create_account_button(self) -> Locator:
        return self.page.locator(self.CREATE_ACCOUNT_BUTTON)

    def filling_in_account_registration_form_and_click_create_account(self, user_data: dict) -> None:
        """
        Fills in the account registration form and clicks the create account button.

        Args:
            user_data (dict): User data with keys:
                password, birth_date, birth_month, birth_year, country,
                firstname, lastname, company, address1, address2, state,
                city, zipcode, mobile_number
        """
        self.radio_gender_female.check()
        self.password_input.fill(user_data["password"])
        self.day_select.select_option(user_data["birth_date"])
        self.month_select.select_option(user_data["birth_month"])
        self.year_select.select_option(user_data["birth_year"])
        self.checkbox_offers.check()
        self.country_select.select_option(user_data["country"])
        self.input_name.fill(user_data["firstname"])
        self.input_lastname.fill(user_data["lastname"])
        self.input_company.fill(user_data["company"])
        self.input_address1.fill(user_data["address1"])
        self.input_address2.fill(user_data["address2"])
        self.input_state.fill(user_data["state"])
        self.input_city.fill(user_data["city"])
        self.input_zipcode.fill(user_data["zipcode"])
        self.input_mobile_number.fill(user_data["mobile_number"])
        self.create_account_button.click()