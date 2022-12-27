import json
# Сделаем другие необходимые импорты
from operator import concat
from filed import field
from unique import Unique
from sort import sort
from gen_random import gen_random
from cm_timer import cm_timer_1
from gen_random import gen_random
from print_result import print_result
# путь файла
path = '../data_light.json'

# Необходимо в переменную path сохранить путь к файлу, который был передан при запуске сценария

# Преобразуем в UTF-8 кодировку, иначе программа неправильно прочтет файл
with open(path, 'r', encoding='UTF-8') as f:
    data = json.load(f)
    # print(data)

# Далее необходимо реализовать все функции по заданию, заменив `raise NotImplemented`
# Предполагается, что функции f1, f2, f3 будут реализованы в одну строку
# В реализации функции f4 может быть до 3 строк

@print_result
def f1(arg):
    # Подборка названий работы, которые не совпадают друг друга в списке
    # info_name_work = Unique([i['name-work'] for i in field(data, 'name-work')], ignore_case=True)
    # Отсортируем
    # info_name_work_sorted = sorted(info_name_work, key=str, reverse = False)
    # return info_name_work.mas.sort()
    # return sorted(info_job_name, key=str, reverse = False)
    # return sorted(list(set([el['name-work'] for meaning in arg])), key=lambda a: a.lower())
    return list(Unique([i['job-name'] for i in field(data, 'job-name')], ignore_case=True))

@print_result
def f2(arg):
    # list() - создает или преобразует переданный объект в список.
    # filter() - применяет другую функцию к заданному итерируемому объекту (список, строка, словарь и так далее),
    # проверяя, нужно ли сохранить конкретный элемент или нет.
    # startswith() – начинается ли строка с определенного шаблона или нет.
    return list(filter(lambda i: i.startswith('программист'), arg))

@print_result
def f3(arg):
    # list() - создает или преобразует переданный объект в список.
    # map() — это функция, позволяющая обрабатывать и преобразовывать все элементы в итерируемом объекте без цикла for.
    # concat - сложение строк.
    return list(map(lambda x: concat(x, ' c опытом Python'), arg))

@print_result
def f4(arg):
    # list() - создает или преобразует переданный объект в список.
    # zip - создает итератор, который объединяет элементы из нескольких источников данных.
    return list(zip(arg, ['зарплата ' + str(meaning) + ' руб.' for meaning in gen_random(len(arg), 100000, 200000)]))

if __name__ == '__main__':
    with cm_timer_1():
        # ex_1 = f1(data)
        # ex_2 = f2(f1(data))
        # ex_3 = f3(f2(f1(data)))
        ex_4 = (f4(f3(f2(f1(data)))))
        print()