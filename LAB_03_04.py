import sys
from lab_python_fp.filed import *
from lab_python_fp.gen_random import *
from lab_python_fp.unique import *
from lab_python_fp.sort import *
from lab_python_fp.print_result import *
from lab_python_fp.cm_timer import *
# from lab_python_fp.process_data import *

def get_argv(index, prompt):
    try:
        # Получение значения из командной строки
        coef_str = sys.argv[index]
        print(index + 1, prompt, coef_str)
    except:
        # Вводим с клавиатуры
        print(index + 1, prompt, end='')
        coef_str = input()
    # По умолчанию строки
    return coef_str

def get_argv_value(index, prompt):
    try:
        # Получение значения из командной строки
        coef_str = sys.argv[index]
    except:
        # Вводим с клавиатуры
        print(prompt, end='')
        coef_str = input()
    # Переводим строку в целое число
    coef = int(coef_str)
    return coef

def into_tuple_from_str_in_value(str):
    tuple_buff = []
    str_buff = ''
    for i in range(len(str)):
        if (str[i] == ' '):
            tuple_buff.append(int(str_buff))
            str_buff = ''
        else:
            str_buff += str[i]

    tuple_buff.append(int(str_buff))

    return tuple_buff

def main():
    print('МЕНЮ')
    print('1. Задача 1 (файл field.py)')
    print('2. Задача 2 (файл gen_random.py)')
    print('3. Задача 3 (файл unique.py)')
    print('4. Задача 4 (файл sort.py)')
    print('5. Задача 5 (файл print_result.py)')
    print('6. Задача 6 (файл cm_timer.py)')
    # print('7. Задача 7 (файл process_data.py)')
    # Переключатель
    # switch = int(input('Введите номер пункта: '))
    switch = get_argv_value(1, 'Введите номер пункта: ')

    if(switch == 1):
        print('Задача 1 (файл field.py)')
        mas = ''
        if(len(sys.argv)==1):
            count_argv = int(input('Введите количество аргументов: '))
            if(count_argv > 1):
                for i in range(0, count_argv):
                    # print('{}-ый аргумент'.format(i + 1))
                    mas += (get_argv(i, '-ый аргумент: '))
                    # print('{}-ый аргумент: {}'.format(i + 1, mas[i]))
                    mas += ' '
                print(field(goods, mas))
            else:
                print('Ошибка введения количество аргументов!')

        elif (len(sys.argv) > 1):
            for i in range(0, len(sys.argv)):
                # print('{}-ый аргумент'.format(i + 1))
                mas += (get_argv(i, '-ый аргумент: '))
                # print('{}-ый аргумент: {}'.format(i + 1, mas[i]))
                mas += ' '
            print(field(goods, mas))
        else:
            print('Ошибка введения аргументов!')

    elif (switch == 2):
        print('Задача 2 (файл gen_random.py)')
        print('Генерация случайных чисел:')
        size = get_argv_value(2, 'Введите кол-во: ')
        if(size < 1):
            print('Ошибка! Разер больше 0 должен быть')
        else:
            numbers = gen_random(size, get_argv_value(3, 'Введите диапазон от: '),
                                 get_argv_value(4, 'Введите диапазон до: '))
            print(numbers)

    elif (switch == 3):
        print('Задача 3 (файл unique.py)')
        data = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2]
        print(data)
        mas1 = Unique(data)
        for i in Unique(mas1):
            print(i, end=' ')
        print()

        data_1 = gen_random(10, 1, 3)
        print(data_1)
        mas2 = Unique(data_1)
        for i in Unique(mas2):
            print(i, end=' ')
        print()

        data_2 = ['a', 'A', 'b', 'B', 'a', 'A', 'b', 'B']
        print(data_2)
        mas3 = Unique(data_2)
        for i in Unique(mas3):
            print(i, end=' ')
        print()

        mas4 = Unique(data_2, ignore_case=True)
        for i in Unique(mas4):
            print(i, end=' ')
        print()

        if (len(sys.argv) == 1):
            data_input = into_tuple_from_str(input('Введите любые значения в списке (между значениями ставьте пробелом)\n'))

            print(data_input)
            mas3 = Unique(data_input)
            print('С чувствительным регистром')
            for i in Unique(mas3):
                print(i, end=' ')
            print()

            print(data_input)
            mas3 = Unique(data_input, ignore_case=True)
            print('Без чувствительного регистра')
            for i in Unique(mas3):
                print(i, end=' ')
            print()

        elif (len(sys.argv) > 1):
            buff = sys.argv[2]
            for i in range(2, len(sys.argv)):
                buff = buff + ' ' + sys.argv[i]

            data_3 = into_tuple_from_str(buff)

            print(data_3)
            c = Unique(data_3)
            print('С чувствительным регистром')
            for i in Unique(c):
                print(i, end=' ')
            print()

            print(data_3)
            c = Unique(data_3, ignore_case=True)
            print('Без чувствительного регистра')
            for i in Unique(c):
                print(i, end=' ')
            print()
        else:
            print('Ошибка введения аргументов!')

    elif (switch == 4):
        print('Задача 4 (файл sort.py)')
        sort()

        if (len(sys.argv) == 1):
            data_input = into_tuple_from_str_in_value(input('Введите любые значения в списке (между значениями ставьте пробелом)\n'))

            print(f'Исходный список:\n {data_input}')

            result_with_lambda = sorted(data_input, key=lambda i: -abs(i))
            print(f'Отсортированный список с применением lambda-фнукции:\n {result_with_lambda}')

            result = sorted(data_input, key=abs, reverse=True)
            print(f'Отсортированный список без применении lambda-функции:\n {result}')

        elif (len(sys.argv) > 1):
            buff = sys.argv[2]
            for i in range(3, len(sys.argv)):
                buff = buff + ' ' + sys.argv[i]

            data_argv = into_tuple_from_str_in_value(buff)

            print(f'Исходный список:\n {data_argv}')

            result_with_lambda = sorted(data_argv, key=lambda i: -abs(i))
            print(f'Отсортированный список с применением lambda-фнукции:\n {result_with_lambda}')

            result = sorted(data_argv, key=abs, reverse=True)
            print(f'Отсортированный список без применении lambda-функции:\n {result}')
        else:
            print('Ошибка введения аргументов!')

    elif (switch == 5):
        print('Задача 5 (файл print_result.py)')
        fun_print_result()

    elif (switch == 6):
        print('Задача 6 (файл cm_timer.py)')
        cm_timer()

    # elif (switch == 7):
        # print('Задача 7 (файл process_data.py)')
        # print('Переходите в директорию lab_python_fp в файл process_data.py, чтобы выполнить это задание')

    else:
        print('Ошибка! Нет такого пункта!')

if __name__ == '__main__':
    main()