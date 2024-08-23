import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from configuration.ConfigProvider import ConfigProvider

class AdvancedSearch:

    def __init__(self, driver:WebDriver):
        self._url = ConfigProvider().get_ui_url()
        self._driver = driver
    
    @allure.step("Перейти на главную страницу")
    def go(self):
        self._driver.get(self._url)

    @allure.step("Открыть расширенный поиск")
    def open_advanced_search(self):
        self._driver.find_element(By.CSS_SELECTOR, 'a[aria-label="Расширенный поиск"]').click()

    @allure.step("Искать фильм по режиссеру {director} с указанием названия фильма {film_name}")
    def search_director_film(self, film_name: str, director: str):
        self._driver.find_element(By.CSS_SELECTOR, 'input[id="find_film"]').send_keys(film_name)
        self._driver.find_element(By.CSS_SELECTOR, 'input[name="m_act[cast]"]').send_keys(director)
        self._driver.find_element(By.CSS_SELECTOR, 'form[id="formSearchMain"]>input[value="поиск"]').click()

    @allure.step("Искать актёра {actor_name}")
    def search_actor(self, actor_name:str):
        self._driver.find_element(By.CSS_SELECTOR, 'input[id="find_people"]').send_keys(actor_name)
        WebDriverWait(self._driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'form[name="people_search"]>input[value="поиск"]')))
        self._driver.find_element(By.CSS_SELECTOR, 'form[name="people_search"]>input[value="поиск"]').click()

    @allure.step("Искать студию {studio_name}")
    def search_studio(self, studio_name:str):
        self._driver.find_element(By.CSS_SELECTOR, 'input[id="find_studio"]').send_keys(studio_name)
        WebDriverWait(self._driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'form[id="studio_search"]>input[value="поиск"]')))
        self._driver.find_element(By.CSS_SELECTOR, 'form[id="studio_search"]>input[value="поиск"]').click()
        
    @allure.step("Получить результат расширеного поиска студии")
    def get_studio(self) -> list[str]:
        all_elements = self._driver.find_elements(By.CSS_SELECTOR, 'td[class="news"]')
        elements_list = []
        for elem in all_elements:
            elements_list.append(elem.text)
        return elements_list

    @allure.step("Получить результат расширеного поиска")
    def get_advanced_results(self) -> list[str]:
        all_elements = self._driver.find_elements(By.CSS_SELECTOR, 'p[class="name"]>a[class="js-serp-metrika"]')
        elements_list = []
        for elem in all_elements:
            elements_list.append(elem.text)
        return elements_list
    
    @allure.step("Получить пустой результат поиска")
    def get_empty_result(self) -> str:
        result = self._driver.find_element(By.CSS_SELECTOR, 'h2[class="textorangebig"]').text
        return result