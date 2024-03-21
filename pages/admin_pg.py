import os
import time
import allure
import keyboard as keyboard
from selenium.webdriver.chrome import webdriver
from selenium.webdriver.common.by import By
from base.base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class RrsAdminPage(BasePage):

    PAGE_URL = Links.ADMIN_PAGE

    USERNAME_FIELD = ("name", "username")
    PASSWORD_FIELD = ("id", "id_password")
    SUBMIT_BUTTON = ("class name", "submit-row")
    DROP_DOWN_LIST = ("css selector", "#navigation-menu > li:nth-child(4) > a")
    REPORTS = ("css selector", "#navigation-menu > li:nth-child(4) > ul > li:nth-child(2) > a")
    SUPPLIERS_REPORT = ("css selector", "#module_1 > div > ul > li:nth-child(2) > a")
    ADD_REPORT = ("class name", "addlink")
    DATA_INPUT_1 = ("name", "start_interval_0")
    TIME_ENTER_START = ("css selector", "#supplierstatsmview_form > div > fieldset > div.form-row.field-start_interval > div > p > span:nth-child(5) > a:nth-child(1)")
    DATA_INPUT_29 = ("id", "id_end_interval_0")
    TIME_ENTER_AND = ("css selector", "#supplierstatsmview_form > div > fieldset > div.form-row.field-end_interval > div > p > span:nth-child(5) > a:nth-child(1)")
    SUPPLIERS_ALL = ("id", "id_supplier_add_all_link")
    ENTER_SUPPLIERS_ONE = ("xpath", "/html/body/div[1]/div[3]/div/div[1]/div/form/div/fieldset/div[3]/div/div/ul/li[1]/a")
    ENTER_REPORT = ("id", "btn_formation")
    EXPORT = ("id", "btn_export_to_excel")
    SPINER = ("xpath", "/html/body/div[1]/div[3]/div/div[1]/div/form/div/div[1]/h2")
    SPINER1 = ("xpath", "/html/body/div[1]/div[3]/div/div[1]/div/form/div/section")
    BODY = ("xpath", "/html/body")


    @allure.step("Enter login")
    def enter_login(self, login):
        self.wait.until(EC.element_to_be_clickable(self.USERNAME_FIELD)).send_keys(login)
        # time.sleep(2)

    @allure.step("Enter password")
    def enter_password(self, password):
        self.wait.until(EC.element_to_be_clickable(self.PASSWORD_FIELD)).send_keys(password)
        # time.sleep(2)

    @allure.step("Click on submit button")
    def click_submit_button(self):
        self.wait.until(EC.element_to_be_clickable(self.SUBMIT_BUTTON)).click()
        # time.sleep(1)

    @allure.step("Drop down list")
    def drop_down_list(self):
        self.wait.until(EC.element_to_be_clickable(self.DROP_DOWN_LIST)).click()
        # time.sleep(1)

    @allure.step("Reports")
    def report(self):
        self.wait.until(EC.element_to_be_clickable(self.REPORTS)).click()
        # time.sleep(1)

    @allure.step("Suppliers report")
    def suppliers_report(self):
        self.wait.until(EC.element_to_be_clickable(self.SUPPLIERS_REPORT)).click()
        # time.sleep(1)

    @allure.step("Add report")
    def add_report(self):
        self.wait.until(EC.element_to_be_clickable(self.ADD_REPORT)).click()
        # time.sleep(1)

    @allure.step("Data input start")
    def data_input_start(self, data_start):
        self.wait.until(EC.element_to_be_clickable(self.DATA_INPUT_1)).send_keys(data_start)
        # time.sleep(1)

    @allure.step("Timer enter start")
    def timer_enter_start(self):
        self.wait.until(EC.element_to_be_clickable(self.TIME_ENTER_START)).click()
        # time.sleep(1)

    @allure.step("Data input end")
    def data_input_end(self, data_and):
        self.wait.until(EC.element_to_be_clickable(self.DATA_INPUT_29)).send_keys(data_and)
        # time.sleep(1)

    @allure.step("Timer enter end")
    def timer_enter_and(self):
        self.wait.until(EC.element_to_be_clickable(self.TIME_ENTER_AND)).click()
        # time.sleep(1)

    @allure.step("Suppliers all")
    def suppliers_all(self):
        self.wait.until(EC.element_to_be_clickable(self.SUPPLIERS_ALL)).click()
        # time.sleep(1)

    @allure.step("Enter report")
    def enter_report(self):
        self.wait.until(EC.element_to_be_clickable(self.ENTER_REPORT)).click()
        # time.sleep(15)

    @allure.step("Spiner")
    def spiner(self):
        self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, "table-report")))    # Ожидание таблицы
        # time.sleep(3)

    @allure.step("Export report")
    def export(self):
        self.wait.until(EC.element_to_be_clickable(self.EXPORT)).click()
        # time.sleep(1)

    # @allure.step("Click enter")
    # def enter(self):
    #     self.wait.until(EC.presence_of_element_located(self.BODY)).send_keys(Keys.ENTER)
    #     # time.sleep(1)

    # keyboard.press('enter')       # вводим клавишу Enter
    # keyboard.release('enter')     # выходим из ввода клавишу Enter

    # @allure.step("Click enter")
    # def enter(self):
    #     keyboard.press('enter')
    #     keyboard.release('enter')
    #     time.sleep(10)


    # @allure.step("Click on submit button")
    # def enter_2(self):
    #     # отправка клавиши Enter в любом месте на странице
    #     actions = ActionChains(self.driver)
    #     actions.send_keys(Keys.ENTER)
    #     actions.perform()
    #
    #     # закрытие драйвера
    #     self.driver.quit()

