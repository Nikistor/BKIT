#Подключение библиотеки unittest для тестирования
import unittest

from function.filed import field, goods

#Создание класса тестирования filed
class test_filed(unittest.TestCase):
    # Проверка вывода с одним аргументом
    def test_check_output_one_argument(self):
        self.assertEqual(field(goods, 'title'),
            [
                {'title': 'Ковер'},
                {'title': 'Диван для отдыха'}
            ])

    # Проверка вывода с двумя аргументами
    def test_check_output_two_argument(self):
        self.assertEqual(field(goods, 'title color'),
            [
                {'color': 'green', 'title': 'Ковер'},
                {'color': 'black', 'title': 'Диван для отдыха'}
            ])

    # Проверка вывода с тремя аргументами
    def test_check_output_three_argument(self):
        self.assertEqual(field(goods, 'title color price'),
            [
                {'color': 'green', 'price': 2000, 'title': 'Ковер'},
                {'color': 'black', 'price': 5300, 'title': 'Диван для отдыха'}
            ])
