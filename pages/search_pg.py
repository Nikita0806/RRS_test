import time
import allure
from base.base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC


class RrsSearchPage(BasePage):

    PAGE_URL = Links.SEARCH_PAGE

    SEARCH_BUTTON = ("css selector", "#sidebar > ul > li:nth-child(2) > a")
    ENTER_SEARCH_1 = ("css selector", "#content > form > table > tbody > tr:nth-child(2) > td.basket_add > div > a")
    ENTER_SEARCH_2 = ("css selector", "#content > form > table > tbody > tr:nth-child(3) > td.basket_add > div > a")
    SEARCH = ("css selector", "#header > ul > li:nth-child(4) > a")
    CHECK = ("name", "delete-948507790")
    DELETE = ("css selector", "#content > form > button:nth-child(4)")
    DESIGN = ("css selector", "#content > form > button:nth-child(6)")
    DESIGN_OK = ("css selector", "#content > form > input.button")

    @allure.step("search button")
    def search_button(self):
        self.wait.until(EC.element_to_be_clickable(self.SEARCH_BUTTON)).click()
        # time.sleep(1)

    @allure.step("enter search 1 button")
    def enter_search_1(self):
        self.wait.until(EC.element_to_be_clickable(self.ENTER_SEARCH_1)).click()
        # time.sleep(1)

    @allure.step("enter search 1 button")
    def enter_search_2(self):
        self.wait.until(EC.element_to_be_clickable(self.ENTER_SEARCH_2)).click()
        # time.sleep(1)

    @allure.step("search")
    def search(self):
        self.wait.until(EC.element_to_be_clickable(self.SEARCH)).click()
        # time.sleep(1)

    @allure.step("check box in search")
    def check(self):
        self.wait.until(EC.element_to_be_clickable(self.CHECK)).click()
        # time.sleep(1)

    @allure.step("delete position in search")
    def delete(self):
        self.wait.until(EC.element_to_be_clickable(self.DELETE)).click()
        # time.sleep(1)

    @allure.step("design")
    def design(self):
        self.wait.until(EC.element_to_be_clickable(self.DESIGN)).click()
        # time.sleep(1)

    @allure.step("design true")
    def design_ok(self):
        self.wait.until(EC.element_to_be_clickable(self.DESIGN_OK)).click()
        # time.sleep(1)
