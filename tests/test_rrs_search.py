import allure
import pytest
from base.base_test import BaseTest


@allure.feature("Search")
class TestSearch(BaseTest):

    @allure.title("Search test")
    @allure.severity("Medium")
    @pytest.mark.smoke
    def test_login(self):
        self.rrs_login.open()                               # открытие страницы
        self.rrs_login.invoices_and_orders()                # открытие стрыницы Счета заказы
        self.rrs_login.enter_login(self.data.LOGIN)         # ввод логина
        self.rrs_login.enter_password(self.data.PASSWORD)   # ввод пароля
        self.rrs_login.click_submit_button()                # вход
        self.rrs_search.search_button()                     # открытие страницы товаров
        self.rrs_login.close_offer()                        # закрытие офера
        self.rrs_search.enter_search_1()                    # выбор товара
        self.rrs_search.enter_search_2()                    # выбор товара
        self.rrs_search.search()                            # открытие страницы корзины
        self.rrs_search.check()                             # выбор товара
        self.rrs_search.delete()                            # удаление товара
        self.rrs_search.design()                            # подтверждение покупки предварительное
        self.rrs_search.design_ok()                         # подтверждение покупки
        self.rrs_search.make_screenshot("Screenshot")
