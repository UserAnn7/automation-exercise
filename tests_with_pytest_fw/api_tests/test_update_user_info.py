from playwright.sync_api import sync_playwright
import logging
from helpers.check_if_user_exists import check_if_user_exists
from helpers.create_account_function import create_account_function
from helpers.delete_account_function import delete_account_function
from helpers.data_loader import load_test_data

logger = logging.getLogger(__name__)

# Update user information (API) test-case
def test_update_user_info():
    test_data = load_test_data()
    response_check = check_if_user_exists(test_data["users"]["user2"])
    logger.info(f"Result for checking if acc already exists: {response_check}")
    if response_check["responseCode"] != 200:
        create_account_function(test_data["users"]["user2"])
        logger.info("Creating account")
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

    response_del = delete_account_function(test_data["users"]["user2"])
    logger.info(f"Deleting Account: {response_del}")