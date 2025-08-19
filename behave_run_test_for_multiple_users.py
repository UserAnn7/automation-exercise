from helpers.data_loader import DataLoader
import subprocess

test_data = DataLoader("data/user_data.json")
users = test_data.data

for user_id in users:
    print(f"Running test for user: {user_id}")
    subprocess.run([
        "behave",
        "--tags=@multi_user",
        f"--define=user_id={user_id}"
    ])