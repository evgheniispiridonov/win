import telebot
from telebot import types
import os


API_TOKEN = '871426689:AAHjCbL5mmk_NyJWj9G_OhQxUjf1-T-jMzU'

bot = telebot.TeleBot(API_TOKEN)




markup_inline_url2 = types.InlineKeyboardMarkup()
btn_in_url2 = types.InlineKeyboardButton('Права и обязанности сторон', url='https://note-pad.net/ru/read/fd3d573508e0c70d56cb3490ae25c147?page=1')
markup_inline_url2.add(btn_in_url2)


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
 print(message)
 bot.send_message(message.chat.id, "*ДdfdfF4B1*                                                             "
                                   "\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796                                                "
                                   "Обменdsfgdsgsdfgel.                                                          "
                                   "\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796\U00002796                                                "
                                   "Выберите подходящий пункт меню: ", parse_mode="Markdown")
def main():
    port = os.getenv('PORT', default=8000)
    updater.start_webhook(port=port)

@bot.message_handler(func=lambda message: True)
def echo_all(message):
 print(message)
 if message.text == "Оdfgd5":
  bot.send_message(message.chat.id, "fgdgdfdg")




bot.polling(none_stop=True)

