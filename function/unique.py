# Итератор для удаления дубликатов
class Unique(object):
    def __init__(self, items, **kwargs):
        self.arr = []

        # Используя кортежи, получаем ключ и значения
        for key, meaning in kwargs.items():
            # Если ключ пустой и значение TRUE, то
            if key == 'ignore_case' and meaning == True:
                # Методы lower () возвращают строку в нижнем регистре из заданной строки.
                # Он преобразует все заглавные символы в строчные.
                items = [i.lower() for i in items]

        for index in items:
            # Если текущее значение из списка item не совпадает/не существует в созданном списке mas
            if index not in self.arr:
                # То присваиваем несуществующее значение в созданном списке arr
                self.arr.append(index)
        pass

    # Для перехода к следующему элементу используется метод __next__.
    def __next__(self):
        try:
            x = self.arr[self.begin]
            self.begin += 1
            return x
        except:
            # Оператор raise позволяет принудительно породить исключение. (Заверщение работы итератора)
            raise StopIteration

    #__iter__(self) метод, который возвращает объект итератора;
    def __iter__(self):
        self.begin = 0
        return self