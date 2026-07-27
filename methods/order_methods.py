import requests
from urls import Url

class OrderMethods:

    @staticmethod
    def get_ingredients():
        return requests.get(Url.INGREDIENTS_URL)

    @staticmethod
    def create_order(payload, token=None):
        headers = {}
        if token:
            headers["Authorization"] = token
        return requests.post(Url.ORDERS_URL, json=payload, headers=headers)

    @staticmethod
    def get_user_orders(token=None):
        headers = {}
        if token:
            headers["Authorization"] = token
        return requests.get(Url.ORDERS_URL,headers=headers)