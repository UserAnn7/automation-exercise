# Place Order: Register before Checkout
from playwright.sync_api import Page, expect

def test_place_order_register_before_checkout(page):
    #2.Navigate to url 'http://automationexercise.com' and closing "This site asks for consent to use your data" pop-up
    page.goto("http://automationexercise.com")
    consent_button = page.locator("p.fc-button-label:has-text('Consent')")
    expect(consent_button).to_be_visible()
    consent_button.click()
    #3.Verify that home page is visible successfully
    assert page.url == "https://automationexercise.com/"
    home_tab = page.locator("a:has-text('Home')")
    expect(home_tab).to_be_visible()
    color = home_tab.evaluate("el => getComputedStyle(el).color")
    assert color == "rgb(255, 165, 0)"
    #4.Click 'Signup / Login' button
    signup_login_button = page.locator("a[href='/login']:has-text('Signup / Login')")
    expect(signup_login_button).to_be_visible()
    signup_login_button.click()
    #5.Fill all details in Signup and create account
    input_name = page.locator('input[data-qa="signup-name"]')
    expect(input_name).to_be_visible()
    input_name.fill("Ann")
    input_email = page.locator('input[data-qa="signup-email"]')
    expect(input_email).to_be_visible()
    input_email.fill("mynewemail@gmail.com")
    signup_button = page.locator('button[data-qa="signup-button"]')
    expect(signup_button).to_be_visible()
    signup_button.click()
    # Filling in Enter Account Information form
    def filling_in_account_registration_form():
        radio_button = page.locator('input#id_gender2')
        expect(radio_button).to_be_visible()
        radio_button.check()

        password_input = page.locator('input[data-qa="password"]')
        expect(password_input).to_be_visible()
        password_input.fill("Pass1234")

        day_select = page.locator('select[data-qa="days"]')
        expect(day_select).to_be_visible()
        day_select.select_option("7")

        month_select = page.locator('select[data-qa="months"]')
        expect(month_select).to_be_visible()
        month_select.select_option("5")

        year_select = page.locator('select[data-qa="years"]')
        expect(year_select).to_be_visible()
        year_select.select_option("1997")

        checkbox_receive_special_offers  = page.locator('#optin')
        expect(checkbox_receive_special_offers).to_be_visible()
        checkbox_receive_special_offers.check()

        country_select = page.locator('select[data-qa="country"]')
        expect(country_select).to_be_visible()
        country_select.select_option("United States")

        address_info = {
            'input[data-qa="first_name"]': "Ann",
            'input[data-qa="last_name"]': "Skipor",
            'input[data-qa="company"]': "ITS",
            'input[data-qa="address"]': "Best street",
            'input[data-qa="address2"]': "Best street2",
            'input[data-qa="state"]': "Best street2",
            'input[data-qa="city"]': "New York",
            'input[data-qa="zipcode"]': "02776",
            'input[data-qa="mobile_number"]': "+2345678990"
        }

        for selector, value in address_info.items():
            locator = page.locator(selector)
            expect(locator).to_be_visible()
            locator.fill(value)

    filling_in_account_registration_form()

    create_account_button = page.locator('button[data-qa="create-account"]')
    expect(create_account_button).to_be_visible()
    create_account_button.click()
    #6. Verify 'ACCOUNT CREATED!' and click 'Continue' button



