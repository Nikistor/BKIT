import unittest

from RK_2 import Section, Document, SectionDocument, task_1, task_2, task_3

modul_document = [
    Document(1, 'Отчет по БКИТ'),
    Document(2, 'Акт'),
    Document(3, 'Практическое задание')
]
modul_section = [
    Section(1, 'Список литературы', 3, 2),
    Section(2, 'Задания', 4, 3),
    Section(3, 'Результат работы', 25, 1)
]
modul_sections_documents = [
    SectionDocument(2, 1),
    SectionDocument(1, 1),
    SectionDocument(3, 2)
]

class test_section(unittest.TestCase):
    def test_class_section_zero_parameters(self):
        with self.assertRaises(TypeError) as context:
            Section()
        self.assertEqual(
            "__init__() missing 4 required positional arguments: 'id', 'name', 'page', and 'document_id'",
            str(context.exception)
        )

    def test_class_section_zero_meaning(self):
        test_class_section = Section(None, None, None, None)
        self.assertEqual(test_class_section.id, None)
        self.assertEqual(test_class_section.name, None)
        self.assertEqual(test_class_section.page, None)
        self.assertEqual(test_class_section.document_id, None)

    def test_class_section_meaning(self):
        test_class_section = Section(1, 'Технические основы разработки', 10, 3)
        self.assertEqual(test_class_section.id, 1)
        self.assertEqual(test_class_section.name, 'Технические основы разработки')
        self.assertEqual(test_class_section.page, 10)
        self.assertEqual(test_class_section.document_id, 3)

    def test_class_document_meaning(self):
        test_class_document = Document(1, 'Отчет по МД')
        self.assertEqual(test_class_document.id, 1)
        self.assertEqual(test_class_document.name, 'Отчет по МД')

    def test_class_section_document_meaning(self):
        test_class_sections_documents = SectionDocument(3, 1)
        self.assertEqual(test_class_sections_documents.document_id, 3)
        self.assertEqual(test_class_sections_documents.section_id, 1)

    #Тестирование задания 1
    def test_task_1(self):
        self.assertEqual(dict(task_1(modul_document, modul_section)), {'Акт': ['Список литературы']})

    #Тестирование задания 2
    def test_task_2(self):
        self.assertEqual(dict(task_2(modul_document, modul_section)), {'Отчет по БКИТ': 25, 'Практическое задание': 4, 'Акт': 3})

    #Тестирование задания 3
    def test_task_3(self):
        self.assertEqual(task_3(modul_document, modul_section), [('Акт', 'Список литературы'), ('Отчет по БКИТ', 'Список литературы')])

if __name__ == '__main__':
    unittest.main()