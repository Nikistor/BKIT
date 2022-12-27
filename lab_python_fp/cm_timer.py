#time - время, sleep - задержка
from time import time, sleep
from contextlib import contextmanager

# На основе класса
class cm_timer_1:
    def __int__(self):
        self._start = 0
        self._end = 0

    def __enter__(self):
        self._start = time()

    def __exit__(self, the_type, the_value, the_backing):
        self._end = time()
        print(f'Время работы блок кода: {self._end - self._start}')

# С использованием библиотеки contextlib
@contextmanager
def cm_timer_2():
    start_time = time()
    # Yield – ключевое слово, которое используется вместо return. С его помощью функция возвращает значение
    # без уничтожения переменных, кроме того, при каждом последующем вызове функция начинает своё
    # выполнение с оператора yield.
    yield None
    end_time = time()
    print(f'Время работы блок кода: {end_time - start_time}')

def cm_timer():
    with cm_timer_1():
        sleep(5.5)

    with cm_timer_2():
        sleep(5.5)