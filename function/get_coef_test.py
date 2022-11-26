import sys

def get_coef_test_no_cmd(index, value):
    if (index > 3 or index < 1):
        print('Индекс вне диапазона. Индексом должен быть 1, 2 и 3')
        return None

    while True:
        # Вводим с клавиатуры
        coef_str = str(value)
        # Проверка, есть ли минус числа и нулевой коэффициент?

        if (coef_str[0] == '-'):
            coef_str_buff = coef_str.replace('-', '')
            if (coef_str_buff.isdigit()):
                break
        if (coef_str.isdigit()):
            break
        else:
            print("Ошибка! Введите натуральное число!")
            return None

    # Переводим строку в действительное число
    coef = float(coef_str)
    return coef


def get_coef_test_with_cmd(index, value):
    if(index > 3 or index < 1):
        print('Индекс вне диапазона. Индексом должен быть 1, 2 и 3')
        return None

    # Пробуем прочитать коэффициент из командной строки
    coef_str = str(value)

    if (coef_str[0] == '-'):
        coef_str = coef_str.replace('-', '')
        # print('coef_str_if', coef_str)
    else:
        coef_str = str(value)
        # print('coef_str_else', coef_str)

    if (coef_str.isdigit() == True):
        coef_str = str(value)
        # print(f'{coef_str} явл-ется числом', )
    else:
        print('Ошибка! Введите натуральное число!')
        return None

    coef = float(coef_str)
    return coef