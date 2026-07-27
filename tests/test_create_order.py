import allure
import data
from methods.order_methods import OrderMethods

class TestCreateOrder:

    @allure.title("Создание заказа авторизованным пользователем")
    def test_create_order_authorized(self, create_user, ingredient_id):
        payload = {"ingredients": [ingredient_id]}
        response = OrderMethods.create_order(payload, create_user["token"])
        assert response.status_code == 200
        assert response.json()["success"] is True

    @allure.title("Создание заказа без авторизации")
    def test_create_order_without_authorization(self, ingredient_id):
        payload = {"ingredients": [ingredient_id]}
        response = OrderMethods.create_order(payload)
        assert response.status_code == 200
        assert response.json()["success"] is True

    @allure.title("Создание заказа с ингредиентами")
    def test_create_order_with_ingredients(self, ingredient_id):
        payload = {"ingredients": [ingredient_id]}
        response = OrderMethods.create_order(payload)
        assert response.status_code == 200
        assert response.json()["success"] is True

    @allure.title("Создание заказа без ингредиентов")
    def test_create_order_without_ingredients(self):
        payload = {"ingredients": data.EMPTY_INGREDIENTS}
        response = OrderMethods.create_order(payload)
        assert response.status_code == 400
        assert response.json()["message"] == data.EMPTY_INGREDIENTS_MESSAGE

    @allure.title("Создание заказа с неверным хешем ингредиентов")
    def test_create_order_with_invalid_ingredients(self):
        payload = {"ingredients": data.INVALID_INGREDIENTS}
        response = OrderMethods.create_order(payload)
        assert response.status_code == 400