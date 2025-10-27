import telebot
from handlers import register_handlers

bot = telebot.TeleBot("")

# Регистрируем все обработчики
register_handlers(bot)

# Запуск бота
bot.polling(none_stop=True)