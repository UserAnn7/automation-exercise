import json
import os

def load_test_data():
    base_path = os.path.join(os.path.dirname(__file__), "..", "data")

    user_data_path = os.path.join(base_path, "user_data.json")
    payment_info_path = os.path.join(base_path, "payment_info.json")

    with open(user_data_path, encoding='utf-8') as f:
        user_data = json.load(f)

    with open(payment_info_path, encoding='utf-8') as f:
        payment_info = json.load(f)

    return {
        "users": user_data,
        "payment_info": payment_info
    }
