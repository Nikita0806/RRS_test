import time
import allure
from base.base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC


class RrsLoginPage(BasePage):

    PAGE_URL = Links.HOST

    INVOICES_AND_ORDERS = ("css selector", "#header > ul > li:nth-child(5) > a")
    USERNAME_FIELD = ("xpath", "/html/body/table/tbody/tr[2]/td[2]/form/fieldset/div[1]/div/input")
    PASSWORD_FIELD = ("xpath", "/html/body/table/tbody/tr[2]/td[2]/form/fieldset/div[2]/div/input")
    SUBMIT_BUTTON = ("css selector", "#content > form > input")
    CLOSE_OFFER = ("css selector", "#weekdays-modal > div > a")

    @allure.step("Invoices and orders")
    def invoices_and_orders(self):
        self.wait.until(EC.element_to_be_clickable(self.INVOICES_AND_ORDERS)).click()
        # time.sleep(2)

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
        # time.sleep(2)

    @allure.step("Close offer")
    def close_offer(self):
        self.wait.until(EC.element_to_be_clickable(self.CLOSE_OFFER)).click()
        # time.sleep(2)
