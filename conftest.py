import pytest
import helpers
from data import create_user_data
from methods.user_methods import UserMethods
from methods.order_methods import OrderMethods


@pytest.fixture
def create_user():
    user = create_user_data()
    response = UserMethods.create_user(user)
    token = helpers.get_token(response)
    yield {
        "user": user,
        "token": token
    }
    UserMethods.delete_user(token)

@pytest.fixture
def delete_user():
    data = {}

    yield data

    if "token" in data:
        UserMethods.delete_user(data["token"])

@pytest.fixture
def ingredient_id():
    response = OrderMethods.get_ingredients()
    return helpers.get_ingredient_id(response)