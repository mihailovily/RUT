import os
from telebot import types
import telebot
from music import yamusic


token = open('tokens/telegram.txt').readline()
bot = telebot.TeleBot(token)  # инит


@bot.message_handler(commands=['start', 'help'])  # старт
def send_welcome(message):
    usr_id = str(message.from_user.id)  # userid
    usr_name = str(message.from_user.first_name)  # имя юзера
    keyboard = types.ReplyKeyboardMarkup(True)  # генерируем клаву
    butt_music = types.KeyboardButton(text='YandexMusic')
    butt_YT = types.KeyboardButton(text='YouTube')
    butt_magnet = types.KeyboardButton(text='Magnet link')
    keyboard.add(butt_music, butt_YT, butt_magnet)
    bot.reply_to(message, "Hello, " + str(message.from_user.first_name), reply_markup=keyboard)  # здороваемся
    bot.reply_to(message, "You can send me link to any YouTube video, YandexMusic song or magnet-link and I'll send you file. Author: @mihailovily")


@bot.message_handler(commands=['music'])
@bot.message_handler(regexp="YandexMusic")
def find_music(message):
    bot.reply_to(message, "I'm waiting your link to YM")
    bot.register_next_step_handler(message, send_music)
    # кушаем ответ, пихаем в след функцию

def send_music(message):
    usr_id = str(message.from_user.id)
    title, performer = yamusic.track_dl(message.text).split(' - ')
    audio = open('track.mp3', 'rb')
    bot.send_audio(usr_id, audio, performer=performer, title=title)


@bot.message_handler(commands=['video'])
@bot.message_handler(regexp="YouTube")
def find_music(message):
    bot.reply_to(message, "I'm waiting your link to YouTube")
    bot.register_next_step_handler(message, send_yt)

def send_yt(message):
    usr_id = str(message.from_user.id)
    bot.send_message(usr_id, 'YouTube is under constructon')


@bot.message_handler(commands=['magnet'])
@bot.message_handler(regexp="Magnet link")
def find_music(message):
    bot.reply_to(message, "I'm waiting your magnet link")
    bot.register_next_step_handler(message, send_torrent)

def send_torrent(message):
    usr_id = str(message.from_user.id)
    bot.send_message(usr_id, 'Torrents are under constructon')

# если сообщение не распознано
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, "I didn't understand you. Try again please")


if __name__ == '__main__':
    bot.infinity_polling()
