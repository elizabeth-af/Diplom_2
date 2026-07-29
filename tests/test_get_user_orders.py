import allure
import data
from methods.order_methods import OrderMethods

class TestGetUserOrders:

    @allure.title("Получение заказов авторизованным пользователем")
    def test_get_user_orders_authorized(self, create_user, ingredient_id):
        payload = {"ingredients": [ingredient_id]}
        OrderMethods.create_order(payload, create_user["token"])
        response = OrderMethods.get_user_orders(create_user["token"])
        assert response.status_code == 200
        assert response.json()["success"] is True
        assert "orders" in response.json()

    @allure.title("Получение заказов неавторизованным пользователем")
    def test_get_user_orders_without_authorization(self):
        response = OrderMethods.get_user_orders()
        assert response.status_code == 401
        assert response.json()["message"] == data.UNAUTHORIZED_MESSAGE