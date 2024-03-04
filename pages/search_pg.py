import time
import allure
from base.base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC


class RrsSearchPage(BasePage):

    PAGE_URL = Links.SEARCH_PAGE

    SEARCH_BUTTON = ("xpath", "/html/body/table/tbody/tr[2]/td[1]/ul/li[2]/a")
    ENTER_SEARCH_1 = ("xpath", "/html/body/table/tbody/tr[2]/td[2]/form/table/tbody/tr[2]/td[10]/div/a")
    ENTER_SEARCH_2 = ("xpath", "/html/body/table/tbody/tr[2]/td[2]/form/table/tbody/tr[3]/td[10]/div/a")
    SEARCH = ("xpath", "/html/body/table/tbody/tr[1]/td[2]/ul/li[4]/a")
    CHECK = ("xpath", "/html/body/table/tbody/tr[2]/td[2]/form/table/tbody/tr[3]/td[1]/input")
    DELETE = ("xpath", "/html/body/table/tbody/tr[2]/td[2]/form/button[2]")
    DESIGN = ("xpath", "/html/body/table/tbody/tr[2]/td[2]/form/button[4]")
    DESIGN_OK = ("xpath", "/html/body/table/tbody/tr[2]/td[2]/form/input[3]")

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