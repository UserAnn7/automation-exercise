def test_homepage_loads(page):
    page.goto("https://automationexercise.com")
    assert "Automation Exercise" in page.title()