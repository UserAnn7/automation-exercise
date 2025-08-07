import requests

def check_if_user_exists(user):
    """
        Проверяет есть ли такой акк через API.

        :param user: dict – данные пользователя (например: test_data["users"]["user1"])
        :return: dict – результат запроса

        если пользователь существует будет 'responseCode': 200 в body ответа
        если пользователь не существует будет 'responseCode': 404 в body ответа
    """
    email = user["email"]
    url = "https://automationexercise.com/api/getUserDetailByEmail?email=" + email
    try:
        response = requests.get(url)
        response.raise_for_status()  # выбросит исключение, если код ответа >= 400
        print(response.json())
        return response.json()  # возвращает данные в формате JSON
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}