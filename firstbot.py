import telebot
from telebot import types


TOKEN = "6727488426:AAE-5RQIl4gWC4pa5IVu0gvLoaJB4edPdeE"
bot = telebot.TeleBot(TOKEN)


keyboard = types.ReplyKeyboardMarkup(row_width=2)
BPMN_button = types.KeyboardButton('Диаграмма BPMN')
dashboard_button = types.KeyboardButton('Дашборд')
help_button = types.KeyboardButton('Помощь')
creator_button = types.KeyboardButton('Создатель')
keyboard.add(BPMN_button, help_button, dashboard_button, creator_button)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, 'Привет! Это бот телеграм. Выберите команду', reply_markup=keyboard)

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    if message.text == 'Диаграмма BPMN':
        bot.reply_to(message, 'текст про BPMN ')
    elif message.text == 'Создатель':
        bot.reply_to(message, 'Владислав')
    elif message.text == 'Дашборд':
        bot.reply_to(message, 'Текст про дашборд ')
    elif message.text == 'Помощь':
        bot.reply_to(message, 'Привет! Это бот телеграм. Выберите команду')
    else:
        bot.reply_to(message, 'Не понимаю', reply_markup=keyboard)

bot.infinity_polling()