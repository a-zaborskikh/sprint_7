import requests
from constans import Urls


class Courier:
    base_url = Urls.BASE_URL

    def create_courier(self, data):
        endpoint = '/api/v1/courier'
        url = self.base_url + endpoint
        return requests.post(url, data)

    def get_login_courier(self, data):
        endpoint = '/api/v1/courier/login'
        url = self.base_url + endpoint
        return requests.post(url, data)

    def delete_courier(self, data):
        get_login_id = self.get_login_courier(data)
        login_id = get_login_id.json()["id"]

        endpoint = f'/api/v1/courier/{login_id}'
        url = self.base_url + endpoint
        requests.delete(url)
