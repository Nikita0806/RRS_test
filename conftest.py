import os

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope="function", autouse=True)          # autouse=True - она будет использоваться автоматически для всех тестов, scope="function" - создаёт браузер для каждого теста отдельно
def driver(request):                                    # Фикстура для инициализации наших тестов
    options = Options()                                 #
    service = Service(executable_path=ChromeDriverManager().install())          # для скачивания файлов
    prefs = {"download.default_directory": f"{os.getcwd()}\downloads"}          # путь к скачиванию файлов
    options.add_experimental_option("prefs", prefs)                             # для скачивания файлов
    options.add_argument("--headless")                  # для безголового режима для запуска в CI
    options.add_argument("--no-sandbox")                # доказательство, что это настоящий проект
    options.add_argument("--disable-dev-shm-usage")     #
    options.add_argument("--window-size=1920,1080")     # для размера окна
    driver = webdriver.Chrome(service=service, options=options)          # инициализация драйвера
    request.cls.driver = driver                         # создает объект драйвера в нутри наших тестов
    yield driver                                        # возращаю его
    driver.quit()                                       # закрываю
