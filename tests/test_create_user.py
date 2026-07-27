import allure
import data
import helpers
import pytest
from methods.user_methods import UserMethods

class TestCreateUser:

    @allure.title("Создание уникального пользователя")
    def test_create_unique_user(self):
        user = data.create_user_data()
        response = UserMethods.create_user(user)
        assert response.status_code == 200
        assert response.json()["success"] is True
        token = helpers.get_token(response)
        UserMethods.delete_user(token)

    @allure.title("Создание пользователя, который уже зарегистрирован")
    def test_create_existing_user(self):
        user = data.create_user_data()
        create_response = UserMethods.create_user(user)
        token = helpers.get_token(create_response)
        response = UserMethods.create_user(user)
        assert response.status_code == 403
        assert response.json()["message"] == data.USER_ALREADY_EXISTS_MESSAGE
        UserMethods.delete_user(token)

    @allure.title("Создание пользователя без обязательного поля {field}")
    @pytest.mark.parametrize("field",
        [
            "email",
            "password",
            "name"
        ]
    )
    def test_create_user_without_required_field(self, field):
        user = data.create_user_data()
        del user[field]
        response = UserMethods.create_user(user)
        assert response.status_code == 403
        assert response.json()["message"] == data.REQUIRED_FIELDS_MESSAGE
