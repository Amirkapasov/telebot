from telebot import types
from parsing import last_news
from parsing import news
import telebot

bot = telebot.TeleBot(token='6179654095:AAGVixhDs2y77DpktKJNLZrAPyCtyh1fM30')

@bot.message_handler (commands= ['start'])
def start(message):
    user_id = message.chat.id
    welcome_message = 'Приветствую, меня зовут Bot! Чем могу помочь?\n'
    available_commands = '/start - Начать\n/help - Помощь'
    bot.send_message(user_id, welcome_message + available_commands)

@bot.message_handler(commands=['help'])
def help(message):
    user_id = message.chat.id
    help_text = "Выберите действие:"
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    button1 = types.KeyboardButton ("узнать новости")
    button2 = types.KeyboardButton("узнать погоду")
    button3 = types.KeyboardButton ("привет")
    markup.row(button1, button2)
    markup.row(button3)
    bot.send_message(user_id, help_text, reply_markup = markup)

@bot.message_handler (func = lambda message: True)
def text_message_handler (message):
    user_id = message.chat.id
    text = message.text
    if str(text).lower() == "привет":
        bot.send_message(user_id,"я занят !")
    if str(text).lower() == "узнать погоду":
        bot.send_message(user_id, last_news())
    if str(text).lower() == "узнать новости":
        bot.send_message(user_id, news())
    else:
        bot.send_message(user_id, "здорова сначала !")
bot.polling (none_stop=True)