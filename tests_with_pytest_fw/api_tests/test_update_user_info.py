from playwright.sync_api import sync_playwright
import logging

logger = logging.getLogger(__name__)

# Update user information (API) test-case
def test_update_user_info(test_data):
    with sync_playwright() as p:
        request_context = p.request.new_context()
        url = "https://automationexercise.com/api/updateAccount"
        response = request_context.put(url, multipart = test_data["users"]["user2"])

        logger.info(f"Calling API:PUT:{url}")
        response_body = response.json()
        logger.info(f"Result from API:{response_body}")

        assert response.status == 200, f"Status code: {response.status}"
        assert response_body["responseCode"] == 200, f"Response code: {response_body['responseCode']}"
        assert response_body["message"] == "User updated!", f"Response message: {response_body['message']}"