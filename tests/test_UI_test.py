# Place Order: Register before Checkout
from playwright.sync_api import expect
import logging
import pytest
import allure
from helpers.account_creation import AccountCreation
from helpers.add_product_to_cart_and_proceed_to_checkout import AddProductToCartAndProceedToCheckout
from helpers.delete_account import DeleteAccount
from helpers.place_order import PlaceOrder

logger = logging.getLogger(__name__)

@pytest.mark.ui
def test_place_order_register_before_checkout(page):
    with allure.step("Navigate to url 'http://automationexercise.com'"):
        page.goto("http://automationexercise.com")
        consent_button = page.locator("p.fc-button-label:has-text('Consent')")
        expect(consent_button).to_be_visible()
        consent_button.click()
    with allure.step("Verify that home page is visible successfully"):
        assert page.url == "https://automationexercise.com/"
        home_tab = page.locator("a:has-text('Home')")
        expect(home_tab).to_be_visible()
        color = home_tab.evaluate("el => getComputedStyle(el).color")
        assert color == "rgb(255, 165, 0)"
    with allure.step("Create account"):
        account_creation = AccountCreation(page)
        account_creation.click_signup_login_button()
        account_creation.fill_details_in_signup_and_click_signup_button()
        account_creation.filling_in_account_registration_form_and_click_create_account()
        account_creation.verify_that_account_created_and_click_continue_button()
        account_creation.verify_loggeed_in_as_username()

    with allure.step("Add product to cart and proceed to checkout"):
        add_product = AddProductToCartAndProceedToCheckout(page)
        add_product.add_product_to_cart()
        add_product.click_cart_button()
        add_product.verify_cart_page_displayed()
        add_product.click_proceed_to_checkout()

    with allure.step("Place order"):
        place_order = PlaceOrder(page)
        place_order.verify_address_and_product_in_chart()
        place_order.enter_comment_and_place_order()
        place_order.enter_payment()
        place_order.click_pay_and_confirm()
        place_order.verify_success_message_for_placing_order()

    with allure.step("Delete account"):
        delete_account = DeleteAccount(page)
        delete_account.click_delete_account()
        delete_account.verify_account_deleted()