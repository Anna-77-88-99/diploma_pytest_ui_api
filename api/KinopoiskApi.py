import allure
import requests

class KinopoiskApi:

    def __init__(self, token: str, baseurl: str):
        self._baseurl = baseurl
        self._token = token

    @allure.step("с помощью данных {years}:{mpaa}:{type_str} получить список фильмов")
    def get_films_by_years_and_mpaa(self, years: str, mpaa: str, type_str:str):
        path = ("{url_value}/v1.4/movie?type={type_value}&year={years_value}&ratingMpaa={mpaa_value}".format(url_value = self._baseurl, type_value = type_str, years_value = years, mpaa_value = mpaa))
        headers_value = {"X-API-KEY":self._token}
        resp = requests.get(path, headers=headers_value)
        return resp.json()

    @allure.step("с помощью данных {gender}:{place} получить список актёров")
    def get_actores_by_geneder_and_place(self, gender: str, place: str):
        path = ("{url_value}/v1.4/person?birthPlace.value={place_value}&sex={gender_value}".format(url_value = self._baseurl, place_value = place, gender_value = gender))
        headers_value = {"X-API-KEY":self._token}
        resp = requests.get(path, headers=headers_value)
        return resp.json()
    
    @allure.step("с помощью {corp_title} получить список студий-производителей")
    def get_studio_by_title(self, corp_title: str):
        path = ("{url_value}/v1.4/studio?title={corp_value}".format(url_value = self._baseurl, corp_value = corp_title))
        headers_value = {"X-API-KEY":self._token}
        resp = requests.get(path, headers=headers_value)
        return resp.json()

    @allure.step("с помощью некорректного mpaa {mpaa} получить список фильмов")
    def get_films_by_wrong_mpaa(self, mpaa: str):
        path = ("{url_value}/v1.4/movie?ratingMpaa={mpaa_value}".format(url_value = self._baseurl, mpaa_value = mpaa))
        headers_value = {"X-API-KEY":self._token}
        resp = requests.get(path, headers=headers_value)
        return resp.json()
    
    @allure.step("с помощью некорректного значения {type_str} получить список фильмов")
    def get_studio_by_wrong_type(self, type_str: str, studio_name: str):
        path = ("{url_value}/v1.4/studio?type={type_value}&title={title_value}".format(url_value = self._baseurl, type_value = type_str, title_value = studio_name))
        headers_value = {"X-API-KEY":self._token}
        resp = requests.get(path, headers=headers_value)
        return resp.json()  