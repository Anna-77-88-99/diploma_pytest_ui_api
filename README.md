# diploma_pytest_ui_api

## Дипломная работа. Архитектура фреймворка

### Стек:
- pytest
- webdriver-manager
- selenium
- requests
- allure
- configparser
- json

### Шаги:
1. Склонировать проект 'git clone https://github.com/Anna-77-88-99/diploma_pytest_ui_api.git'
2. Установить все зависимости `pip install -r requirements.txt`
3. Запустить тесты `python -m pytest`
4. Сгенерировать отчет `allure generate allure-files -o allure-report`
5. Открыть отчет `allure open allure-report`

### Структура:
- ./test - тесты
- ./pages - описание страниц
- ./api - для работы с API
- ./configuration - провайдер настроек
    - test_config.ini - настройки для тестов
- ./testdata - провайдер тестовых данных
    - test_data.json

### Библиотеки:
pip install pytest
pip install webdriver-manager
pip install selenium
pip install requests
pip install allure

### Полезные ссылки:
- [Подсказка по markdown] (https://www.markdownguide.org/cheat-sheet/)
- [Генератор .gitignore] (https://www.toptal.com/developers/gitignore)
- [Подсказка по pytest] (https://docs.pytest.org/en/stable/)
- [Подсказка по webdriver-manager] (https://pypi.org/project/webdriver-manager/)
- [Подсказка по Selenium] (https://www.selenium.dev/documentation/)
- [Подсказка по Requests] (https://requests.readthedocs.io/en/latest/index.html)
- [Подсказка по Allure Report] (https://allurereport.org/docs/) 
