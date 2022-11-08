import sys
import math

def get_coef(index, prompt):
    '''
        Читаем коэффициент из командной строки или вводим с клавиатуры
        Args:
            index (int): Номер параметра в командной строке
            prompt (str): Приглашение для ввода коэффицента
        Returns:
            float: Коэффициент квадратного уравнения
        '''
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

    except:
        while True:
            # Вводим с клавиатуры
            print(prompt)
            coef_str = input()
            # Проверка, есть ли минус числа и нулевой коэффициент?
            if (coef_str[0] != '0' or index == 2 or index == 3):
                if (coef_str[0] == '-'):
                    coef_str_buff = coef_str.replace('-', '')
                    if (coef_str_buff.isdigit()):
                        break
                if (coef_str.isdigit()):
                    break

            print("Ошибка! Введите натуральное число!")

    # Переводим строку в действительное число
    coef = float(coef_str)
    return coef


def get_roots(a, b, c):
    result = []
    D = b * b - 4 * a * c

    # Если дискриминат равен нулю, то корень может быть только одним
    if D == 0.0:
        root = -b / (2.0 * a)
        result.append(root)
        if (root > 0.0):
            root1 = math.sqrt(root)
            result.append(root1)
            result.append(-root1)

    # Если дискриминат больше нули, то корень может быть четырем
    elif D > 0.0:
        sqD = math.sqrt(D)
        root1 = (-b + sqD) / (2.0 * a)
        root2 = (-b - sqD) / (2.0 * a)

        if (root1 == 0):
            result.append(abs(root1))
        elif (root2 == 0):
            result.append(abs(root2))

        if (root1 > 0.0):
            root3 = math.sqrt(root1)
            result.append(root3)
            result.append(-root3)

        if (root2 > 0.0):
            root4 = math.sqrt(root2)
            result.append(root4)
            result.append(-root4)

    return result


def main():
    while True:
        try:
            a = get_coef(1, 'Введите коэффициент А:')
            b = get_coef(2, 'Введите коэффициент B:')
            c = get_coef(3, 'Введите коэффициент C:')

            # Вычисление корней
            roots = get_roots(a, b, c)

            # Вывод корней
            len_roots = len(roots)
            if len_roots == 0:
                print('Нет корней')
            elif len_roots == 1:
                print('Один корень {}'.format(round(roots[0], 2)))
            elif len_roots == 2:
                print('Два кореня: {} и {}'.format(round(roots[0], 2), round(roots[1], 2)))
            elif len_roots == 3 and roots[0] == 0.0:
                print('Три корня: {} и {} и {}'.format(round(roots[0], 2), round(roots[1], 2), round(roots[2], 2)))
            elif len_roots == 3:
                print('Два корня: {} и {}'.format(round(roots[1], 2), round(roots[2], 2)))
            elif len_roots == 4:
                print(
                    'Четыре корня: {} и {} и {} и {}'.format(round(roots[0], 2), round(roots[1], 2), round(roots[2], 2),
                                                             round(roots[3], 2)))
            break
        except:
            print('Ошибка заполнения!')
            break


# Если сценарий запущен из командной строки
if __name__ == "__main__":
    main()