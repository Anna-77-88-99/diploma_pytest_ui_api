import allure
from api.KinopoiskApi import KinopoiskApi

@allure.id("KINOPOISKAPI-1")
@allure.epic("КИНОПОИСК API")
@allure.title("Получить список фильмов")
@allure.description("Получить список фильмов через GET запрос с использованием годов и возрастного рейтинга")
@allure.feature("READ")
@allure.severity("blocker")
def test_film_by_years_and_mpaa(api_client: KinopoiskApi, test_data: dict):
    result_api = api_client.get_films_by_years_and_mpaa(test_data.get("api_years"), test_data.get("api_mpaa"), test_data.get("api_type_movie"))
    with allure.step("Проверить данные, полученные в результате запроса"):
        assert result_api["docs"][0]["name"] == "Хвостатые пришельцы"
        assert result_api["docs"][0]["alternativeName"] == "Space Pups"
        assert result_api["docs"][0]["type"] == "movie"
        assert result_api["docs"][0]["year"] == 2023

@allure.id("KINOPOISKAPI-2")
@allure.epic("КИНОПОИСК API")
@allure.title("Получить список актеров")
@allure.description("Получить список актеров через GET запрос с использованием значений пола и места рождения")
@allure.feature("READ")
@allure.severity("blocker")
def test_actores_by_gender_and_place(api_client: KinopoiskApi):
    result_api = api_client.get_actores_by_geneder_and_place("Мужской", "Лос-Анджелес")
    with allure.step("Проверить данные, полученные в результате запроса"):
        assert result_api["docs"][1]["name"] == "Си Томас Хауэлл"
        assert result_api["docs"][1]["enName"] == "C. Thomas Howell"
        assert result_api["docs"][1]["sex"] == "Мужской"
        assert result_api["docs"][1]["age"] == 57

@allure.id("KINOPOISKAPI-3")
@allure.epic("КИНОПОИСК API")
@allure.title("Получить список студий-производителей")
@allure.description("Получить список студий-производителей через GET запрос по их названию")
@allure.feature("READ")
@allure.severity("blocker")
def test_studio_by_title(api_client: KinopoiskApi, test_data: dict):
    result_api = api_client.get_studio_by_title(test_data.get("api_studio"))
    with allure.step("Проверить данные, полученные в результате запроса"):
        assert result_api["docs"][0]["subType"] == "studio"
        assert result_api["docs"][0]["title"] == "Warner Bros."
        assert result_api["docs"][0]["type"] == "Производство"
        assert result_api["docs"][0]["createdAt"] == "2024-02-14T09:27:04.465Z"
        assert result_api["docs"][0]["updatedAt"] == "2024-08-07T15:44:54.113Z"

@allure.id("KINOPOISKAPI-4")
@allure.epic("КИНОПОИСК API")
@allure.title("Получить список фильмов по некорректным данным")
@allure.description("Через GET запрос отправить некорректные данные возрастного рейтинга")
@allure.feature("READ")
@allure.severity("blocker")
def test_wrong_mpaa(api_client: KinopoiskApi, test_data: dict):
    result_api = api_client.get_films_by_wrong_mpaa(test_data.get("api_wrong_mpaa"))
    with allure.step("Проверить сообщение об ошибке, полученное в результате использования некорректных данных"):
        assert result_api["message"][0] == "Поле ratingMpaa должно быть значением из списка: g, nc17, pg, pg13, r!"

@allure.id("KINOPOISKAPI-4")
@allure.epic("КИНОПОИСК API")
@allure.title("Получить список студий-производителей по некорректным данным")
@allure.description("Через GET запрос отправить некорректные данные типа студий-производителей")
@allure.feature("READ")
@allure.severity("blocker")
def test_wrong_studio_type(api_client: KinopoiskApi, test_data: dict):
    result_api = api_client.get_studio_by_wrong_type("Издатель", test_data.get("api_studio"))
    with allure.step("Проверить сообщение об ошибке, полученное в результате использования некорректных данных"):
        assert result_api["message"][0] == "Поле type должно быть значением из списка: Производство, Спецэффекты, Прокат, Студия дубляжа!"