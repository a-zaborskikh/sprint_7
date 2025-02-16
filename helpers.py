import random
from faker import Faker
from datetime import datetime


class FakerDataGenerator:
    def __init__(self):
        self.fake = Faker('ru_RU')

    def get_login(self):
        return f'courier-{self.fake.user_name()}'

    def get_password(self):
        return self.fake.password()

    def get_first_name(self):
        return self.fake.first_name()

    def get_last_name(self):
        return self.fake.last_name()

    def get_address(self):
        return self.fake.street_name() + ', дом ' + str(random.randint(1, 100))

    def get_phone_number(self):
        return self.fake.numerify('8925#######')

    def get_random_comment(self):
        """Генерация рандомного комментария"""
        if random.choice([True, False]):
            random_comment = self.fake.sentence()
        else:
            random_comment = ""

        return random_comment

    @staticmethod
    def get_rent_time_number():
        return random.randint(1, 7)

    @staticmethod
    def get_metro_stations_number():
        return random.randint(1, 237)

    @staticmethod
    def get_today_date():
        return str(datetime.now().date())
