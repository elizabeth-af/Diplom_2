def get_token(response):
    return response.json()["accessToken"]


def get_ingredient_id(response):
    return response.json()["data"][0]["_id"]