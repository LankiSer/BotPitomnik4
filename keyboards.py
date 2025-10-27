import telebot

def main_menu():
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = telebot.types.KeyboardButton('Кошки')
    btn2 = telebot.types.KeyboardButton('Собаки')
    markup.add(btn1, btn2)
    return markup

def breeds_menu(breeds_list):
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    for breed in breeds_list:
        markup.add(telebot.types.KeyboardButton(breed))
    markup.add(telebot.types.KeyboardButton('Назад'))
    return markup