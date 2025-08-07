from behave import when, then
from playwright.sync_api import expect
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.signup_page import SignupPage
from pages.account_created_page import AccountCreatedPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.order_placed_page import OrderPlacedPage
from pages.payment_page import PaymentPage
from pages.header import Header
from pages.account_deleted_page import AccountDeletedPage

@when('the user navigates to "{url}"')
def step_impl(context, url):
    context.page = context.browser.new_page()
    context.page.goto(url)

    context.home_page = HomePage(context.page)
    context.login_page = LoginPage(context.page, context.user)
    context.signup_page = SignupPage(context.page, context.user)
    context.account_created_page = AccountCreatedPage(context.page)
    context.cart_page = CartPage(context.page)
    context.checkout_page = CheckoutPage(context.page, context.user)
    context.order_placed_page = OrderPlacedPage(context.page)
    context.payment_page = PaymentPage(context.page, context.payment)
    context.header = Header(context.page)
    context.account_deleted_page = AccountDeletedPage(context.page)

@then("the home page is visible")
def step_impl(context):
    context.home_page.navigate_to_home_page()
    expect(context.header.home_tab).to_be_visible()

@when('the user clicks the "Signup / Login" button')
def step_impl(context):
    context.login_page.click_signup_login_button()

@when("fills in signup details and creates an account")
def step_impl(context):
    context.login_page.fill_details_in_signup_and_click_signup_button()
    context.signup_page.filling_in_account_registration_form_and_click_create_account()

@when('verifies account creation and clicks "Continue"')
def step_impl(context):
    expect(context.account_created_page.success_message).to_be_visible()
    context.account_created_page.continue_button_click()

@then('sees "Logged in as" at the top')
def step_impl(context):
    expect(context.header.logged_in_as(context.user["firstname"])).to_be_visible()

@when("adds a product to the cart")
def step_impl(context):
    context.home_page.add_product_to_cart()

@when("goes to the cart")
def step_impl(context):
    context.home_page.click_cart_button()
    expect(context.cart_page.shopping_cart_header).to_be_visible()

@when("proceeds to checkout")
def step_impl(context):
    context.cart_page.click_proceed_to_checkout()

@when("verifies address details and order summary")
def step_impl(context):
    checkout = context.checkout_page.scraped_address.all_text_contents()
    user = context.user
    assert user["firstname"] in checkout[1]
    assert user["lastname"] in checkout[1]
    assert user["company"] in checkout[2]
    assert user["address1"] in checkout[3]
    assert user["address2"] in checkout[4]
    assert user["mobile_number"] in checkout[7]

@when("enters a comment and places the order")
def step_impl(context):
    context.checkout_page.enter_comment_and_place_order()

@when("enters payment information")
def step_impl(context):
    context.payment_page.enter_payment()

@when("confirms the order")
def step_impl(context):
    context.payment_page.click_pay_and_confirm()

@then('the success message "Your order has been placed successfully!" should be visible')
def step_impl(context):
    expect(context.order_placed_page.confirmation_text).to_be_visible()

@when("the user deletes their account")
def step_impl(context):
    context.header.click_delete_account()

@then("the account deletion confirmation should be visible")
def step_impl(context):
    expect(context.account_deleted_page.account_deleted_title).to_be_visible()
    context.account_deleted_page.click_continue_on_account_deleted_page()