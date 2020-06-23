import telebot

STICKER_NAME = 'CAACAgIAAxkBAAMwXvH1cIa8GSty_WIzjy8OZbrFLUcAAt0AA_cCyA_qWS-8p2pAPBoE'
TOKEN_NAME = '1220261783:AAFdptfz_Pofp-HGp7YqfUYlBgHhpAG3Do0'

bot = telebot.TeleBot(TOKEN_NAME)
keyboards = telebot.types.ReplyKeyboardMarkup(True, True)
keyboards.row('привет', 'ПРИВЕТ', '/start')


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, ты написал мнe', reply_markup=keyboards)


@bot.message_handler(content_types='text')
def write_message(message):
    if message.text.lower() == 'привет':
        bot.send_message(message.chat.id, 'Привет, мой создатель')
    elif message.text.lower() == 'пока':
        bot.send_message(message.chat.id, 'Прощай, мой создатель')


@bot.message_handler(content_types=['sticker'])
def sticker_id(message):
    print(message)


bot.polling(none_stop=True)
