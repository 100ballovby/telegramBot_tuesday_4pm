import telebot
import requests as r

bot = telebot.TeleBot('')


@bot.message_handler(commands=['start', 'help'])
def start(message):
    with open('texts/hello.txt', encoding='utf8') as file:
        greeting = file.read()
    bot.send_message(message.chat.id, greeting)


bot.polling(none_stop=True, interval=0)
