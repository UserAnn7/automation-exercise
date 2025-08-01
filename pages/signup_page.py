from helpers.attach_screenshot import attach_screenshot


class SignupPage:
    def __init__(self, page, test_data):
        self.page = page
        self.radio_gender_female = page.locator('#id_gender2')
        self.password_input = page.locator('input[data-qa="password"]')
        self.day_select = page.locator('select[data-qa="days"]')
        self.month_select = page.locator('select[data-qa="months"]')
        self.year_select = page.locator('select[data-qa="years"]')
        self.checkbox_offers = page.locator('#optin')
        self.country_select = page.locator('select[data-qa="country"]')
        self.input_first_name = page.locator('input[data-qa="first_name"]')
        self.input_last_name = page.locator('input[data-qa="last_name"]')
        self.input_company = page.locator('input[data-qa="company"]')
        self.input_address = page.locator('input[data-qa="address"]')
        self.input_address2 = page.locator('input[data-qa="address2"]')
        self.input_state = page.locator('input[data-qa="state"]')
        self.input_city = page.locator('input[data-qa="city"]')
        self.input_zipcode = page.locator('input[data-qa="zipcode"]')
        self.input_mobile_number = page.locator('input[data-qa="mobile_number"]')
        self.create_account_button = page.locator('button[data-qa="create-account"]')
        self.user = test_data["user_for_UI_tests"]

    # Filling in Enter Account Information form
    def filling_in_account_registration_form_and_click_create_account(self):
        self.radio_gender_female.check()
        self.password_input.fill(self.user["password"])
        self.day_select.select_option(self.user["dayOfBirth"])
        self.month_select.select_option(self.user["monthOfBirth"])
        self.year_select.select_option(self.user["yearOfBirth"])
        self.checkbox_offers.check()
        self.country_select.select_option(self.user["country"])
        self.input_first_name.fill(self.user["first_name"])
        self.input_last_name.fill(self.user["last_name"])
        self.input_company.fill(self.user["company"])
        self.input_address.fill(self.user["address"])
        self.input_address2.fill(self.user["address2"])
        self.input_state.fill(self.user["state"])
        self.input_city.fill(self.user["city"])
        self.input_zipcode.fill(self.user["zipcode"])
        self.input_mobile_number.fill(self.user["mobile_number"])
        attach_screenshot(self.page, name="Form filled successfully")
        self.create_account_button.click()