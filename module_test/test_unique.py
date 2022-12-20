#Подключение библиотеки unittest для тестирования
import unittest

from function.unique import Unique

#Создание класса тестирования unique
class test_unique(unittest.TestCase):
    #Проверка на значения
    def test_check_meaning(self):
        meaning = [1, 1, 2, 2, 2, 3, 3, 3, 4, 4]
        #Получение уникальных элементов числового типа
        mas_unique = Unique(meaning).arr
        #Проверка
        self.assertEqual(mas_unique, [1, 2, 3, 4])

    #Проверка на буквы
    def test_check_symbol(self):
        symbol = ['a', 'A', 'b', 'B', 'a', 'A', 'b', 'B']
        #Получение уникальных элементов символьного типа
        mas_unique = Unique(symbol).arr
        #Проверка
        self.assertEqual(mas_unique, ['a', 'A', 'b', 'B'])

    #Проверка на буквы без чувствительного регистра
    def test_check_symbol_sensitive_register(self):
        symbol = ['a', 'A', 'b', 'B', 'a', 'A', 'b', 'B']
        #Получение уникальных элементов символьного типа
        mas_unique = Unique(symbol, ignore_case = True).arr
        #Проверка
        self.assertEqual(mas_unique, ['a', 'b'])

    #Проверка на буквы со значениями (смещанный тип)
    def test_check_symbol_meaning(self):
        sym_men = ['a', 'A', 'b', 'B', '1', '1', '2', '2']
        #Получение уникальных элементов смещанного типа
        mas_unique = Unique(sym_men).arr
        #Проверка
        self.assertEqual(mas_unique, ['a', 'A', 'b', 'B', '1', '2'])

if __name__ == '__main__':
    unittest.main()