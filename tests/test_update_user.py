import allure
import data
import pytest

from methods.user_methods import UserMethods


class TestUpdateUser:

    @allure.title("Изменение email авторизованным пользователем")
    def test_update_email_authorized(self, create_user):
        new_email = f"new_{create_user['user']['email']}"
        response = UserMethods.update_user({"email": new_email},create_user["token"])
        assert response.status_code == 200
        assert response.json()["success"] is True
        assert response.json()["user"]["email"] == new_email

    @allure.title("Изменение имени авторизованным пользователем")
    def test_update_name_authorized(self, create_user):
        new_name = "New Test User"
        response = UserMethods.update_user({"name": new_name},create_user["token"])
        assert response.status_code == 200
        assert response.json()["success"] is True
        assert response.json()["user"]["name"] == new_name

    @allure.title("Изменение пароля авторизованным пользователем")
    def test_update_password_authorized(self, create_user):
        new_password = "new_password123"
        response = UserMethods.update_user({"password": new_password},create_user["token"])
        assert response.status_code == 200
        assert response.json()["success"] is True

    @allure.title("Изменение поля {field} без авторизации")
    @pytest.mark.parametrize("field, value",
        [
            ("email", "new_email@mail.ru"),
            ("password", "new_password123"),
            ("name", "New Test User")
        ]
    )
    def test_update_user_without_authorization(self, field, value):
        response = UserMethods.update_user_without_auth({field: value})
        assert response.status_code == 401
        assert response.json()["message"] == data.UNAUTHORIZED_MESSAGE