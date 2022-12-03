import sys
import math

from function.get_coef import get_coef
from function.get_roots import get_roots
# Основная программа
def main():
    while True:
        try:
            a = get_coef(1, 'Введите коэффициент А:')
            b = get_coef(2, 'Введите коэффициент B:')
            c = get_coef(3, 'Введите коэффициент C:')

            if (a == None or b == None or c == None):
                print()
                print('Ошибка заполнения!')
                break

            # Вычисление корней
            roots = get_roots(a, b, c)

            # Вывод корней
            len_roots = len(roots)
            if len_roots == 0:
                print('Нет корней')
            elif len_roots == 1:
                print('Один корень {}'.format(round(roots[0], 2)))
            elif len_roots == 2:
                print('Два корня: {} и {}'.format(round(roots[0], 2), round(roots[1], 2)))
            elif len_roots == 3 and roots[0] == 0.0:
                print('Три корня: {} и {} и {}'.format(round(roots[0], 2), round(roots[1], 2), round(roots[2], 2)))
            elif len_roots == 3:
                print('Два корня: {} и {}'.format(round(roots[1], 2), round(roots[2], 2)))
            elif len_roots == 4:
                print(
                    'Четыре корня: {} и {} и {} и {}'.format(round(roots[0], 2), round(roots[1], 2), round(roots[2], 2),
                                                             round(roots[3], 2)))
            else:
                print('Ошибка! Корней нет!')
            break

        except ArithmeticError:
            print('Ошибка! Коэффициент a должен быть натуральным числом!')
            break

# Если сценарий запущен из командной строки
if __name__ == "__main__":
    main()
