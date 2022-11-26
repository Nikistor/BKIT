import math
# Функция высчисления дискримината
# Получение корней
def get_roots(a, b, c):
    result = []
    D = b * b - 4 * a * c

    # Если дискриминат равен нулю, то корень может быть только один
    if D == 0.0:
        root = -b / (2.0 * a)
        # result.append(root)
        if (root > 0.0):
            root1 = math.sqrt(root)
            result.append(root1)
            result.append(-root1)

    # Если дискриминат больше нуля, то корнем может быть четыре
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
