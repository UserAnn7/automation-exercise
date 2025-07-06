import allure
# from allure_commons.types import AttachmentType


def test_homepage_loads(page):
    with allure.step("Opening Home page"):
        page.goto("https://automationexercise.com")
        assert "Automation Exercise" in page.title()

#    allure.attach(page.screenshot(path="screenshot/screen1.png"), name="homepage_loads", attachment_type=AttachmentType.PNG)