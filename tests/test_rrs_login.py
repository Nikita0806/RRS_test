import allure
import pytest
from base.base_test import BaseTest


@allure.feature("Login")
class TestLogin(BaseTest):

    @allure.title("Login")
    @allure.severity("Medium")
    @pytest.mark.smoke
    def test_login(self):
        self.rrs_login.open()                                 # открытие страницы
        self.rrs_login.invoices_and_orders()                  # открытие стрыницы Счета заказы
        self.rrs_login.enter_login(self.data.LOGIN)           # ввод логина
        self.rrs_login.enter_password(self.data.PASSWORD)     # ввод пароля
        self.rrs_login.click_submit_button()                  # вход
        self.rrs_login.close_offer()                          # закрытие офера
        self.rrs_login.make_screenshot("Screenshot")
