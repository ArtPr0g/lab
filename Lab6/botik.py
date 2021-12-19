import telebot
from telebot import types
import config
import dbworker

# Создание бота
bot = telebot.TeleBot(config.TOKEN)

# Начало диалога
@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, я твой скромный помощник по тикитоку')
    dbworker.set(message.chat.id, config.States.STATE_NAME.value)
    bot.send_message(message.chat.id, 'Как к тебе можно обращаться?')

    # По команде /reset будем сбрасывать состояния, возвращаясь к началу диалога
    @bot.message_handler(commands=['reset'])
    def cmd_reset(message):
        bot.send_message(message.chat.id, 'А я забыла, я забыла, тебя опять, опять, опять...')
        dbworker.set(message.chat.id, config.States.STATE_NAME.value)
        bot.send_message(message.chat.id, 'Как к тебе можно обращаться?')

# Обработка ввода имени
@bot.message_handler(func=lambda message: dbworker.get(message.chat.id) == config.States.STATE_NAME.value)
def user_name(message):
    text = message.text
    if not text.isalpha():
        # Состояние не изменяется, выводится сообщение об ошибке
        bot.send_message(message.chat.id, 'Кажется, ты не ввел имя!')
        return
    else:
        bot.send_message(message.chat.id, f'Приятно познакомиться, {text}')
        # Меняем текущее состояние
        dbworker.set(message.chat.id, config.States.STATE_NAME.value)
        # Сохраняем имя
        dbworker.set((message.chat.id, config.States.STATE_NAME.value), text)
        bot.send_message(message.chat.id, 'Знаю, что такое не прилично спрашивать, но сколько тебе лет?')
        dbworker.set(message.chat.id, config.States.STATE_AGE.value)

# Обработка вызраста
@bot.message_handler(func=lambda message: dbworker.get(message.chat.id) == config.States.STATE_AGE.value)
def user_age(message):
    text = message.text
    if not text.isdigit():
        # Состояние не изменяется, выводится сообщение об ошибке
        bot.send_message(message.chat.id, 'Кажется, это не число')
        return
    else:
        bot.send_message(message.chat.id, f'Супер, {text}, значит {text}')
        # Меняем текущее состояние
        dbworker.set(message.chat.id, config.States.STATE_OPERATION.value)
        # Сохраняем число
        dbworker.set((message.chat.id, config.States.STATE_AGE.value), text)
        markup = types.ReplyKeyboardMarkup(row_width=2)
        itembtn1 = types.KeyboardButton('Получить тики-ток от меня')
        itembtn2 = types.KeyboardButton('Поделиться тики-током со мной')
        markup.add(itembtn1, itembtn2)
        bot.send_message(message.chat.id, 'Выберите, пожалуйста, чтобы ты хотел сделать', reply_markup=markup)

# Выбор действия
@bot.message_handler(func=lambda message: dbworker.get(message.chat.id) == config.States.STATE_OPERATION.value)
def operation(message):
    # Текущее действие
    op = message.text

    if op == 'Получить тики-ток от меня':
        bot.send_message(message.chat.id,
                         "https://www.tiktok.com/@adrian_balu/video/7039550606817692934?is_copy_url=1&is_from_webapp=v1")
        bot.send_message(message.chat.id,
                         "Наслаждайся! Если захочешь пообщаться снова - "
                         "отправь команду /start.")
    elif op == 'Поделиться тики-током со мной':
        bot.send_message(message.chat.id,
                         "Что ж, я весь в предвкушении..."
                         "Но только я не настолько хорош, чтобы переходить по ссылкам, поэтому пришли его обычным видио)))")

        @bot.message_handler(content_types=["video"], func=lambda message: dbworker.get(message.chat.id) == config.States.STATE_OPERATION.value)
        def user_video(message):

            bot.send_message(message.chat.id, "Вау, это прекрасно!!!")
            bot.send_message(message.chat.id,
                             "С тобой очень приятно иметь дело. Если захочешь пообщаться снова - "
                             "отправь команду /start.")
            dbworker.set(message.chat.id, config.States.STATE_START.value)



if __name__ == '__main__':
    bot.infinity_polling()
