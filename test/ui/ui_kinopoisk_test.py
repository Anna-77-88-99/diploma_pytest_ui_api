import allure
from selenium import webdriver
from pages.MainSearch import MainSearch
from pages.AdvancedSearch import AdvancedSearch

@allure.id("KINOPOISKUI-1")
@allure.epic("КИНОПОИСК UI")
@allure.title("Стандартный поиск")
@allure.description("Искать фильм через стандартный поиск")
@allure.feature("READ")
@allure.severity("blocker")
def test_main_search(browser):
    search = MainSearch(browser)
    search.go()
    search.main_search_data("Появляется Данстон")
    result_search = search.get_result_name()
    with allure.step("Проверить, что указаный фильм совпадает с результатом поиска"):
        assert result_search == "Появляется Данстон (1996)"

@allure.id("KINOPOISKUI-2")
@allure.epic("КИНОПОИСК UI")
@allure.title("Расширенный поиск по режиссеру")
@allure.description("Искать фильм через расширенный поиск по режиссеру")
@allure.feature("READ")
@allure.severity("blocker")
def test_find_film_by_director(browser):
    search = AdvancedSearch(browser)
    search.go()
    search.open_advanced_search()
    search.search_director_film("Тайная жизнь домашних животных", "Крис Рено")
    result_search = search.get_advanced_results()
    with allure.step("Проверить, что указаный фильм совпадает с результатом поиска согласно MPAA"):
        assert result_search[1] == "Тайная жизнь домашних животных" 

@allure.id("KINOPOISKUI-3")
@allure.epic("КИНОПОИСК UI")
@allure.title("Расширенный поиск по актерам")
@allure.description("Искать актёра по имени и фамилии")
@allure.feature("READ")
@allure.severity("blocker")
def test_find_actor(browser):
    search = AdvancedSearch(browser)
    search.go()
    search.open_advanced_search()
    search.search_actor("Лесли Нильсен")
    result_search = search.get_advanced_results()
    with allure.step("Проверить, что указаный актёр совпадает с результатом поиска"):
        assert result_search[0] == "Лесли Нильсен"

@allure.id("KINOPOISKUI-4")
@allure.epic("КИНОПОИСК UI")
@allure.title("Расширенный поиск студий")
@allure.description("Искать студию по её названию")
@allure.feature("READ")
@allure.severity("blocker")
def test_find_studio(browser, test_data: dict):
    search = AdvancedSearch(browser)
    search.go()
    search.open_advanced_search()
    search.search_studio(test_data.get("ui_studio_name"))
    result_search = search.get_studio()
    with allure.step("Проверить, что указаная студия совпадает с результатом поиска"):
        assert result_search[0] == test_data.get("ui_studio_result")

@allure.id("KINOPOISKUI-5")
@allure.epic("КИНОПОИСК UI")
@allure.title("Расширенный поиск по режиссеру и несуществующему названию")
@allure.description("Получить результаты поиска если название фильма не является корректным")
@allure.feature("READ")
@allure.severity("blocker")
def test_empty_result(browser, test_data: dict):
    search = AdvancedSearch(browser)
    search.go()
    search.open_advanced_search()
    search.search_director_film(test_data.get("wrong_film_title"), "Крис Рено")
    result_search = search.get_empty_result()
    with allure.step("Проверить, что в случае неправильного названия фмльма получим пустой результат поиска"):
        assert result_search == "К сожалению, по вашему запросу ничего не найдено..." 
