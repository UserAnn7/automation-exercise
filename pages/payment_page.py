from pages.base_page import BasePage
from playwright.sync_api import Page, Locator


class PaymentPage(BasePage):
    NAME_ON_CARD_SELECTOR = 'input[data-qa="name-on-card"]'
    CARD_NUMBER_SELECTOR = 'input[data-qa="card-number"]'
    CVC_SELECTOR = 'input[data-qa="cvc"]'
    EXPIRY_MONTH_SELECTOR = 'input[data-qa="expiry-month"]'
    EXPIRY_YEAR_SELECTOR = 'input[data-qa="expiry-year"]'
    PAY_BUTTON_SELECTOR = 'button[data-qa="pay-button"]'

    def __init__(self, page: Page) -> None:
        super().__init__(page)

    @property
    def name_on_card_input(self) -> Locator:
        return self.page.locator(self.NAME_ON_CARD_SELECTOR)

    @property
    def card_number_input(self) -> Locator:
        return self.page.locator(self.CARD_NUMBER_SELECTOR)

    @property
    def cvc_input(self) -> Locator:
        return self.page.locator(self.CVC_SELECTOR)

    @property
    def expiry_month_input(self) -> Locator:
        return self.page.locator(self.EXPIRY_MONTH_SELECTOR)

    @property
    def expiry_year_input(self) -> Locator:
        return self.page.locator(self.EXPIRY_YEAR_SELECTOR)

    @property
    def pay_button(self) -> Locator:
        return self.page.locator(self.PAY_BUTTON_SELECTOR)

    def enter_payment(self, payment: dict) -> None:
        """
        Fill payment details form.

        Args:
            payment (dict): Payment info with keys:
                - name_on_card
                - card_number
                - cvc
                - expiry_month
                - expiry_year
        """
        self.name_on_card_input.fill(payment["name_on_card"])
        self.card_number_input.fill(payment["card_number"])
        self.cvc_input.fill(payment["cvc"])
        self.expiry_month_input.fill(payment["expiry_month"])
        self.expiry_year_input.fill(payment["expiry_year"])

    def click_pay_and_confirm(self) -> None:
        """Click the 'Pay and Confirm Order' button."""
        self.pay_button.click()