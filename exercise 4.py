import telebot

token='2116981405:AAHjvzABeFTSHErDFJXi2Q47PukDvuk6HiM'
bot = telebot.TeleBot(token)

letters_ = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

@bot.message_handler(content_types=["text"])
def repeat_all_messages(message):
    str_=message.text
    k = 0
    for i in str_:
        if i in letters_:
            k+=1

    bot.send_message(message.chat.id, text=f'Количество гласных в вашем слове {k}')

bot.infinity_polling()