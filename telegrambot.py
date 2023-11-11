import telebot
from telebot import apihelper
import time
import os
from main import hhapi

TOKEN = '6883888987:AAHLGCTTvwRXTclWXfSbFXFrcuT4djDw2gQ'

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, f"Здравствуйте, {message.from_user.first_name}!!")
    #print(message)
    #print(message.from_user.first_name)

@bot.message_handler(commands=['hh'])
def send_welcome(message):
    zapros = str(message.text.replace('/hh ', ''))
    bot.reply_to(message, f"{message.from_user.first_name}, Ваш запрос обрабатывается...")
    hhapi(zapros)
    with open('output.txt', 'rb') as data:
        bot.send_document(message.chat.id, data)

@bot.message_handler(content_types=['text'])
def textindef(message):
    hhapi(message.text)
    with open('output.txt', 'rb') as data:
        bot.send_document(message.chat.id, data)
bot.polling()