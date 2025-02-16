import allure
import pytest

from api.courier_api import Courier
from helpers import FakerDataGenerator
from constans import Errors
from data import CourierData


class TestLoginCourier:
    courier = Courier()
    random_data = FakerDataGenerator()
    error = Errors()

    @allure.title('Проверяем, что курьер может авторизоваться')
    def test_auth_courier_success(self):
        payload = {
            "login": self.random_data.get_login(),
            "password": self.random_data.get_password()
        }

        with allure.step("Создаем нового курьера"):
            self.courier.create_courier(payload)

        with allure.step("Логинимся новым курьером"):
            response = self.courier.get_login_courier(payload)

        with allure.step("Проверяем статус и текст сообщения"):
            data = response.json()
            assert response.status_code == 200
            assert 'id' in data and data['id'] > 0

        with allure.step("Удаляем курьера"):
            self.courier.delete_courier(payload)

    @allure.title('Проверяем, что нельзя авторизоваться курьером под несуществующим логином')
    def test_auth_courier_account_not_exists_error(self):
        payload = {
            "login": self.random_data.get_login(),
            "password": self.random_data.get_password()
        }

        with allure.step("Авторизуемся несуществующим логином курьера"):
            response = self.courier.get_login_courier(payload)

        with allure.step("Проверяем статус и текст сообщения"):
            data = response.json()
            assert response.status_code == 404
            assert data['message'] == self.error.ACCOUNT_NOT_EXISTS

    @pytest.mark.parametrize("login, password", CourierData.for_register_with_empty_filed)
    @allure.title('Проверяем, что курьер не авторизуется без обязательного поля(логин или пароль)')
    def test_auth_courier_with_empty_fields_error(self, login, password):
        payload_for_create_courier = {
            "login": self.random_data.get_login(),
            "password": self.random_data.get_password(),
            "firstName": self.random_data.get_first_name()
        }

        payload_for_login = {
            "login": login,
            "password": password
        }

        with allure.step("Создаем курьера"):
            self.courier.create_courier(payload_for_create_courier)

        with allure.step("Курьер не авторизуется без обязательного поля"):
            response = self.courier.get_login_courier(payload_for_login)

        with allure.step("Проверяем статус и текст сообщения"):
            data = response.json()
            assert response.status_code == 400
            assert data["message"] == self.error.NOT_ENOUGH_DATA_AUTH_COURIER

        with allure.step("Удаляем созданного курьера"):
            self.courier.delete_courier(payload_for_create_courier)
