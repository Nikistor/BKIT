import json

file_locator = 'D:\Работа\МГТУ им. Н.Э.Баумана\Программирование\Программы\Программы за 5 семестр\DZ\calculate\data'

#Запись данных
def data_recording(data, title=file_locator):
    with open(f"{title}.json", "w", encoding="utf-8") as file:
        json.dump(data, file, indent=2, ensure_ascii=False)

#Чтение данных
def load_data(title=file_locator):
    with open(f"{title}.json", "r") as file:
        data = json.load(file)
    return data

#Добавление данных
def combined_data(data_json, id_user='id_user', title=file_locator):
    #Если есть файл и не пустой
    try:
        with open(f"{title}.json", encoding="utf-8") as file:
            data = json.load(file)
            temp = data[id_user]
            for info_data in data_json[id_user]:
                n = {
                    'id': info_data['id'],
                    'meaning': info_data['meaning'],
                    'result': info_data['result']
                }
            temp.append(n)
        data_recording(data)
    #Если нет файла
    except:
        data_recording(data_json)

#Загрузка данных для идентификатора пользователя
def load_data_for_id_user(id_user, title=file_locator):
    try:
        with open(f"{title}.json", "r", encoding="utf-8") as file:
            data = json.load(file)
            temp = data[id_user]
            for info_data in data[id_user]:
                n = {
                    'id': info_data['id'],
                    'meaning': info_data['meaning'],
                    'result': info_data['result']
                }
            temp.append(n)
        return temp
    except:
        return 'Ошибка! Такого идентификатора не существует.'

#Удаление данных для индентификатора пользователя
def delete_data_for_id_user(id_user, title=file_locator):
    try:
        with open(f"{title}.json", encoding="utf-8") as file:
            data = json.load(file)
            data_1 = {}
            for id_user_data in data:
                if (id_user != id_user_data):
                    temp = data[id_user_data]
                    data_1 = {id_user_data: []}
                    for j in temp:
                        n = {
                            'id': j['id'],
                            'meaning': j['meaning'],
                            'reault': j['result']
                        }
                        data_1[id_user_data].append(n)
                    temp.append(data_1)
        data_recording(data_1)
    except:
        return 'Ошибка! Такого идентификатора не существует.'