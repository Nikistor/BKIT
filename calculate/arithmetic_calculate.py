class mathematical_calculator(object):
    def __init__(self, math_calculate):
        self.math_calculation = math_calculate
        self.math_calculation_list = self.convert_string_in_list(math_calculate)
        self.list_enumeration_of_sign = self.enumeration_of_sign(self.math_calculation_list)

        self.type_error = None

        for sign in self.list_enumeration_of_sign:
            self.arithmetic_operations(sign, self.math_calculation_list)

        if(self.type_error == None):
            self.result = float(self.math_calculation_list[0])

    # Преобразование тип строки в list
    def convert_string_in_list(self, str_calculate):
        str_1 = []
        str_meaning = ''
        for i in str_calculate:
            if(i != ' '):
                str_meaning += i
            else:
                str_1.append(str_meaning)
                str_meaning = ''
        #append () добавляет в конец списка элемент, переданный ему в качестве аргумента.
        str_1.append(str_meaning)

        return str_1

    #Растановка приоритета операции
    def enumeration_of_sign(self, list_str):
        counter_sign = []
        for i in list_str:
            if ('*' == i): counter_sign.append(i)
            if ('/' == i): counter_sign.append(i)
            if ('+' == i): counter_sign.append(i)
            if ('-' == i): counter_sign.append(i)

        counter_sign = self.priority(counter_sign)

        return counter_sign

    #Подержка функции по расстановку приоритета операции
    def priority(self, list_str):
        list_1 = []
        size = len(list_str)
        count = 0
        while (size != 0):
            if ('*' in list_str or '/' in list_str):
                for i in list_str:
                    if (i == '*' or i == '/'):
                        list_1.append(i)
                size -= 1
            if ('+' in list_str or '-' in list_str):
                for i in list_str:
                    if (i == '+' or i == '-'):
                        list_1.append(i)
                size -= 1

        return list_1

    #Арифметические операции
    def arithmetic_operations(self, sign, list):
        result = None
        if (sign in list):
            for i in range(1, len(list)-1):
                try:
                    if (list[i] == sign):
                        if (sign == '*'):
                            result = float(list[i - 1]) * float(list[i + 1])
                        elif (sign == '/'):
                            result = float(list[i - 1]) / float(list[i + 1])
                        elif (sign == '+'):
                            result = float(list[i - 1]) + float(list[i + 1])
                        elif (sign == '-'):
                            result = float(list[i - 1]) - float(list[i + 1])

                        list[i] = result
                        del list[i - 1: i]
                        del list[i: i + 1]

                #Деление на 0
                except ZeroDivisionError:
                    self.type_error = 'Division by 0'
                    self.result = 'infinity'

                #Граница вне диапазона
                except:
                    return result

    def calculate(self, math_calculate):
        self.math_calculation = math_calculate
        self.math_calculation_list = self.convert_string_in_list(math_calculate)
        self.list_enumeration_of_sign = self.enumeration_of_sign(self.math_calculation_list)

        self.type_erorr = None

        for sign in self.list_enumeration_of_sign:
            self.arithmetic_operations(sign, self.math_calculation_list)

        if(self.type_erorr == None):
            self.result = float(self.math_calculation_list[0])

        return self