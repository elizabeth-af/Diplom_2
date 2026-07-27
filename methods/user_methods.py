import requests
from urls import Url
class UserMethods:

    @staticmethod
    def create_user(payload):
        return requests.post(Url.REGISTER_URL, json=payload)

    @staticmethod
    def login_user(payload):
        return requests.post(Url.LOGIN_URL, json=payload)

    @staticmethod
    def update_user(payload, token):
        headers = {
            "Authorization": token
        }
        return requests.patch(Url.USER_URL, json=payload, headers=headers)

    @staticmethod
    def update_user_without_auth(payload):
        return requests.patch(Url.USER_URL, json=payload)

    @staticmethod
    def delete_user(token):
        headers = {
            "Authorization": token
        }
        return requests.delete(Url.USER_URL, headers=headers)
