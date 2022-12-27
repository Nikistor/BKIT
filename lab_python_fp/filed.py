goods = [
    {'title': 'Ковер', 'price': 2000, 'color': 'green'},
    {'title': 'Диван для отдыха', 'price': 5300, 'color': 'black'}
 ]
# field(goods, 'title') должен выдавать 'Ковер', 'Диван для отдыха'
# field(goods, 'title', 'price') должен выдавать {'title': 'Ковер', 'price': 2000}, {'title': 'Диван для отдыха', 'price': 5300}

def field(items, *args):
    try:
        # Преобразование в кортеж из строки
        argv = into_tuple_from_str(*args)
        # Необходимо реализовать генератор
        # len () возвращает длину (количество элементов) в объекте.
        assert len(argv) > 0, 'Ошибка! Нет аргументов! \nПримечание аргументы не должны быть пустыми!'
        #range - диапазон, len - длина списка
        #items - это переменная, в которой на каждой итерации оказывается элемент списка.
        r = [{} for i in range(len(items))]
        for i in range(len(items)):
            for j in items[i]:
                if j in argv:
                    # updatе - метод обновления словаря элементами из другого объекта словаря.
                    r[i].update({j: items[i][j]})
        # возврат значения
        return r
    except:
        print('Ошибка! Нет списка в качестве переданного аргумента!')

# Преобразование в строку из кортежа
def into_tuple_from_str(str):
    cortes_buf = []
    str_buf = ''
    for i in range(len(str)):
        if (str[i] == ' '):
            cortes_buf.append(str_buf)
            str_buf = ''
        else:
            str_buf += str[i]
    # append - метод добавления элементов
    cortes_buf.append(str_buf)
    # возврат значения
    return cortes_buf