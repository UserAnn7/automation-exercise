from helpers.data_loader import load_test_data

def before_all(context):
    context.test_data = load_test_data()
    context.user = context.test_data["user_data"]["user_for_UI_tests"]
    context.payment = context.test_data["payment_info"]