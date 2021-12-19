import telebot

token = '5029500189:AAFBXXZSWdoNWfDJD-m9Cz5FAjBOuuCxFmI'
bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def start_message(message):
    keyboard = telebot.types.ReplyKeyboardMarkup(True)
    keyboard.row('Хорошо', 'Не очень')
    bot.send_message(message.chat.id, 'Привет!Как настроение?', reply_markup=keyboard)


@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text.lower() == 'хорошо':
        bot.send_message(message.chat.id, 'Я очень рад!')
    elif message.text.lower() == 'не очень':
        bot.send_message(message.chat.id, 'Не грусти!')


bot.polling()