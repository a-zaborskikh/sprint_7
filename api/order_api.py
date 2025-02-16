import requests

from constans import Urls


class Order:
    base_url = Urls.BASE_URL

    def create_order(self, data):
        endpoint = '/api/v1/orders'
        url = self.base_url + endpoint
        return requests.post(url, data)

    def get_order_list(self, id_courier):
        endpoint = f'/api/v1/orders?courierId={id_courier}'
        url = self.base_url + endpoint
        return requests.get(url, id_courier)
