import pytest
from config.data import Data
from pages.login_pg import RrsLoginPage
from pages.search_pg import RrsSearchPage
from pages.admin_pg import RrsAdminPage

class BaseTest:                             # базовый для наших тестов для инотации типов

    data: Data                              # из данных (пароли)

    rrs_login: RrsLoginPage
    rrs_search: RrsSearchPage
    rrs_admin: RrsAdminPage

    @pytest.fixture(autouse=True)           # autouse=True для всех тестов она применяется
    def setup(self, request, driver):       # фикстура
        request.cls.driver = driver  # чтобы в тестах могли использовать драйвер
        request.cls.data = Data()
        request.cls.rrs_login = RrsLoginPage(driver)
        request.cls.rrs_search = RrsSearchPage(driver)
        request.cls.rrs_admin = RrsAdminPage(driver)
