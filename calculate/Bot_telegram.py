import configuration
import telebot
from telebot import types
import random

#SageMathCloud (сокращённо SMC) — это онлайновый сервис, в котором можно написать математический или любой другой расчёт.
from arithmetic_calculate import mathematical_calculator as smc
from json_function import combined_data, delete_data_for_id_user, load_data_for_id_user
from work_calculate import generator_of_meaning

# Создание бота
bot = telebot.TeleBot(configuration.token)

SPISOK = '''
/menu - Меню (кнопки переключателя)
/calculate - Бот-калькулятор (посчет арифметических операций)
/story - Просмотр история вычисления
/cleaner - Очистка истории вычисления
/generation - Генерация случайных вычислений
/image - Просмотр изображения
'''

# Список меню
@bot.message_handler(commands=['spisok'])
def menu(message):
    bot.send_message(message.chat.id, SPISOK)

# При нажатии на /menu
@bot.message_handler(commands=['menu'])
def menu(message):
    markup = types.InlineKeyboardMarkup(row_width=1)
    btn_1 = types.InlineKeyboardButton(text="Решить пример", callback_data='btn_1')
    btn_2 = types.InlineKeyboardButton(text="Посмотреть историю вычисления", callback_data='btn_2')
    btn_3 = types.InlineKeyboardButton(text="Очистить истории вычисления", callback_data='btn_3')
    btn_4 = types.InlineKeyboardButton(text="Генерировать вычисления", callback_data='btn_4')
    btn_5 = types.InlineKeyboardButton(text="Посмотреть изображение", callback_data='btn_5')
    markup.add(btn_1, btn_2, btn_3, btn_4, btn_5)
    bot.send_message(message.chat.id, text=f"Привет, {message.from_user.first_name}! Выберите то, что Вам нужно",
                     reply_markup=markup)

# Кнопки переключателя при нажатии на /menu
@bot.callback_query_handler(func=lambda callback: callback.data)
def check_callback_data(callback):
    #Пользовательский индентификатор
    user_id = str(callback.from_user.id)

    if (callback.data == "btn_1"):
        bot.send_message(callback.message.chat.id, 'Напишите пример вычисления')

        # Пользовательский индентификатор
        user_id = str(callback.from_user.id)

        @bot.message_handler(content_types=["text"])
        def info(message):
            meaning = smc(message.text)
            bot.send_message(message.chat.id, f'Решение: {meaning.result}')
            data = {
                user_id: [{"id": random.randint(0, 10000),
                        "meaning": str(message.text),
                        "result": str(meaning.result)}]
            }
            combined_data(data, str(message.from_user.id))

    elif (callback.data == "btn_2"):
        bot.send_message(callback.message.chat.id, 'История вычисления')
        data = load_data_for_id_user(str(user_id))
        if(data == 'Ошибка! Такого идентификатора не существует.'):
            bot.send_message(callback.message.chat.id, 'Нет базы данных')
        else:
            for j in range(len(data) - 1):
                id = data[j]['id']
                meaning = data[j]['meaning']
                result = data[j]['result']
                print_info = f'id:{id}\n{meaning} = {result}\n\n'
                bot.send_message(callback.message.chat.id, print_info)

    elif(callback.data == "btn_3"):
        bot.send_message(callback.message.chat.id, 'Очистка истории вычисления')

        check_error = delete_data_for_id_user(user_id)

        if(check_error != 'Ошибка! Такого идентификатора не существует.'):
            bot.send_message(callback.message.chat.id, 'Операция прошла успешно')
        else:
            bot.send_message(callback.message.chat.id, check_error)

    elif (callback.data == "btn_4"):
        bot.send_message(callback.message.chat.id, 'Генерация случайных вычислений')
        generator_of_meaning(user_id)
        bot.send_message(callback.message.chat.id, 'Операция прошла успешно')

    elif (callback.data == "btn_5"):
        img = open('moscow.jpg', 'rb')
        bot.send_photo(callback.message.chat.id, img)

    else:
        bot.send_message(callback.chat.id, 'Нет такой команды. Введите /spisok')

# Вычисления
@bot.message_handler(commands=['calculate'])
def start_calculate(message):
    bot.send_message(message.chat.id, 'Напишите пример вычисления')

    # Пользовательский идентификатор
    user_id = str(message.from_user.id)

    @bot.message_handler(content_types=["text"])
    def info(message):
        meaning = smc(message.text)
        bot.send_message(message.chat.id, f'Результат решения: {meaning.result}')
        data = {
            user_id: [{"id": random.randint(0, 10000),
                 "meaning": str(message.text),
                 "result": str(meaning.result)}]
        }
        combined_data(data, str(message.from_user.id))

# Просмотр история вычисления
@bot.message_handler(commands=['story'])
def start_story(message):
    bot.send_message(message.chat.id, 'История вычисления')

    # Пользовательский идентификатор
    user_id = str(message.from_user.id)

    data = load_data_for_id_user(str(user_id))

    if (data == 'Ошибка! Такого идентификатора не существует.'):
        bot.send_message(message.chat.id, 'Нет базы данных')
    else:
        for j in range(len(data) - 1):
            id = data[j]['id']
            meaning = data[j]['meaning']
            result = data[j]['result']
            print_info = f'id: {id}\n{meaning} = {result}\n\n'
            bot.send_message(message.chat.id, print_info)

#Просмотр изображения
@bot.message_handler(commands=['image'])
def start_image(message):
    img = open('moscow.jpg', 'rb')
    bot.send_photo(message.chat.id, img)

#Генерация случайных вычислений
@bot.message_handler(commands=['generation'])
def start_generation(message):
    bot.send_message(message.chat.id, 'Генерация случайных вычислений')

    #Пользовательский идентификатор
    user_id = str(message.from_user.id)

    generator_of_meaning(user_id)

    bot.send_message(message.chat.id, 'Операция прошла успешно')

#Очистка истории вычисления
@bot.message_handler(commands=['cleaner'])
def start_cleaner(message):
    bot.send_message(message.chat.id, 'Очистка истории вычислений')

    # Пользовательский идентификатор
    user_id = str(message.from_user.id)

    check_error = delete_data_for_id_user(user_id)

    if (check_error != 'Ошибка! Такого идентификатора не существует.'):
        bot.send_message(message.chat.id, 'Операция прошла успешно')
    else:
        bot.send_message(message.chat.id, check_error)

#Работа программы в телеграме без остановки
bot.polling(none_stop=True)