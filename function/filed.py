goods = [
    {'title': 'Ковер', 'price': 2000, 'color': 'green'},
    {'title': 'Диван для отдыха', 'price': 5300, 'color': 'black'}
 ]

def field(items, *args):
    try:
        # Преобразование в кортеж из строки
        argv = into_cortes_from_str(*args)
        # Необходимо реализовать генератор
        # len () возвращает длину (количество элементов) в объекте.
        assert len(argv) > 0, 'Ошибка! Нет аргументов! \nПримечание аргументы не должны быть пустыми!'
        #range - диапазон, len - длина списка
        #items - это переменная, в которой на каждой итерации оказывается элемент списка.
        n = [{} for i in range(len(items))]
        for i in range(len(items)):
            for j in items[i]:
                if j in argv:
                    #updatе - метод обновления словаря элементами из другого объекта словаря.
                    n[i].update({j: items[i][j]})
        # возврат значения
        return n
    except:
        print('Ошибка! Нет списка в качестве переданного аргумента!')

# Преобразование в строку из кортежа
def into_cortes_from_str(str):
    cortes = []
    str_buf = ''
    for i in range(len(str)):
        if (str[i] == ' '):
            cortes.append(str_buf)
            str_buf = ''
        else:
            str_buf += str[i]
    # append - метод добавления элементов
    cortes.append(str_buf)
    # возврат значения
    return cortes