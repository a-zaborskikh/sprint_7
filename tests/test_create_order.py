import json
import allure
import pytest

from api.order_api import Order
from helpers import FakerDataGenerator
from constans import Errors
from data import ChoiceColor


class TestCreateOrder:
    order = Order()
    faker_data = FakerDataGenerator()
    error = Errors()

    @pytest.mark.parametrize("color", ChoiceColor.choice_color)
    @allure.title('Проверяем, что заказ оформляется с разными цветами и без')
    def test_create_order_with_different_colors_success(self, color):
        payload = {
            "firstName": self.faker_data.get_first_name(),
            "lastName": self.faker_data.get_last_name(),
            "address": self.faker_data.get_address(),
            "metroStation": self.faker_data.get_metro_stations_number(),
            "phone": self.faker_data.get_phone_number(),
            "rentTime": self.faker_data.get_rent_time_number(),
            "deliveryDate": self.faker_data.get_today_date(),
            "comment": self.faker_data.get_random_comment(),
            "color": color
        }

        with allure.step("Создаем заказ"):
            payload_json = json.dumps(payload)
            response = self.order.create_order(payload_json)

        with allure.step("Проверяем статус и текст сообщения"):
            data = response.json()
            assert response.status_code == 201
            assert 'track' in data and data["track"] > 0
