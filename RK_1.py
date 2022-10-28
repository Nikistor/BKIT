from operator import itemgetter

# Класс Раздел
class Section:

    def __init__(self, id, name, page, document_id):
        # Номер раздела
        self.id = id
        # Наименование раздела
        self.name = name
        # Количество страниц раздела
        self.page = page
        # Номер документа
        self.document_id = document_id

# Класс Документ
class Document:

    def __init__(self, id, name):
        # Номер документа
        self.id = id
        # Наименование документа
        self.name = name

# Класс Раздел Документ
class SectionDocument:

    def __init__(self, document_id, section_id):
        self.document_id = document_id
        self.section_id = section_id

# Документы
documents = [
    Document(1, 'Положение'),
    Document(2, 'Агентский договор'),
    Document(3, 'Правила'),
    Document(4, 'Инструкция'),
    Document(5, 'Регламент'),
]

# Разделы
sections = [
    Section(1, 'Содержание', 10, 1),
    Section(2, 'Введение', 20, 2),
    Section(3, 'Определение', 31, 5),
    Section(4, 'Нормативные ссылки', 8, 2),
    Section(5, 'Заключение', 44, 3),
    Section(6, 'Список использованных источников', 28, 4),
    Section(7, 'Общие положения', 61, 1),
    Section(8, 'Права', 11, 5),
    Section(9, 'Функции', 66, 3),
    Section(10, 'Ответственность', 94, 4),
]

# Разделы документов
sections_documents = [
    SectionDocument(2, 1),
    SectionDocument(3, 5),
    SectionDocument(4, 3),
    SectionDocument(5, 6),
    SectionDocument(5, 2),
    SectionDocument(1, 4),
    SectionDocument(4, 7),
    SectionDocument(3, 6),
    SectionDocument(1, 1),
    SectionDocument(5, 3),
]

def main():
    # Соединение данных один-ко-многим
    one_to_many = [(sec.name, sec.page, document.name)
                   for document in documents
                   for sec in sections
                   if sec.document_id == document.id]

    # Соединение данных многие-ко-многим
    many_to_many_temp = [(document.name, sec_documents.document_id, sec_documents.section_id)
                         for document in documents
                         for sec_documents in sections_documents
                         if document.id == sec_documents.document_id]

    many_to_many = [(sec.name, sec.page, document_name)
                    for document_name, document_id, sec_id in many_to_many_temp
                    for sec in sections if sec.id == sec_id]

    print('Задание Г1')
    mas_dict = {}
    for folder_name, i, document_name in one_to_many:
        if document_name[0] == 'А':
            if document_name in mas_dict:
                mas_dict[document_name].append(folder_name)
            else:
                mas_dict[document_name] = [folder_name]
    print(*mas_dict.items())

    print('\nЗадание Г2')
    mas_dict_1 = {}
    for i, poisk_max, document_name in one_to_many:
        if document_name in mas_dict_1:
            mas_dict_1[document_name] = max(mas_dict_1[document_name], poisk_max)
        else:
            mas_dict_1[document_name] = poisk_max
        mas_dict_1 = {key: meaning for key, meaning in sorted(mas_dict_1.items(), key=lambda item: item[1])}
    print(*mas_dict_1.items())

    print('\nЗадание Г3')
    mas_list = []
    for folder_name, i, document_name in many_to_many:
        mas_list.append((document_name, folder_name))
    mas_list = sorted(mas_list, key=lambda item: item[0])
    print(*mas_list)

if __name__ == '__main__':
    main()