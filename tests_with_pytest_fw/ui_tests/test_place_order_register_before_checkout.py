# Place Order: Register before Checkout
from playwright.sync_api import expect
import logging
import pytest
import allure
from helpers.attach_screenshot import attach_screenshot
from pages.account_created_page import AccountCreatedPage
from pages.account_deleted_page import AccountDeletedPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.header import Header
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.order_placed_page import OrderPlacedPage
from pages.payment_page import PaymentPage
from pages.signup_page import SignupPage
logger = logging.getLogger(__name__)

@pytest.mark.ui
def test_place_order_register_before_checkout(page, test_data):
    user = test_data["user_data"]["user_for_UI_tests"]
    payment = test_data["payment_info"]
    home_page = HomePage(page)
    login_page = LoginPage(page,user)
    signup_page = SignupPage(page, user)
    account_created_page = AccountCreatedPage(page)
    cart_page = CartPage(page)
    checkout_page = CheckoutPage(page, user)
    order_placed_page = OrderPlacedPage(page)
    payment_page = PaymentPage(page, payment)
    header = Header(page)
    account_deleted_page = AccountDeletedPage(page)

    with allure.step("Launch browser"): #Not sure if the step is needed
        logger.info("Browser launched")

    with allure.step("Navigate to url 'http://automationexercise.com'"):
        home_page.navigate_to_home_page()
        logger.info("'http://automationexercise.com' is opened")

    with allure.step("Verify that home page is visible successfully"):
        assert page.url == "https://automationexercise.com/"
        expect(header.home_tab).to_be_visible()
        color = header.home_tab.evaluate("el => getComputedStyle(el).color")
        assert color == "rgb(255, 165, 0)"
        attach_screenshot(page, name="User is on Home page")
        logger.info("Home page is visible")

    with allure.step("Click 'Signup / Login' button"):
        login_page.click_signup_login_button()
        logger.info("'Signup / Login' button is clicked")

    with allure.step("Fill all details in Signup and create account"):
        login_page.fill_details_in_signup_and_click_signup_button()
        signup_page.filling_in_account_registration_form_and_click_create_account()
        logger.info("Details filled in Signup and create account button is clicked")

    with allure.step("Verify 'ACCOUNT CREATED!' and click 'Continue' button"):
        expect(account_created_page.success_message).to_be_visible()
        attach_screenshot(page, name="Account created")
        account_created_page.continue_button_click()
        logger.info("Account is created successfully")

    with allure.step("Verify ' Logged in as username' at top"):
        logged_in_element = header.logged_in_as(user["first_name"])
        expect(logged_in_element).to_be_visible()
        attach_screenshot(page, name="Logged in as correct user")
        logger.info("' Logged in as username' is displayed at top")

    with allure.step("Add product to cart"):
        home_page.add_product_to_cart()
        logger.info("Product added to cart")

    with allure.step("Click 'Cart' button"):
        home_page.click_cart_button()
        logger.info("'Cart' button is clicked")

    with allure.step("Verify that cart page is displayed"):
        expect(cart_page.shopping_cart_header).to_be_visible()
        attach_screenshot(page, name="Cart page")
        logger.info("User is on Cart page")

    with allure.step("Click Proceed To Checkout"):
        cart_page.click_proceed_to_checkout()
        logger.info("'Proceed To Checkout' button is clicked'")

    with allure.step("Verify Address Details and Review Your Order"):
        [_, full_name, company, street1, street2, city_state_zip, country, phone] = checkout_page.scraped_address.all_text_contents()
        assert user["first_name"] in full_name, f"Entered first name '{user['first_name']}' is not in displayed name: '{full_name}'"
        assert user["last_name"] in full_name, f"Entered last name '{user['last_name']}' is not in displayed name: '{full_name}'"
        assert user["company"] in company, f"Entered company '{user['company']}' is not in displayed: '{company}'"
        assert user[ "address"] in street1, f"Entered address '{user['address']}' is not in displayed: '{street1}'"
        assert user["address2"] in street2, f"Entered address2 '{user['address2']}' is not in displayed: '{street2}'"
        assert user["mobile_number"] in phone, f"Entered phone number '{user['mobile_number']}' is not in displayed: '{phone}'"
        attach_screenshot(page, name="Address Details and Order")
        logger.info("Address details are verified")

    with allure.step("Enter description in comment text area and click 'Place Order'"):
        checkout_page.enter_comment_and_place_order()
        logger.info("'Place Order' button is clicked'")

    with allure.step("Enter payment details: Name on Card, Card Number, CVC, Expiration date"):
        payment_page.enter_payment()
        logger.info("Payment info is entered")

    with allure.step("Click 'Pay and Confirm Order' button"):
        payment_page.click_pay_and_confirm()
        logger.info("'Pay and Confirm Order' button is clicked'")

    with allure.step("Verify success message 'Your order has been placed successfully!'"):
        expect(order_placed_page.confirmation_text).to_be_visible()
        attach_screenshot(page, name="Order placed successfully")
        logger.info("Order is placed successfully")

    with allure.step("Click 'Delete Account' button"):
        header.click_delete_account()
        logger.info("'Delete Account' button is clicked'")

    with allure.step("Verify 'ACCOUNT DELETED!' and click 'Continue' button"):
        expect(account_deleted_page.account_deleted_title).to_be_visible()
        attach_screenshot(page, name="Account Deleted")
        account_deleted_page.click_continue_on_account_deleted_page()
        logger.info("Account is deleted")