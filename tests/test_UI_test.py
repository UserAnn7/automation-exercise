# Place Order: Register before Checkout
from playwright.sync_api import Page, expect
import logging
import pytest
import tests.data.address_info as address_info

logger = logging.getLogger(__name__)

@pytest.mark.ui
def test_place_order_register_before_checkout(page):
    #2.Navigate to url 'http://automationexercise.com' and closing "This site asks for consent to use your data" pop-up
    page.goto("http://automationexercise.com")

    logger.info("This is an informational message.")
#    logger.debug("This is a debug message.")
    logger.warning("This is a warning message.")

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
    username = "Ann"
    input_name.fill(username)
    input_email = page.locator('input[data-qa="signup-email"]')
    expect(input_email).to_be_visible()
    input_email.fill("qwerty1234567@gmail.com")
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
        password_input.fill("1234")

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

        for selector, value in address_info.address_info.items():
            locator = page.locator(selector)
            expect(locator).to_be_visible()
            locator.fill(value)

    filling_in_account_registration_form()

    create_account_button = page.locator('button[data-qa="create-account"]')
    expect(create_account_button).to_be_visible()
    create_account_button.click()
    #6. Verify 'ACCOUNT CREATED!' and click 'Continue' button

    success_message = page.locator("b", has_text="Account Created!")
    expect(success_message).to_be_visible()

    continue_button = page.locator('a[data-qa="continue-button"]')
    expect(continue_button).to_be_visible()
    continue_button.click()

    #7. Verify 'Logged in as username' at top
    logged_in_element = page.locator(f"a:has-text('Logged in as {username}')")
    expect(logged_in_element).to_be_visible()

    #8. Add products to cart
    #add_to_cart_button = page.locator('a[data-product-id="3"]')
    #expect(add_to_cart_button).to_be_visible()
    #add_to_cart_button.click()
    # Наводим на карточку товара, чтобы появился overlay
    product_card = page.locator('div.features_items div:nth-child(5)')
    product_card.hover()

    # Кликаем по нужной кнопке в overlay
    add_to_cart_btn = product_card.locator('div.product-overlay a[data-product-id="3"]')
    expect(add_to_cart_btn).to_be_visible()
    add_to_cart_btn.click()

    #9. Click 'Cart' button
    view_cart_link = page.locator("u", has_text="View Cart")
    expect(view_cart_link).to_be_visible()
    view_cart_link.click()

    #10. Verify that cart page is displayed
    shopping_cart_header = page.locator("li.active", has_text="Shopping Cart")
    expect(shopping_cart_header).to_be_visible()

    #11. Click Proceed To Checkout
    proceed_to_checkout_button = page.locator('a.btn.btn-default.check_out')
    expect(proceed_to_checkout_button).to_be_visible()
    proceed_to_checkout_button.click()

    #12. Verify Address Details and Review Your Order

    scraped_address = page.locator("#address_delivery li")
    logger.info(f'Denis: {scraped_address.all_text_contents()}')
    # print(f'Ann: {scraped_address.dir}')

    [_, full_name, company, street1, street2, city_state_zip, country, phone] = scraped_address.all_text_contents()

    assert address_info.first_name in full_name, f"Entered first name {address_info.first_name} is not in displayed name: {full_name}"
    assert address_info.last_name in full_name, f"Entered last name {address_info.last_name} is not in displayed name: {full_name}"

    assert address_info.company == company, f"Entered company {address_info.company} doesn't match displayed {company}"
    assert address_info.address == street1, f"Entered address {address_info.address} doesn't match displayed {street1}"
    assert address_info.address2 == street2, f"Entered address {address_info.address2} doesn't match displayed {street2}"
    assert address_info.mobile_number == phone, f"Entered phone number {address_info.mobile_number} doesn't match displayed {phone}"

    product_in_cart = page.locator('tr#product-3')
    expect(product_in_cart).to_be_visible()

    #13. Enter description in comment text area and click 'Place Order'
    message_input = page.locator('textarea[name="message"]')
    expect(message_input).to_be_visible()
    message_input.fill("My comment")

    place_order_button = page.locator('a.btn.btn-default.check_out[href="/payment"]')
    expect(place_order_button).to_be_visible()
    place_order_button.click()

    #14. Enter payment details: Name on Card, Card Number, CVC, Expiration date
    name_on_card_input = page.locator('input[data-qa="name-on-card"]')
    expect(name_on_card_input).to_be_visible()
    name_on_card_input.fill("Ann Skipor")

    card_number_input = page.locator('input[data-qa="card-number"]')
    expect(card_number_input).to_be_visible()
    card_number_input.fill("1234 5678 9012 3456")

    cvc_input = page.locator('input[data-qa="cvc"]')
    expect(cvc_input).to_be_visible()
    cvc_input.fill("311")

    expiry_month_input = page.locator('input[data-qa="expiry-month"]')
    expect(expiry_month_input).to_be_visible()
    expiry_month_input.fill("12")

    expiry_year_input = page.locator('input[data-qa="expiry-year"]')
    expect(expiry_year_input).to_be_visible()
    expiry_year_input.fill("2025")

    #15. Click 'Pay and Confirm Order' button
    pay_button = page.locator('button[data-qa="pay-button"]')
    expect(pay_button).to_be_visible()
    pay_button.click()

    #16. Verify success message 'Your order has been placed successfully!'
    confirmation_text = page.locator('p', has_text="Congratulations! Your order has been confirmed!")
    expect(confirmation_text).to_be_visible()

    #17. Click 'Delete Account' button
    delete_account_btn = page.locator('a[href="/delete_account"]', has_text="Delete Account")
    expect(delete_account_btn).to_be_visible()
    delete_account_btn.click()

    #18. Verify 'ACCOUNT DELETED!' and click 'Continue' button
    account_deleted = page.locator('b', has_text='Account Deleted!')
    expect(account_deleted).to_be_visible()

    continue_btn = page.locator('a[data-qa="continue-button"]')
    expect(continue_btn).to_be_visible()
    continue_btn.click()

