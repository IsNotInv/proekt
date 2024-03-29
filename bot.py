from threading import Thread
import telebot
from telebot import types
import schedule
import time
import datetime


token = '5178976057:AAGC4qow2nJyxLXkORXQSzGiY3j70OC3VdQ'
bot = telebot.TeleBot(token)



@bot.message_handler(content_types=['text'])



def get_text_messages(message):
    sched = """ 
    1 урок - |08:30 - 09:10|
    2 урок - |09:30 - 10:10| 
    3 урок - |10:30 - 11:10|
    4 урок - |11:25 - 12:05|
    5 урок - |12:15 - 12:55|
    6 урок - |13:15 - 13:55|
    7 урок - |14:10 - 14:50|
    """

    if message.text == "/start":
        bot.send_message(message.from_user.id, 'Привет! Это телеграмм чат-бот, который помогает следить за звонками и не опаздывать на уроки.')
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        buttons = ["Расписание", "Подключение оповещений"]
        keyboard.add(*buttons)
        bot.send_message(message.chat.id,'Выберите, что Вам нужно:', reply_markup=keyboard)
    if message.text == 'Расписание':
        bot.send_message(message.chat.id, '' + sched)

    def text():
        bot.send_message(message.from_user.id, 'Звонок через 5 минут')
    if message.text == 'Подключение оповещений':
        bot.send_message(message.from_user.id, 'Оповещения подключены')
        if date_checker() == True:
            schedule.every().day.at('08:25').do(text)
            schedule.every().day.at('09:05').do(text)
            schedule.every().day.at('09:25').do(text)
            schedule.every().day.at('10:05').do(text)
            schedule.every().day.at('10:25').do(text)
            schedule.every().day.at('11:05').do(text)
            schedule.every().day.at('11:20').do(text)
            schedule.every().day.at('12:00').do(text)
            schedule.every().day.at('12:10').do(text)
            schedule.every().day.at('12:50').do(text)
            schedule.every().day.at('13:10').do(text)
            schedule.every().day.at('13:50').do(text)
            schedule.every().day.at('14:05').do(text)
            schedule.every().day.at('14:45').do(text)
        Thread(target=schedule_checker).start()
        Thread(target=date_checker).start()


def date_checker():
    while int(datetime.datetime.today().isoweekday()) != 6 and int(datetime.datetime.today().isoweekday()) != 7:
        return True

def schedule_checker():
    while True:
        schedule.run_pending()
        time.sleep(10)








bot.infinity_polling()
