import pytest
from api.courier_api import Courier



#Эта фикстура не работает,  поэтому пока её не использую
@pytest.fixture(scope="function")
def delete_courier_fix(payload=None):
    """Фикстура для удаления курьера"""
    yield payload
    Courier().delete_courier(payload)
    print('удалено')
