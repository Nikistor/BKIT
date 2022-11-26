# Подключаем библиотеку unitetest для тестирования
import unittest
import math

'''
assertEqual(self, first, second)
first - передаваемое значение
second - полученное значение (в тело функции должен быть return, если вы там не оставили, тогда прописать здесь как None)
если передаваемое значение совпадает с полученным значением, то тест пройден успешно
'''

# Вычисление корня
from function.get_roots import get_roots

# Тест на сумму
class test_get_roots(unittest.TestCase):
    # https://tutomath.ru/baza-znanij/bikvadratnye-uravneniya.html
    # Пример №1
    # Дискриминат больше 0 и 4 корней
    def test_example_1(self):
        self.assertEqual(
            get_roots(1, -5, 6), [math.sqrt(3), -math.sqrt(3), math.sqrt(2), -math.sqrt(2)]
        )

    # Пример №2
    # Дискриминат равен 0 и 2 корня
    def test_example_2(self):
        self.assertEqual(
            get_roots(1, -4, 4), [math.sqrt(2), -math.sqrt(2)]
        )

    # Пример №3
    # Дискриминат больше 0 и 3 корней
    def test_example_3(self):
        self.assertEqual(
            get_roots(-4, 16, 0), [0, 2, -2]
        )

    # Пример №4
    # Дискриминат равен 0 и 2 корней
    def test_example_4(self):
        self.assertEqual(
            get_roots(1, 0, -16), [2.0, -2.0]
        )

    # Пример №5
    # Дискриминат равен 0 и нет корней
    def test_example_5(self):
        self.assertEqual(
            get_roots(1, 0, 10), []
        )

    # Пример №6
    # Дискриминат больше 0 и 2 корня
    def test_example_6(self):
        self.assertEqual(
            get_roots(1, -5, -36), [3, -3]
        )

    # Пример №7
    # Дискриминат больше 0 и 4 корней
    def test_example_7(self):
        self.assertEqual(
            get_roots(1, -5, 4), [2.0, -2.0, 1.0, -1.0]
        )


# Получение коэффициента с комадной строки или ввода
from function.get_coef_test import get_coef_test_no_cmd, get_coef_test_with_cmd

class test_get_coef_no_cmd(unittest.TestCase):
    # Без командной строки

    # Тест на обычное числа
    def test_value_index_1(self):
        self.assertEqual(
            get_coef_test_no_cmd(1, 1), 1.0
        )

    # Тест на нулевое числа
    def test_value_index_2(self):
        self.assertEqual(
            get_coef_test_no_cmd(2, 0), 0.0
        )

    # Тест на обычное числа
    def test_value_index_3(self):
        self.assertEqual(
            get_coef_test_no_cmd(3, 5), 5.0
        )

    # Тест на индекс
    def test_value_index_4(self):
        self.assertEqual(
            get_coef_test_no_cmd(4, 7), None
        )

    # Тест на индекс
    def test_value_index_0(self):
        self.assertEqual(
            get_coef_test_no_cmd(0, 7), None
        )

    # Тест на отрицательное число
    def test_value_index_negative_sign(self):
        self.assertEqual(
            get_coef_test_no_cmd(3, -5), -5.0
        )

    # Тест на другие символ
    def test_value_other_char(self):
        self.assertEqual(
            get_coef_test_no_cmd(3, 'a'), None
        )

    # Тест на другие символ
    def test_value_other_char_and_negative_sign(self):
        self.assertEqual(
            get_coef_test_no_cmd(3, '-a'), None
        )

class test_get_coef_with_cmd(unittest.TestCase):
    # С командной строки

    # Тест на обычное числа
    def test_value_index_1(self):
        self.assertEqual(
            get_coef_test_with_cmd(1, 1), 1.0
        )

    # Тест на нулевое числа
    def test_value_index_2(self):
        self.assertEqual(
            get_coef_test_with_cmd(2, 0), 0.0
        )

    # Тест на обычное числа
    def test_value_index_3(self):
        self.assertEqual(
            get_coef_test_with_cmd(3, 5), 5.0
        )

    # Тест на индекс
    def test_value_index_4(self):
        self.assertEqual(
            get_coef_test_with_cmd(4, 7), None
        )

    # Тест на индекс
    def test_value_index_0(self):
        self.assertEqual(
            get_coef_test_with_cmd(0, 7), None
        )

    # Тест на отрицательное число
    def test_value_negative_sign(self):
        self.assertEqual(
            get_coef_test_with_cmd(3, -5), -5.0
        )

    # Тест на другие символ
    def test_value_other_char(self):
        self.assertEqual(
            get_coef_test_with_cmd(3, 'a'), None
        )

    # Тест на другие символ
    def test_value_other_char_and_negative_sign(self):
        self.assertEqual(
            get_coef_test_with_cmd(3, '-a'), None
        )

if __name__ == '__main__':
    unittest.main()