# 1.Отправить запрос для получения всех категорий
# 2.Получить 1 шутку по каждой из категорий (16 шт) - всего 16 шуток

import json
import requests

class Test_new_joke():
    """Создание новой шутки"""

    def test_get_categories(self):
        """Получение списка категорий"""
        url = "https://api.chucknorris.io/jokes/categories"
        print(url)
        global result
        result = requests.get(url)
        print("Статус код: " + str(result.status_code))
        assert 200 == result.status_code
        print("Успешно!!! Мы получили список категорий")
        result.encoding = "utf-8"
        print(result.text)

    def test_get_joke_by_category(self):
        """Получение шуток по категориям"""
        category_list = json.loads(result.text)
        joke_count = 0
        for j in category_list:
            url = "https://api.chucknorris.io/jokes/random?category=" + str(j)
            print(url)
            result_joke = requests.get(url)
            print("Статус код: " + str(result_joke.status_code))
            assert 200 == result_joke.status_code
            result_joke.encoding = "utf-8"
            # print(result_joke.text)
            check = result_joke.json()
            check_info = check.get("categories")
            # print(check_info)
            assert check_info == [j]
            print("Категория " + j + " верна")
            print("Успешно!!! Мы получили шутку из категории " + j)
            check_info_value = check.get("value")
            print(check_info_value)
            name = "Chuck"
            assert name in check_info_value
            print("Chuck присутствует в шутке")
            joke_count = joke_count + 1
        print("Всего шуток получилось " + str(joke_count))


categories_get = Test_new_joke()
categories_get.test_get_categories()
category_joke = Test_new_joke()
category_joke.test_get_joke_by_category()