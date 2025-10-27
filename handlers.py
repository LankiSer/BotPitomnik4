from keyboards import main_menu, breeds_menu
from data import cats, dogs
from telebot import teleBot


def register_handlers(bot: teleBot):
    @bot.message_handler(commands=['start'])
    def start(message):
        bot.send_message(message.chat.id, 'Добро пожаловать в питомник! Выберите животное:',
                         reply_markup=main_menu())

    @bot.message_handler(func=lambda message: message.text == 'Кошки')
    def show_cats(message):
        bot.send_message(message.chat.id, 'Выберите породу кошки:',
                         reply_markup=breeds_menu(cats.keys()))

    @bot.message_handler(func=lambda message: message.text == 'Собаки')
    def show_dogs(message):
        bot.send_message(message.chat.id, 'Выберите породу собаки:',
                         reply_markup=breeds_menu(dogs.keys()))

    @bot.message_handler(func=lambda message: message.text in cats.keys())
    def show_cat_info(message):
        breed = message.text
        description = cats[breed]
        bot.send_message(message.chat.id, f'{breed}:\n\n{description}')

    @bot.message_handler(func=lambda message: message.text in dogs.keys())
    def show_dog_info(message):
        breed = message.text
        description = dogs[breed]
        bot.send_message(message.chat.id, f'{breed}:\n\n{description}')

    @bot.message_handler(func=lambda message: message.text == 'Назад')
    def back(message):
        bot.send_message(message.chat.id, 'Выберите животное:',
                         reply_markup=main_menu())