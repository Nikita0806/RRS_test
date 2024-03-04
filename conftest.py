import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

@pytest.fixture(scope="function",autouse=True)          # autouse=True - она будет использоваться автоматически для всех тестов, scope="function" - создаёт браузер для каждого теста отдельно
def driver(request):                                    # Фикстура для инициализации наших тестов
    options = Options()                                 #
    # options.add_argument("--headless")                  # для безголового режима для запуска в CI
    options.add_argument("--no-sandbox")                # доказательство, что это настоящий проект
    options.add_argument("--disable-dev-shm-usage")     #
    options.add_argument("--window-size=1920,1080")     # для размера окна
    driver = webdriver.Chrome(options=options)          # инициализация драйвера
    request.cls.driver = driver                         # создает объект драйвера в нутри наших тестов
    yield driver                                        # возращаю его
    driver.quit()                                       # закрываю
