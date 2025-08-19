import requests

from helpers.data_loader import DataLoader

def delete_account_function(user):
    """
        Удаляет аккаунт через API.

        :param user: dict – данные пользователя (например: test_data["users"]["user1"])
        :return: dict – результат запроса
    """
    url = "https://automationexercise.com/api/deleteAccount"
    email_and_password = ["email", "password"]
    new_dict={}
    for k in email_and_password:
        if k in user:
            new_dict[k] = user[k]
    print(new_dict)

    try:
        response = requests.delete(url, data=new_dict)
        response.raise_for_status()  # выбросит исключение, если код ответа >= 400
        print(response.json())
        return response.json()  # возвращает данные в формате JSON
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}


# test_data = DataLoader("../data/user_data.json")
# delete_account_function(test_data.data["user1"])