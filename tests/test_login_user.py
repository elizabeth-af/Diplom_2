import allure
import data
import pytest
import helpers
from methods.user_methods import UserMethods

class TestLoginUser:

    @allure.title("Логин под существующим пользователем")
    def test_login_existing_user(self, create_user):
        user = create_user["user"]
        response = UserMethods.login_user(user)
        assert response.status_code == 200
        assert response.json()["success"] is True

    @allure.title("Логин с неверным {field}")
    @pytest.mark.parametrize("field, value",
        [
            ("email", "wrong_email@mail.ru"),
            ("password", "wrong_password")
        ]
    )
    def test_login_with_wrong_credentials(self, field, value):
        user = data.create_user_data()
        user[field] = value
        response = UserMethods.login_user(user)
        assert response.status_code == 401
        assert response.json()["message"] == data.INVALID_CREDENTIALS_MESSAGE