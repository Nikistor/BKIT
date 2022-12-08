import random

from calculate.json_function import data_recording, load_data, combined_data, load_data_for_id_user
from calculate.arithmetic_calculate import mathematical_calculator as smc

#Генерация значений
def generator_of_meaning(id_user='id_user'):
    arithmetic = ['+', '-', '/', '*']

    arith = arithmetic[random.randint(0, 3)]
    gen_id = random.randint(0, 100000)
    m_1 = random.randint(0, 1000)
    m_2 = random.randint(0, 1000)
    class_calculate = smc(str(m_1) + ' ' + str(arith) + ' ' + str(m_2))

    data = {
        str(id_user): [
                {"id": gen_id,
                "meaning": (str(m_1) + ' ' + str(arith) + ' ' + str(m_2)),
                "result": class_calculate.result}
        ]
    }
    combined_data(data, id_user)

#Получение информации
def get_info():
    try:
        data = load_data()
        return data
    except:
        return 'Нет файла'

#Получение информации с идентификатором пользователя
def get_info_with_id_user(id_user):
    try:
        data = load_data_for_id_user(id_user)
        return data
    except:
        return 'Нет файла'