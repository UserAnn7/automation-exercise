from helpers.data_loader import load_test_data
from playwright.sync_api import sync_playwright

# def before_all(context):
#     context.test_data = load_test_data()
#     # context.user = context.test_data["users"]["user1"]
#     context.payment = context.test_data["payment_info"]

def before_scenario(context, scenario):
    context.playwright = sync_playwright().start()
    context.browser = context.playwright.chromium.launch(headless=False)
    context.test_data = load_test_data()
    context.payment = context.test_data["payment_info"]
    # context.user = context.test_data["users"]["user1"]

    if 'multi_user' in scenario.tags:
        user_id = context.config.userdata.get("user_id")
        if not user_id:
            raise ValueError("No user_id provided via --define user_id=...")

        users = load_test_data()["users"]

        if user_id not in users:
            raise ValueError(f"user_id '{user_id}' not found in user_data.json")

        context.user = users[user_id]

def after_scenario(context, scenario):
    context.browser.close()
    context.playwright.stop()