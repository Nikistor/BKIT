from lab_python_oop.rectangle import Rectangle
from lab_python_oop.circle import Circle
from lab_python_oop.square import Square

import sys
"""Def – это инструкция, позволяющая создавать функцию."""
def get_coef(index, prompt):
    try:
        #Пробуем прочитать коэффициент из командной строки
        coef_str = sys.argv[index]
    except:
        while True:
            #Вводим с клавиатуры
            print(prompt)
            coef_str = input()
            # Проверка, есть ли минус и 0?
            if (int(coef_str) > 0 and int(coef_str) < 20):
                break
            else:
                print('Ошибка! Введите номер варианта от 1 до 20')
    #Переводим строку в действительное число
    coef = float(coef_str)
    return coef

def main():
    N = get_coef(1, 'Введите номер вашего варианта по списку журнала:')
    if (N > 0 and N < 20):
        r = Rectangle("синего", N, N)
        c = Circle("зеленого", N)
        s = Square("красного", N)
        print(r)
        print(c)
        print(s)
    else:
        print('Ошибка! Введите номер варианта от 1 до 20')

if __name__ == "__main__":
    main()
