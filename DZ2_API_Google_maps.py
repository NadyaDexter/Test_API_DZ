# 1. Отправить метод POST на создание 5 новых локаций
# 2. Создать текстовый файл в котором хранить 5 шт place_id полученных из 1 пункта (не писать портянку вызывая 5 раз метод, сделать красиво)
# 3. Отправить метод Get который будет читать place_id из текстового файла (из него, не их переменной первого запроса) и убедиться что данные place_id существуют


import requests

class Test_new_location():
    """Работа с новой локацией"""

    def test_create_new_location(self):
        """Создание пяти новых локаций"""

        base_url = "https://rahulshettyacademy.com" # Базовая url
        key = "?key=qaclick123"                     # Параметр для всех запросов

        post_resource = "/maps/api/place/add/json"  # Ресурс метода POST

        post_url = base_url + post_resource + key
        print(post_url)

        json_for_create_new_location = {
            "location": {
                "lat": -38.383494,
                "lng": 33.427362
            }, "accuracy": 50,
            "name": "Frontline house",
            "phone_number": "(+91) 983 893 3937",
            "address": "29, side layout, cohen 09",
            "types": [
                "shoe park",
                "shop"
            ],
            "website": "http://google.com",
            "language": "French-IN"
        }
        loc_count = sum(1 for line in open('doc/locations_1.txt', 'r'))
        while loc_count < 5:
            result_post = requests.post(post_url, json=json_for_create_new_location)
            print(result_post.text)
            assert 200 == result_post.status_code
            print("Успешно!!! Создана новая локация")
            print("Статус код: " + str(result_post.status_code))
            check_post = result_post.json()
            check_info_post = check_post.get("status")
            print("Статус код ответа: " + check_info_post)
            assert check_info_post == "OK"
            print("Статус код ответа верен")
            place_id = check_post.get("place_id")
            print("ID локации: " + place_id)
            loc = open('doc/locations_1.txt', 'a')
            loc.write(place_id + "\n")
            loc.close()
            loc_count = sum(1 for line in open('doc/locations_1.txt', 'r'))
            print(loc_count)
        else:
            print("Создание пяти локаций завершено")

        """Проверка созданных локаций"""

        with open('doc/locations_1.txt') as loc_file:
            loc_list = loc_file.read().splitlines()
        for loc_id in loc_list:
            get_resource = "/maps/api/place/get/json"
            get_url = base_url + get_resource + key + "&place_id=" + loc_id
            print(get_url)
            result_get = requests.get(get_url)
            print(result_get.text)
            assert 200 == result_get.status_code
            print("Статус код: " + str(result_get.status_code))
            print("Проверка новой локации успешна!!!")
        print("Проверка пяти созданных локаций завершена")


new_place = Test_new_location()
new_place.test_create_new_location()