# 1. Открыть ссылку https://swapi.dev/
# 2. Отправить метод GET https://swapi.dev/api/people/4/
# 3. Написать код который будет сохранять всех персонажей (имена), которые снимались в фильмах с Дарт Вейдером, в тестовый файл, при этом в файле не должны содержаться дубли


import requests

class Characters_list():
    """Работа со списками фильмов и персонажей"""

    def test_get_characters_list(self):

        """Поиск всех фильмов с Дартом Вейдером"""

        base_url = "https://swapi.dev/api/"
        get_darth_vader_resource = "people/4/"
        vader_url = base_url + get_darth_vader_resource
        print(vader_url)
        result_vader = requests.get(vader_url)
        check_films = result_vader.json()
        check_info_films = list(check_films.get("films"))
        print("Список ссылок на фильмы готов: " + '\n' + str(check_info_films))


        """Поиск всех персонажей в фильмах с Дартом Вейдером"""

        for film in check_info_films:
            film_url = film
            result_film = requests.get(film_url)
            check_characters = result_film.json()
            characters_links = open('doc/characters.txt', 'r')
            characters_links_sort = characters_links.read().splitlines()
            check_characters_info = list(check_characters.get('characters'))
            links_number = len(characters_links_sort)


            """Отбор тех персонажей, которые присутствовали во всех фильмах с Дартом Вейдером"""
            try:
                assert links_number > 0
                characters_links_write = open('doc/characters.txt', 'w')
                friends_list = set(characters_links_sort).intersection(check_characters_info)
                characters_links_write.write('\n'.join(friends_list))
                characters_links_write.close()
                characters_links.close()

            except:
                characters_links_write = open('doc/characters.txt', 'w')
                characters_links_write.write('\n'.join(check_characters_info))
                characters_links_write.close()
                characters_links.close()

        else:
            characters_links = open('doc/characters.txt', 'r')
            characters_links_sort = characters_links.read().splitlines()
            print("Список ссылок на персонажей готов: " + '\n' + str(characters_links_sort))

        """Поиск имен персонажей по списку ссылок"""
        for char_link in characters_links_sort:
            if char_link != vader_url:
                get_url = char_link
                result_char = requests.get(get_url)
                check_char = result_char.json()
                check_char_info = check_char.get("name")
                characters_write = open('doc/names.txt', 'a')
                characters_write.write(check_char_info + '\n')
                characters_write.close()
        else:
            characters_names = open('doc/names.txt', 'r')
            characters_names_sort = characters_names.read().splitlines()
            print("Список имен персонажей готов!! Вместе с Дартом Вейдером во всех фильмах присутствовали: " + '\n' + '\n'.join(sorted(characters_names_sort)))

vader_and_friends = Characters_list()
vader_and_friends.test_get_characters_list()