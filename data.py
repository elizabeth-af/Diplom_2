import random

#генерация данных пользователя
def create_user_data():
    return {
        "email": f"test_{random.randint(100000, 999999)}@mail.ru",
        "password": "password123",
        "name": "Test User"
    }

#генерация пользователя без почты
def user_without_email():
    user = create_user_data()
    del user["email"]
    return user


def user_without_password():
    user = create_user_data()
    del user["password"]
    return user

def user_without_name():
    user = create_user_data()
    del user["name"]

    return user

def get_valid_ingredient(response):
    ingredients = response.json()["data"]
    return ingredients[0]["_id"]

#текст ошибок
USER_ALREADY_EXISTS_MESSAGE = "User already exists"
REQUIRED_FIELDS_MESSAGE = "Email, password and name are required fields"
INVALID_CREDENTIALS_MESSAGE = "email or password are incorrect"
UNAUTHORIZED_MESSAGE = "You should be authorised"
EMPTY_INGREDIENTS_MESSAGE = "Ingredient ids must be provided"

# Неверный хеш ингредиента
INVALID_INGREDIENTS = ["000000000000000000000000"]
# Пустой список ингредиентов
EMPTY_INGREDIENTS = []