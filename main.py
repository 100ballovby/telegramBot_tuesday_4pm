import telebot
import requests as r
from telebot import types


bot = telebot.TeleBot('')


@bot.message_handler(commands=['start', 'help'])
def start(message):
    with open('texts/hello.txt', encoding='utf8') as file:
        greeting = file.read()
    bot.send_message(message.chat.id, greeting)


@bot.message_handler(commands=['convert'])
def convert(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('Курсы валют📈')
    btn2 = types.KeyboardButton('Обмен валют💱')
    markup.add(btn1)
    markup.add(btn2)
    bot.send_message(message.chat.id, 'Выберите', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def button_reply(message):
    if message.text == 'Курсы валют📈':
        bot.send_message(message.chat.id, 'Курсы валют')
    elif message.text == 'Обмен валют💱':
        bot.send_message(message.chat.id, 'Напишите валюту в которую нужно переводить')

bot.polling(none_stop=True, interval=0)
