# Update user information (API) test-case
from playwright.sync_api import sync_playwright
import logging

logger = logging.getLogger(__name__)

def test_update_user_info():
    user_data = {
        "name": "user1",
        "email": "dggdgdgdggd@gmail.com",
        "password": "2zdhL@6XtPMsjdv",
        "title": "Mrs",
        "birth_date": "04",
        "birth_month": "May",
        "birth_year": "1996",
        "firstname": "Mary",
        "lastname": "Nice",
        "company": "ITS",
        "address1": "Random street 1",
        "address2": "Second address",
        "country": "US",
        "zipcode": "92208",
        "state": "California",
        "city": "Sacramento",
        "mobile_number": "+175757575775"
    }
    with sync_playwright() as p:
        request_context = p.request.new_context()
        url = "https://automationexercise.com/api/updateAccount"
        response = request_context.put(url, multipart = user_data)

        logger.info(f"Calling API:PUT:{url}")
        response_body = response.json()
        logger.info(f"Result from API:{response_body}")

        assert response.status == 200, f"Status code: {response.status}"
        assert response_body["responseCode"] == 200, f"Response code: {response_body['responseCode']}"
        assert response_body["message"] == "User updated!", f"Response message: {response_body['message']}"

# Search product without search product parameter (API), negative
def test_negative_search_without_product():
    with sync_playwright() as p:
        request_context = p.request.new_context()
        url = "https://automationexercise.com/api/searchProduct"
        response = request_context.post(url, data = {}, headers={ "Content-Type": "application/json" })

        logger.info(f"Calling API:POST:{url}")
        response_body = response.json()
        logger.info(f"Result from API:{response_body}")

        assert response.status == 200, f"Status code: {response.status}"
        assert response_body["message"] == "Bad request, search_product parameter is missing in POST request.", f"Response message: {response_body['message']}"
        assert response_body["responseCode"] == 400, f"Response code: {response_body['responseCode']}"