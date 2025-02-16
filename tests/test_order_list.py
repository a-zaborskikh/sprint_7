import allure

from api.courier_api import Courier
from api.order_api import Order
from helpers import FakerDataGenerator


class TestOrderList:
    order = Order()
    random_data = FakerDataGenerator()
    courier = Courier()

    @allure.title("В тело ответа возвращается список заказов")
    def test_order_list_return_list(self):
        payload = {
            "login": self.random_data.get_login(),
            "password": self.random_data.get_password()
        }
        with allure.step("Создаем нового курьера"):
            self.courier.create_courier(payload)
        with allure.step("Получаем его логин"):
            data = self.courier.get_login_courier(payload).json()
            id_courier = data['id']
            print(id_courier)

        with allure.step("Запрашиваем список заказов у курьера по логину"):
            response = self.order.get_order_list(id_courier)
            data = response.json()

        with allure.step("Проверяем статус и текст сообщения"):
            assert response.status_code == 200
            assert isinstance(data['orders'], list)
