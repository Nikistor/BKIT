data = [4, -30, 30, 100, -100, 123, 1, 0, -1, -4]

def sort():
    print(f'Исходный список:\n {data}')
    result_with_lambda = sorted(data, key=lambda i: -abs(i))
    print(f'Отсортированный список с использованием lambda-функции:\n {result_with_lambda}')
    # sorted - функция, который упорядочивает значения
    result = sorted(data, key=abs, reverse=True)
    print(f'Отсортированный список без изпользования lambda-функции:\n {result}')