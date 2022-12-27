# Пример:
# gen_random(5, 1, 3) должен выдать выдать 5 случайных чисел в диапазоне от 1 до 3, например 2, 2, 3, 2, 1
# Hint: типовая реализация занимает 2 строки

import random
# gen_random(количество, минимум, максимум)
def gen_random(num_count, begin, end):
    mas = []
    # range - диапазон
    for i in range(0, num_count):
        # генерация случайных чисел
        mas.append(int(random.randint(begin, end)))
    # Возврат значения
    return mas