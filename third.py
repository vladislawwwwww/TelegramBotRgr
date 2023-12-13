import telebot
from telebot import types

TOKEN = "6727488426:AAE-5RQIl4gWC4pa5IVu0gvLoaJB4edPdeE"
bot = telebot.TeleBot(TOKEN)


keyboard = types.InlineKeyboardMarkup(row_width=2)
BPMN_button = types.InlineKeyboardButton('Диаграмма BPMN', callback_data='bpmn')
dashboard_button = types.InlineKeyboardButton('Дашборд', callback_data='dashboard')
help_button = types.InlineKeyboardButton('Помощь', callback_data='help')
creator_button = types.InlineKeyboardButton('Создатель', callback_data='creator')
keyboard.add(BPMN_button, help_button, dashboard_button, creator_button)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, 'Привет! Это бот телеграм. Выберите команду', reply_markup=keyboard)

@bot.message_handler(func=lambda message: True)
def home_screen(message):
    if message.text == 'Диаграмма BPMN':
        #bot.reply_to(message, 'Здесь надо что-то написать про BPMN и показать диаграмму')
        bpmn_markup = types.InlineKeyboardMarkup(row_width=1)
        button9 = types.InlineKeyboardButton('Описание BPMN', callback_data='bpmn_function1')
        button10 = types.InlineKeyboardButton('Ссылка на диаграмму', callback_data='bpmn_function2')
        bpmn_markup.add(button9, button10)
        bot.send_message(message.chat.id, 'Выберите действие:', reply_markup=bpmn_markup)
    elif message.text == 'Создатель':
        bot.reply_to(message, 'Владислав 2ИБ-1')
    elif message.text == 'Дашборд':
        dashboard_markup = types.InlineKeyboardMarkup(row_width=1)
        button1 = types.InlineKeyboardButton('Описание дашборда', callback_data='dashboard_function1')
        button2 = types.InlineKeyboardButton('Ссылка на GitHub', callback_data='dashboard_function2')
        dashboard_markup.add(button1, button2)
        bot.send_message(message.chat.id, 'Выберите действие:', reply_markup=dashboard_markup)
    elif message.text == 'Помощь':
        bot.reply_to(message, 'Привет! Это бот телеграм. Выберите команду')
    else:
        bot.reply_to(message, 'Не понимаю', reply_markup=keyboard)

@bot.callback_query_handler(func=lambda call: True)
def callback_handler(call):
    #кнопки BPMN
    if call.data == 'bpmn':
        pass
    #текстовое описание bpmn
    elif call.data == 'bpmn_function1':
        bot.send_message(call.message.chat.id,
                         'Диаграммы BPMN (Business Process Model and Notation) представляют собой стандартный '
                         'графический язык, разработанный для моделирования бизнес-процессов в организации. '
                         'Этот инструмент обеспечивает единый и понятный способ визуализации бизнес-процессов, '
                         'что помогает более эффективно понимать, анализировать и оптимизировать деятельность компании')

        bpmn_function_markup = types.InlineKeyboardMarkup(row_width=1)

        button11 = types.InlineKeyboardButton('Кнопка 1', callback_data='bpmn_function3')
        button12 = types.InlineKeyboardButton('Кнопка 2', callback_data='bpmn_function4')

        bpmn_function_markup.add(button11, button12)
        bot.send_message(call.message.chat.id, 'Выберите действие:', reply_markup=bpmn_function_markup)

    elif call.data == 'bpmn_function2':
        bot.send_message(call.message.chat.id, 'Ссылка на диаграмму: https://lucid.app/users/registerOrLogin/free?showLogin=false&invitationId=inv_'
                                               'cbccaf51-8132-410a-ac55-685a8529e396&productOpt=chart&invitationType=documentAcceptance&returnUrlOverride='
                                               '%2Flucidchart%2Fd0a8d047-4837-4c88-afad-50bf218fd1c8%2Fedit%3Fviewport_loc%3D-836%252C-242%252C3700%252C1817'
                                               '%252CtFvMj0YbrJai%26invitationId%3Dinv_cbccaf51-8132-410a-ac55-685a8529e396')
    elif call.data == 'bpmn_function3':
        bot.send_message(call.message.chat.id, 'текст1')
    elif call.data == 'bpmn_function4':
        bot.send_message(call.message.chat.id, 'текст2')

        #кнопки дашборда
    elif call.data == 'dashboard':
        pass
    elif call.data == 'dashboard_function1':
        bot.send_message(call.message.chat.id, 'Дашборд предназначен для визуализации и анализа данных о здоровье и медицинских показателях. '
                                               'Содержит пять ключевых графиков, предоставляющих информацию о различных аспектах пациентского здоровья.')

        dashboard_function_markup = types.InlineKeyboardMarkup(row_width=1)

        button3 = types.InlineKeyboardButton('График 1', callback_data='dashboard_function3')
        button4 = types.InlineKeyboardButton('График 2', callback_data='dashboard_function4')
        button5 = types.InlineKeyboardButton('График 3', callback_data='dashboard_function5')
        button6 = types.InlineKeyboardButton('График 4', callback_data='dashboard_function6')
        button7 = types.InlineKeyboardButton('График 5', callback_data='dashboard_function7')
        button8 = types.InlineKeyboardButton('Таблица', callback_data='dashboard_function8')
        dashboard_function_markup.add(button3, button4, button5, button6, button7, button8)
        bot.send_message(call.message.chat.id, 'Выберите график:', reply_markup=dashboard_function_markup)

    elif call.data == 'dashboard_function2':
        bot.send_message(call.message.chat.id, 'Ссылка на GitHub: https://github.com/vladislawwwwww/Dashboardd')
    elif call.data == 'dashboard_function3':
        image1_url = 'https://raw.githubusercontent.com/vladislawwwwww/TelegramBotRgr/development/graphik1.jpg'
        bot.send_photo(call.message.chat.id, image1_url, caption='Это точечный график')
    elif call.data == 'dashboard_function4':
        image2_url = 'https://raw.githubusercontent.com/vladislawwwwww/TelegramBotRgr/development/graphik2.jpg'
        bot.send_photo(call.message.chat.id, image2_url, caption='Это столбчатый график')
    elif call.data == 'dashboard_function5':
        image3_url = 'https://raw.githubusercontent.com/vladislawwwwww/TelegramBotRgr/development/graphik3.jpg'
        bot.send_photo(call.message.chat.id, image3_url, caption='Это круговой график')
    elif call.data == 'dashboard_function6':
        image4_url = 'https://raw.githubusercontent.com/vladislawwwwww/TelegramBotRgr/development/graphik4.jpg'
        bot.send_photo(call.message.chat.id, image4_url, caption='Это линейный график')
    elif call.data == 'dashboard_function7':
        image5_url = 'https://raw.githubusercontent.com/vladislawwwwww/TelegramBotRgr/development/graphik5.jpg'
        bot.send_photo(call.message.chat.id, image5_url, caption='Это ящичковый график')
    elif call.data == 'dashboard_function8':
        image6_url = 'https://raw.githubusercontent.com/vladislawwwwww/TelegramBotRgr/development/table1.jpg'
        bot.send_photo(call.message.chat.id, image6_url, caption='Это таблица')

bot.infinity_polling()