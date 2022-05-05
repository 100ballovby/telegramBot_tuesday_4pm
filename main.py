import telebot

bot = telebot.TeleBot('your-key-here')


@bot.message_handler(content_types=['text'])  # учим бота принимать текстовые сообщения
def get_text_messages(message):
    if message.text == 'Привет':
        answer = 'Привет, как я могу помочь?'
        bot.send_message(message.from_user.id, answer)  # отправить_сообщение(кому, что)
    elif message.text == '/help':
        answer = 'Напиши "Привет"'
        bot.send_message(message.from_user.id, answer)
    else:
        answer = 'Я тебя не понимаю!'
        bot.send_message(message.from_user.id, answer)

bot.polling(none_stop=True, interval=0)