# 1. Отправить метод DELETE,  с помощью которого удалить 2-й и 4-й place_id из текстового файла, полученного в результате выполнения предыдущего задания DZ2_API_Google_maps.py (удалить значит не стереть, это значит что в файле по прежнему 5  значений, но 2-я и 4-я локация не существуют)
# 2. Отправить метод Get который будет читать place_id из текстового файла, и сделает отбор на существующие и несуществующие локации
# 3. Создать новый файл и поместить в него 3 существующих локации (place_id), которые были отобраны в результате метода GET


import requests

class Test_new_location():
    """Работа с новой локацией"""

    def test_delete_new_location(self):
        """Удаление второй и четвертой локации"""

        base_url = "https://rahulshettyacademy.com"
        key = "?key=qaclick123"

        delete_resource = "/maps/api/place/delete/json"

        delete_url = base_url + delete_resource + key
        print(delete_url)

        with open('doc/locations_1.txt') as loc_file:
            loc_list = loc_file.read().splitlines()
        for loc_id_del in loc_list[1], loc_list[3]:

            json_for_delete_new_location = {
                "place_id": loc_id_del
            }
            result_delete = requests.delete(delete_url, json = json_for_delete_new_location)
            print(result_delete.text)
            print("Статус код: " + str(result_delete.status_code))
            assert 200 == result_delete.status_code
            print("Успешно!! Удаление новой локации прошло успешно!!!")
            check_status = result_delete.json()
            check_status_info = check_status.get("status")
            print("Статус: " + str(check_status_info))
            assert check_status_info == "OK"
            print("Удаление локации с ID " + loc_id_del + " прошло успешно")


        """Проверка удаленных и оставшихся локаций локаций"""
        counter_exists = 0
        counter_deleted = 0
        with open('doc/locations_1.txt') as loc_file:
            loc_list = loc_file.read().splitlines()
        for loc_id in loc_list:
            get_resource = "/maps/api/place/get/json"
            get_url = base_url + get_resource + key + "&place_id=" + loc_id
            print(get_url)
            result_get = requests.get(get_url)
            print(result_get.text)
            try:
                assert 200 == result_get.status_code
                print("Статус код: " + str(result_get.status_code))
                print("Проверка успешна. Локация с ID " + loc_id + " существует в базе")
                loc_2 = open('doc/locations_2.txt', 'a')
                loc_2.write(loc_id + "\n")
                loc_2.close()
                counter_exists = int(counter_exists) + 1
            except:
                assert 404 == result_get.status_code
                print("Статус код: " + str(result_get.status_code))
                print("Проверка успешна. Локация с ID " + loc_id + " удалена из базы")
                counter_deleted = int(counter_deleted) + 1
        print("Успешно!! Существующих локаций в списке: " + str(counter_exists) + ", удалено локаций: " + str(counter_deleted))

new_place = Test_new_location()
new_place.test_delete_new_location()