from playwright.sync_api import sync_playwright
import logging

logger = logging.getLogger(__name__)

# Search product without search product parameter (API), negative
def test_negative_search_without_product():
    with sync_playwright() as p: #starts playwright, creates p object
        request_context = p.request.new_context() #creating seesion for sending requests
        url = "https://automationexercise.com/api/searchProduct"
        response = request_context.post(url, data = {}, headers={ "Content-Type": "application/json" })

        logger.info(f"Calling API:POST:{url}")
        response_body = response.json()
        logger.info(f"Result from API:{response_body}")

        assert response.status == 200, f"Status code: {response.status}"
        assert response_body["message"] == "Bad request, search_product parameter is missing in POST request.", f"Response message: {response_body['message']}"
        assert response_body["responseCode"] == 400, f"Response code: {response_body['responseCode']}"

        # The same API test but using pytest not playwright
        # import requests
        # def test_negative_search_without_product():
        #     url = "https://automationexercise.com/api/searchProduct"
        #     headers = {"Content-Type": "application/json"}
        #     data = {}  # пустой JSON объект
        #
        #     logger.info(f"Calling API: POST: {url}")
        #     response = requests.post(url, json=data, headers=headers)  # отправляем POST с JSON
        #     response_body = response.json()
        #     logger.info(f"Result from API: {response_body}")
        #
        #     assert response.status_code == 200, f"Status code: {response.status_code}"
        #     assert response_body[
        #                "message"] == "Bad request, search_product parameter is missing in POST request.", f"Response message: {response_body['message']}"
        #     assert response_body["responseCode"] == 400, f"Response code: {response_body['responseCode']}"