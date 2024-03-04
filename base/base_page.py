import time
import allure
from allure_commons.types import AttachmentType         # для прикрепления файлов разного формата
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:                                                     # в нём мы будем инициализировать сам драйвер чтобы он был доступен на всех страницах
    def __init__(self, driver):                                     # инициализатор
        self.driver = driver                                        #
        self.wait = WebDriverWait(driver, 130, poll_frequency=1)     #

    def open(self):                                                 # помогает открывать страницы
        with allure.step(f"Open {self.PAGE_URL} page"):             # для записи в алюр более понятной
            self.driver.get(self.PAGE_URL)                          #
    time.sleep(2)

    def is_opened(self):                                            # открылась ли страница?
        with allure.step(f"Page {self.PAGE_URL} is opened"):        # для записи в алюр более понятной
            self.wait.until(EC.url_to_be(self.PAGE_URL))

    def scrol_down(self):                                                   # скролл вниз
        with allure.step(f"Scrol {self.PAGE_URL} page"):                    # для записи в алюр более понятной
            self.driver.execute_script("window.scrollBy(0,5000)","")
            # time.sleep(1)

    def scrol_up(self):                                                     # скролл вверх
        with allure.step(f"Scrol {self.PAGE_URL} page"):                    # для записи в алюр более понятной
            self.driver.execute_script("window.scrollBy(0,-5000)","")
            # time.sleep(1)

    def make_screenshot(self, screenshot_name):         # для скриншота
        allure.attach(                                  # как сохранять его
            body=self.driver.get_screenshot_as_png(),
            name=screenshot_name,
            attachment_type=AttachmentType.PNG
        )