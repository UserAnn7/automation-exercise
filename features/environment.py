import allure
from allure_commons.types import AttachmentType

from helpers.data_loader import DataLoader
from playwright.sync_api import sync_playwright


def before_scenario(context, scenario):
    context.playwright = sync_playwright().start()
    context.browser = context.playwright.chromium.launch(headless=True)

    if 'multi_user' in scenario.tags:
        user_id = context.config.userdata.get("user_id")
        if not user_id:
            print("No user_id provided via --define user_id= -> adding default user_id = user1")
            user_id = "user1"
        test_data = DataLoader("data/user_data.json")
        users = test_data.data
        if user_id not in users:
            raise ValueError(f"user_id '{user_id}' not found in user_data.json")
        context.user = users[user_id]

def after_scenario(context, scenario):
    context.browser.close()
    context.playwright.stop()

def after_step(context, step):
    if step.status == "failed":
        screenshot = context.page.screenshot()
        allure.attach(screenshot, name="screenshot", attachment_type=AttachmentType.PNG)