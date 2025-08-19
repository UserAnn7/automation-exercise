import requests

def create_account_function(user):
    """
        Создаёт аккаунт через API.

        :param user: dict – данные пользователя (например: test_data["users"]["user1"])
        :return: dict – результат запроса
    """

    url = "https://automationexercise.com/api/createAccount"
    try:
        response = requests.post(url, data=user)
        response.raise_for_status()  # выбросит исключение, если код ответа >= 400
        print(response.json())
        return response.json()  # возвращает данные в формате JSON
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}