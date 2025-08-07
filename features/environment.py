from helpers.data_loader import load_test_data
from playwright.sync_api import sync_playwright

def before_all(context):
    context.test_data = load_test_data()
    context.user = context.test_data["users"]["user1"]
    context.payment = context.test_data["payment_info"]

def before_scenario(context, scenario):
    context.playwright = sync_playwright().start()
    context.browser = context.playwright.chromium.launch(headless=False)

def after_scenario(context, scenario):
    context.browser.close()
    context.playwright.stop()