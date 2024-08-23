import allure
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from api.KinopoiskApi import KinopoiskApi
from configuration.ConfigProvider import ConfigProvider
from testdata.DataProvider import DataProvider

@pytest.fixture
def browser():
    with allure.step("Открыть и настроить браузер"):
        browser_name = ConfigProvider().get("ui", "browser_name")
        if browser_name == 'chrome':
            browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        else:
            browser = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
        browser.implicitly_wait(ConfigProvider().get_ui_timeout())
        browser.maximize_window()
        yield browser
    with allure.step("Закрыть браузер"):
        browser.quit()

@pytest.fixture
def api_client() -> KinopoiskApi:
    with allure.step("Вернуть KinopoiskAPI с данными"):
        return KinopoiskApi(ConfigProvider().get_api_token(), ConfigProvider().get_api_url())

@pytest.fixture
def test_data():
    with allure.step("Вернуть тестовые данные JSON"):
        return DataProvider()