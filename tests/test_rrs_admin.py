import allure
import pytest
from base.base_test import BaseTest

@allure.feature("Admin")
class TestAdmin(BaseTest):

    @allure.title("Admin test")
    @allure.severity("Medium")
    @pytest.mark.smoke
    def test_login(self):
        self.rrs_admin.open()                               # открытие страницы
        self.rrs_admin.enter_login(self.data.LOGIN_A)         # ввод логина
        self.rrs_admin.enter_password(self.data.PASSWORD_A)   # ввод пароля
        self.rrs_admin.click_submit_button()                # нажатие на кнопку входа
        self.rrs_admin.drop_down_list()                     # нажатие на выпадающий список
        self.rrs_admin.report()                             # нажатие на отчет
        self.rrs_admin.suppliers_report()                   # выбор нужного отчета
        self.rrs_admin.add_report()                         # создание нового отчета
        self.rrs_admin.data_input_start('01.02.2024')           # ввод даты
        self.rrs_admin.timer_enter_start()                  # выбор времени
        self.rrs_admin.data_input_end('29.02.2024')          # ввод даты
        self.rrs_admin.timer_enter_and()                    # выбор времени
        self.rrs_admin.scrol_down()                         # скролл
        self.rrs_admin.suppliers_all()                      # все поставщики
        self.rrs_admin.enter_report()                       # нажатие формирование отчета
        self.rrs_admin.spiner()                             # ожидание когда пропадёт спинер
        self.rrs_admin.scrol_down()                         # скролл вниз
        self.rrs_admin.make_screenshot("Screenshot")
        self.rrs_admin.export()                             # нажатие на экспорт
        self.rrs_admin.enter()                              # нажатие на enter

