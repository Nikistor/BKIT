# Здесь должна быть реализация декоратора
'''
*args - неименованные аргументы (arguments), для которых важен порядок передачи.
Также используется название "позиционные аргументы".
**kwargs - именованные аргументы (keywords), для которых не важен порядок передачи.
Также используется название "аргументы, передаваемые по ключевым словам".
'''
# # Декоратор - это функция, ожидающая ДРУГУЮ функцию в качестве параметра.
# указываем имя декоратора и то, что он принимает function в качестве своей переменной.
def print_result(function):
    #объявление функции-обёртки realization(). Тело обёртки описывает, что именно мы будем делать с функцией, ранее принятой декоратором.
    def realization(mas=[], *args, **kwargs):
        # Печать название вызываемой функции
        print(function.__name__)
        if len(mas) == 0:
            result = function(*args, **kwargs)
        else:
            result = function(mas, *args, **kwargs)

        if type(result) == int or type(result) == str:
            print(result)
        # Если функция вернула список (list), то значения элементов списка должны выводиться в столбик.
        elif type(result) is list:
            print('\n'.join(map(str, result)))
        # Если функция вернула словарь (dict), то ключи и значения должны выводить в столбик через знак равенства.
        elif type(result) is dict:
            for key, meaning in result.items():
                print(f'{key} = {meaning}')
        # Функция zip создает итератор, который объединяет элементы из нескольких источников данных.
        elif type(result) == zip:
            for name, chislo in result:
                print(name, chislo)
        else:
            print(result)
        #функция result возвращает переменную
        return result
    #декоратор возвращает нам уже саму функцию realization, точнее, результат её работы над функцией function.
    return realization

# Синтаксис для обертывания функции в декоратор
@print_result
def test_1():
    return 1

# Синтаксис для обертывания функции в декоратор
@print_result
def test_2():
    return 'iu5'

# Синтаксис для обертывания функции в декоратор
@print_result
def test_3():
    return {'a': 1, 'b': 2}

# Синтаксис для обертывания функции в декоратор
@print_result
def test_4():
    return [1, 2]

# Синтаксис для обертывания функции в декоратор
def fun_print_result():
    test_1()
    test_2()
    test_3()
    test_4()