import unittest

from calculate.json_function import load_data, data_recording, combined_data, load_data_for_id_user, delete_data_for_id_user

data_json = {
    "id_user": [
        {"id": 7581,
            "meaning": '10 + 50',
            "result": '60'}
    ]
}

data_json_big = {
    "id_user": [
        {"id": 6233,
            "meaning": '15 + 15',
            "result": '30'},
        {"id": 1665,
            "meaning": '15 + 15',
            "result": '30'},
        {"id": 6546,
            "meaning": '15 + 15',
            "result": '30'},
        {"id": 3959,
            "meaning": '15 + 15',
            "result": '30'},
        {"id": 4369,
            "meaning": '15 + 15',
            "result": '30'}
    ]
}

data_json1 = {
    "id_user": [
        {"id": 6855,
            "meaning": '103 + 102',
            "result": '205'}
    ]
}

data_json_with_id = {
    "369350471": [
        {"id": 7581,
            "meaning": '10 + 50',
            "result": '60'}
    ]
}

data_json_with_id_1 = {
    "369350471": [
        {"id": 9537,
            "meaning": '13 + 81',
            "result": '94'}
    ]
}

data_json_users_2 = {
      "369350478": [
            {"id": 61419,
              "meaning": 172,
              "result": 836.0},
            {"id": 6409,
              "meaning": "10 / 0",
              "result": "infinity"},
            {"id": 3075,
              "meaning": "15 + 15",
              "result": "30.0"},
            {"id": 2878,
              "meaning": "15 + 15",
              "result": "30.0"},
            {"id": 6965,
              "meaning": "15 + 15",
              "result": "30.0"}
      ],
      "198498415": [
            {"id": 6658,
              "meaning": "31 + 27",
              "result": "58.0"},
            {"id": 7427,
              "meaning": "142 + 440",
              "result": "582.0"},
            {"id": 9230,
              "meaning": "9 + 1 1",
              "result": "10.0"}
      ]
}

class test_json(unittest.TestCase):

    # Проверка на присутствия файла
    def test_write_and_read_file(self):
        # Создаем файл с данным
        data_recording(data_json)

        # Проверка наличия и сходимости
        self.assertEqual(
            load_data(),
            {'id_user': [{'id': 7581, 'result': '60', 'meaning': '10 + 50'}]}
        )

    # Проверка на добавлении json данных
    def test_append_json_in_json(self):
        # Создание файла с данными
        data_recording(data_json)

        # Изменение файла - добавление новых данных
        combined_data(data_json1)

        # Проверка наличия и сходимости
        self.assertEqual(
            load_data(),
            {'id_user': [
                {'id': 7581, 'result': '60', 'meaning': '10 + 50'},
                {'id': 6855, 'result': '205', 'meaning': '103 + 102'}
            ]})

    # Проверка на добавлении json данных с идентификатором пользователя
    def test_and_read_file_with_id(self):
        # Создание файла с данными
        data_recording(data_json_with_id)

        # Проверка наличия и сходимости
        self.assertEqual(
            load_data(),
            {'369350471': [{'id': 7581, 'result': '60', 'meaning': '10 + 50'}]}
        )

    # Проверка на добавлении json данных с идентификатором пользователя
    def test_append_json_in_json_with_id(self):
        # Создание файла с данными
        data_recording(data_json_with_id)

        # Изменение файла - добавление новых данных
        combined_data(data_json_with_id_1, str(369350471))

        # Проверка наличия и сходимости
        self.assertEqual(
            load_data(),
            {'369350471': [
                {'id': 7581, 'result': '60', 'meaning': '10 + 50'},
                {'id': 9537, 'result': '94', 'meaning': '13 + 81'}
            ]})
    #Проверка идентификатора поиска пользователя и получение информации
    def test_search_id_user_and_get_info(self):
        # Создание файл с данными
        data_recording(data_json_users_2)

        # Проверка наличия и сходимости
        self.assertEqual(
            load_data_for_id_user('198498415'),
            [{'id': 6658, 'result': '58.0', 'meaning': '31 + 27'},
             {'id': 7427, 'result': '582.0', 'meaning': '142 + 440'},
             {'id': 9230, 'result': '10.0', 'meaning': '9 + 1 1'},
             {'id': 9230, 'result': '10.0', 'meaning': '9 + 1 1'}])

    #Проверка удаления данных использования идентификатора
    def test_delete_data_of_id_user(self):
        # Создание файла с данными
        data_recording(data_json_users_2)

        # Удаление данные по id пользователя
        delete_data_for_id_user('369350478')

        # Проверка наличия и сходимости
        self.assertEqual(
            load_data_for_id_user('198498415'),
            'Ошибка! Такого идентификатора не существует.')