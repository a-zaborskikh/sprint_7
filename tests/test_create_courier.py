import allure
import pytest

from api.courier_api import Courier
from helpers import FakerDataGenerator
from constans import Errors
from data import CourierData


class TestCreateCourier:
    courier = Courier()
    random_data = FakerDataGenerator()
    error = Errors()

    @allure.title('Проверяем, что курьер корректно создан')
    def test_create_new_courier_success(self):
        payload = {
            "login": self.random_data.get_login(),
            "password": self.random_data.get_password(),
            "firstName": self.random_data.get_first_name()
        }

        with allure.step("Создаем нового курьера"):
            response = self.courier.create_courier(payload)

        with allure.step("Проверяем статус и текст сообщения"):
            data = response.json()
            assert response.status_code == 201
            assert data["ok"] is True

        with allure.step("Удаляем созданного курьера"):
            self.courier.delete_courier(payload)

    @allure.title('Проверяем, что нельзя создать двух одинаковых курьеров')
    def test_create_double_couriers_error(self):
        payload = {
            "login": self.random_data.get_login(),
            "password": self.random_data.get_password(),
            "firstName": self.random_data.get_first_name()
        }

        with allure.step("Создаем нового курьера"):
            self.courier.create_courier(payload)

        with allure.step("Создаем повторно одного и того же курьера"):
            response = self.courier.create_courier(payload)

        with allure.step("Проверяем статус и текст сообщения"):
            data = response.json()
            assert response.status_code == 409
            assert data["message"] == self.error.LOGIN_EXISTS

        with allure.step("Удаляем созданного курьера"):
            self.courier.delete_courier(payload)

    @pytest.mark.parametrize("login, password", CourierData.for_register_with_empty_filed)
    @allure.title('Проверяем, что курьер не создан без обязательного поля')
    def test_create_courier_with_empty_fields_error(self, login, password):
        payload = {
            "login": login,
            "password": password
        }

        with allure.step("Отправляем запрос без обязательного поля (логин или пароль)"):
            response = self.courier.create_courier(payload)

        with allure.step("Проверяем статус и текст сообщения"):
            data = response.json()
            assert response.status_code == 400
            assert data["message"] == self.error.NOT_ENOUGH_DATA_CREATE_COURIER
