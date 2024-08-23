import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from configuration.ConfigProvider import ConfigProvider

class MainSearch:

    def __init__(self, driver:WebDriver):
        self._url = ConfigProvider().get_ui_url()
        self._driver = driver
    
    @allure.step("Перейти на главную страницу")
    def go(self):
        self._driver.get(self._url)
    
    @allure.step("Передать название фильма {film_name} и нажать поиск")
    def main_search_data(self, film_name:str):
        self._driver.find_element(By.CSS_SELECTOR, 'input[name="kp_query"]').send_keys(film_name)
        self._driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()

    @allure.step("Получить результаты обычного поиска")
    def get_result_name(self) -> str:
        WebDriverWait(self._driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'h1[itemprop="name"]>span')))
        result_name = self._driver.find_element(By.CSS_SELECTOR, 'h1[itemprop="name"]').text
        return result_name