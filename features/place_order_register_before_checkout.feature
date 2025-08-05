Feature: Place order as a new user
  Scenario: Successful order placement after account registration

    Given the user navigates to "http://automationexercise.com"
    And the home page is visible

    When the user clicks the "Signup / Login" button
    And fills in signup details and creates an account
    And verifies account creation and clicks "Continue"
    And sees "Logged in as" at the top

    And adds a product to the cart
    And goes to the cart
    And proceeds to checkout
    And verifies address details and order summary

    And enters a comment and places the order
    And enters payment information
    And confirms the order

    Then the success message "Your order has been placed successfully!" should be visible

    When the user deletes their account
    Then the account deletion confirmation should be visible