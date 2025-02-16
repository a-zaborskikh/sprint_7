from helpers import FakerDataGenerator


class CourierData:
    random = FakerDataGenerator()
    for_register_with_empty_filed = [
        ("", random.get_password()),  # Логин пуст
        (random.get_login(), "")  # Пароль пуст
    ]


class ChoiceColor:
    choice_color = [
        ['BLACK'],
        ['GREY'],
        ['BLACK', 'GREY'],
        []
    ]
