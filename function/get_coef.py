import sys

def get_coef(index, prompt):
    if (index > 3 or index < 1):
        print('Индекс вне диапазона. Индексом должен быть 1, 2 и 3')
        return None

    try:
        # Пробуем прочитать коэффициент из командной строки
        coef_str = sys.argv[index]

        if(coef_str[0] == '-'):
            coef_str = sys.argv[index].replace('-','')
            # print('coef_str_if', coef_str)
        else:
            coef_str = sys.argv[index]
            # print('coef_str_else', coef_str)

        if(coef_str.isdigit() == True):
            coef_str = sys.argv[index]
            # print(f'{coef_str} явл-ется числом', )
        else:
            print('Ошибка! Введите натуральное число!')
            return None

    except:
        while True:
            # Вводим с клавиатуры
            print(prompt)
            coef_str = input()

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

