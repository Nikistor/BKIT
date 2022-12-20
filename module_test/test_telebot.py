import unittest
import os.path

file_locator = 'D:\Работа\МГТУ им. Н.Э.Баумана\Программирование\Программы\Программы за 5 семестр\DZ\calculate'

from calculate.work_calculate import generator_of_meaning, get_info_id_user, data_recording

data_json_users_2 = {
    "745896123": [
        {"id": 61419,
         "meaning": 172,
         "result": 836.0},
        {"id": 3075,
         "meaning": "15 + 15",
         "result": "30.0"},
        {"id": 2878,
         "meaning": "15 + 15",
         "result": "30.0"},
        {"id": 6965,
         "meaning": "15 + 15",
         "result": "30.0"},
        {"id": 6409,
         "meaning": "10 / 0",
         "result": "infinity"},
    ],
    "965478145": [
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

class test_telebot(unittest.TestCase):

    # Проверка создания файла
    def test_create_file(self):
        message_from_user_id = 745896123

        generator_of_meaning(str(message_from_user_id))

        self.assertEqual(
            os.path.exists(file_locator + '\data.json'),
            True
        )

    # Проверка на получение информации по id пользователя
    def test_get_info_id_user(self):
        data_recording(data_json_users_2)

        message_from_user_id = 745896123

        check_info = get_info_id_user(str(message_from_user_id))
        print(check_info)
        self.assertEqual(
            check_info, [{'id': 61419, 'meaning': 172, 'result': 836.0},
                         {'id': 3075, 'meaning': '15 + 15', 'result': '30.0'},
                         {'id': 2878, 'meaning': '15 + 15', 'result': '30.0'},
                         {'id': 6965, 'meaning': '15 + 15', 'result': '30.0'},
                         {'id': 6409, 'meaning': '10 / 0', 'result': 'infinity'},
                         {'id': 6409, 'meaning': '10 / 0', 'result': 'infinity'}]
        )
