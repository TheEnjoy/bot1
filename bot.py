# coding=utf-8
import telebot
import os
import sqlite3 as sql

from telebot import types

# connection = sql.connect('user.sqlite', check_same_thread=False)
# q = connection.cursor()

# q.execute('''CREATE TABLE user
# (id int auto_increment primary key,
# IDIS varchar(100),
# Name varchar(100),
# Number varchar(100),
# Date varchar(100),
# Time varchar(100),
# People varchar(100),
# Koment varchar(100))''')
# connection.commit()


TOKEN = '775824922:AAFH6EVud1_pCgQD6buzuH1-E89xi5V9KEA'
PHOTO_ZA1 = 'AgADAgADIasxGwxc0Em0g6bONWDWW0VCXw8ABIJmNSCXSDyOaMYAAgI'
PHOTO_ZA2 = 'AgADAgADvKkxGwxc2EljbPgn3Gpiy_-cOQ8ABAfnUhaBhEt0XpUDAAEC'
PHOTO_INT1 = 'AgADAgADxakxGwxc2EkORu3mO5vSPYlnXw8ABI3DjdW2WqBvCMcAAgI'
PHOTO_INT2 = 'AgADAgADxqkxGwxc2EkU8NY1YgtJS0ukOQ8ABI9Pf_7PynwBsqADAAEC'
PHOTO_INT3 = 'AgADAgADx6kxGwxc2EnRpV0tIctxXIxZOQ8ABGUOYXmNeDfavY0BAAEC'
PHOTO_INT4 = 'AgADAgADyakxGwxc2EnaZmHx02hjXGLktw4ABFLzvSWU9gwL-7kFAAEC'

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands = ['start'])
def first(message):
    key = types.ReplyKeyboardMarkup(True, False)
    key.row('ℹ О нас', '📖 Меню')
    key.row('🛋 Интерьер')
    key.row('🍽 Забронировать столик')
    key.row('🚗 Доставка')
    bot.send_message(message.chat.id, 'Выберите действие ⤵', reply_markup=key)


@bot.message_handler(content_types =['text', 'contact'])
def main(message):
    if message.text == 'ℹ О нас':
        keyboard = telebot.types.ReplyKeyboardMarkup(True, False)
        keyboard.row('Ⓜ Главное меню')
        bot.send_message(message.chat.id, '▫️LOFT - это новый ресторан со смешанной кухней!\n\nУ нас вы можете попробовать мясные/крабовые бургеры и пиццу.\nВ меню всегда есть свежие морепродукты, а также изысканные блюда из фермерских продуктов!\nМы подаем лучшие сорта разливного и бутылочного пива, различные согревающие и соблазняющие коктейли.\n\nLOFT - это место, где проходят вечеринки, кулинарные мастер-классы и анимационные игры для детей. Каждую среду и\nвоскресенье мы собираемся на увлекательную игру Мафия!\nВ День Рождения скидка 20%\n\n🏡  Люберцы, ул Кирова 3\n☎️  8 (495) 784-07-27\n🕘  12:00 - 00:00\n🌐  www.instagram.com/resto_loft')
        send = bot.send_message(message.chat.id, 'Выберите действие ⤵', reply_markup=keyboard)
        bot.register_next_step_handler(send, main)
    elif message.text == '📖 Меню':
        keyboard = telebot.types.ReplyKeyboardMarkup(True, False)
        keyboard.row('🍽 Забронировать столик')
        keyboard.row('🚗 Доставка')
        keyboard.row('Ⓜ Главное меню')
        bot.send_photo(message.chat.id, PHOTO_ZA1)
        bot.send_photo(message.chat.id, PHOTO_ZA2)
        bot.send_message(message.chat.id, 'Выберите действие ⤵', reply_markup=keyboard)
    elif message.text == '🛋 Интерьер':
        keyboard = types.ReplyKeyboardMarkup(True, False)
        keyboard.row('Ⓜ Главное меню')
        bot.send_photo(message.chat.id, PHOTO_INT1)
        bot.send_photo(message.chat.id, PHOTO_INT2)
        bot.send_photo(message.chat.id, PHOTO_INT3)
        bot.send_photo(message.chat.id, PHOTO_INT4)
        send = bot.send_message(message.chat.id, 'Выберите действие ⤵', reply_markup=keyboard)
        bot.register_next_step_handler(send, main)
    elif message.text == '🍽 Забронировать столик':
        keyboard = types.ReplyKeyboardMarkup(True, False)
        keyboard.row('Ⓜ Главное меню')
        send = bot.send_message(message.chat.id, 'Пожалуйста, представтесь:', reply_markup=keyboard)
        bot.register_next_step_handler(send, next2)
    elif message.text == '🚗 Доставка':
        keyboard = types.ReplyKeyboardMarkup(True, False)
        keyboard.row('Ⓜ Главное меню')
        send = bot.send_message(message.chat.id, 'Пожалуйста, представтесь:', reply_markup=keyboard)
        bot.register_next_step_handler(send, a1)
    elif message.text == 'Ⓜ Главное меню':
        first(message)

def next2(message):
    if message.text == 'Ⓜ Главное меню':
        first(message)
    elif message.text:
        # global user_id
        # global user_name
        # user_id = message.from_user.id
        # user_name = message.text
        # print('Id Пользователя =', message.from_user.id)
        # print('Имя =', message.text)
        keyboard = types.ReplyKeyboardMarkup(True, False)
        button_phone = types.KeyboardButton(text='Оставить номер', request_contact=True)
        keyboard.add(button_phone)
        keyboard.row('Ⓜ Главное меню')
        send = bot.send_message(message.chat.id, 'Очень приятно, {name}. Оставьте, пожалуйста, Ваш номер телефона:'.format(name=message.text), reply_markup=keyboard)
        bot.register_next_step_handler(send, next3)

