class AccountInfoPage:
    def __init__(self, page):
        self.page = page

        self.radio_gender_female = page.locator('input#id_gender2')
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
        self.success_message = page.locator("b", has_text="Account Created!")
        self.continue_button = page.locator('a[data-qa="continue-button"]')