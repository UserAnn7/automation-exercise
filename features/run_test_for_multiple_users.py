from helpers.data_loader import load_test_data
import subprocess

users = load_test_data()["users"]

for user_id in users:
    print(f"Running test for user: {user_id}")
    subprocess.run([
        "behave",
        "--tags=@multi_user",
        "--define", f"user_id={user_id}"
    ])