def next3(message):
    if message.text == 'Ⓜ Главное меню':
        first(message)
    elif message.contact:
        # global user_phone
        # user_phone = message.contact.phone_number
        keyboard = types.ReplyKeyboardMarkup(True, False)
        keyboard.row('Ⓜ Главное меню')
        send = bot.send_message(message.chat.id, 'Напишите желаемую дату:', reply_markup=keyboard)
        bot.register_next_step_handler(send, next4)
    elif message.text:
        send = bot.send_message(message.chat.id, 'Оставьте, пожалуйста, ваш номер телефона.')
        bot.register_next_step_handler(send, next3)

def next4(message):
    if message.text == 'Ⓜ Главное меню':
        first(message)
    else:
        # global user_date
        # user_date = message.text
        keyboard = types.ReplyKeyboardMarkup(True, False)
        keyboard.row('12:00', '12:30')
        keyboard.row('13:00', '13:30')
        keyboard.row('14:00', '14:30')
        keyboard.row('15:00', '15:30')
        keyboard.row('16:00', '16:30')
        keyboard.row('17:00', '17:30')
        keyboard.row('18:00', '18:30')
        keyboard.row('19:00', '19:30')
        keyboard.row('20:00', '20:30')
        keyboard.row('21:00', '21:30')
        keyboard.row('Ⓜ Главное меню')
        send = bot.send_message(message.chat.id, 'Выберите время', reply_markup=keyboard)
        bot.register_next_step_handler(send, next6)

def next6(message):
    if message.text == 'Ⓜ Главное меню':
        first(message)
    else:
        # global user_time
        # user_time = message.text
        keyboard = types.ReplyKeyboardMarkup(True, False)
        keyboard.row('1', '2', '3', '4', '5', '6')
        keyboard.row('Ⓜ Главное меню')
        send = bot.send_message(message.chat.id, 'Укажите количество персон:', reply_markup=keyboard)
        bot.register_next_step_handler(send, next7)

def next7(message):
    if message.text == 'Ⓜ Главное меню':
        first(message)
    elif message.text:
        # global user_people
        # user_people = message.text
        keyboard = types.ReplyKeyboardMarkup(True, False)
        keyboard.row('Ⓜ Главное меню')
        send = bot.send_message(message.chat.id, 'Если нужно, оставьте комментарий:', reply_markup=keyboard)
        bot.register_next_step_handler(send, next8)

def next8(message):
    if message.text == 'Ⓜ Главное меню':
        first(message)
    elif message.text:
        # global user_koment
        # user_koment = message.text
        # q.execute("INSERT INTO user (IDIS, Name, Number, Date, Time, People, Koment) VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s')"%(user_id, user_name, user_phone, user_date, user_time, user_people, user_koment))
        send = bot.send_message(message.chat.id, 'Спасибо, мы вскоре вам позвоним, чтобы уточнить бронь.')
        # q.execute("SELECT * FROM user")
        bot.register_next_step_handler(send, first)
        # q.close()
        # connection.commit()
        # connection.close()

def a1(message):
    if message.text == 'Ⓜ Главное меню':
        first(message)
    else:
        keyboard = types.ReplyKeyboardMarkup(True, False)
        button_phone = types.KeyboardButton(text='Оставить номер', request_contact=True)
        keyboard.add(button_phone)
        keyboard.row('Ⓜ Главное меню')
        send = bot.send_message(message.chat.id, 'Очень приятно, {name}. Оставьте, пожалуйста, Ваш номер телефона:'.format(name=message.text), reply_markup=keyboard)
        bot.register_next_step_handler(send, a2)

def a2(message):
    if message.text == 'Ⓜ Главное меню':
        first(message)
    elif message.contact:
        keyboard = types.ReplyKeyboardMarkup(True, False)
        keyboard.row('Ⓜ Главное меню')
        send = bot.send_message(message.chat.id, 'Укажите адрес доставки:', reply_markup=keyboard)
        bot.register_next_step_handler(send, a3)
    elif message.text:
        send = bot.send_message(message.chat.id, 'Оставьте, пожалуйста, ваш номер телефона.')
        bot.register_next_step_handler(send, a2)

def a3(message):
    if message.text == 'Ⓜ Главное меню':
        first(message)
    elif message.text:
        keyboard = types.ReplyKeyboardMarkup(True, False)
        keyboard.row('1', '2', '3', '4', '5', '6')
        keyboard.row('Больше')
        keyboard.row('Ⓜ Главное меню')
        send = bot.send_message(message.chat.id, 'Укажите количество персон:', reply_markup=keyboard)
        bot.register_next_step_handler(send, a4)

def a4(message):
    if message.text == 'Ⓜ Главное меню':
        first(message)
    elif message.text:
        keyboard = types.ReplyKeyboardMarkup(True, False)
        keyboard.row('Ⓜ Главное меню')
        send = bot.send_message(message.chat.id, 'Если нужно, оставьте комментарий:', reply_markup=keyboard)
        bot.register_next_step_handler(send, a5)

def a5(message):
    if message.text == 'Ⓜ Главное меню':
        first(message)
    elif message.text:
        send = bot.send_message(message.chat.id, 'Спасибо, Держите телефон при себе, оператор свяжется с Вами в ближайшее время для подтверждения заказа.')
        bot.register_next_step_handler(send, first)

bot.polling()