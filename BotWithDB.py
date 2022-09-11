from numbers import Real
import sqlite3
import telebot
from datetime import date
import random

bot = telebot.TeleBot("5217938630:AAEdkkqc4aGpedu4FRfvmnx9DKgiMIlMJfI")

conn = sqlite3.connect('db/database.db', check_same_thread=False)
cursor = conn.cursor()

def db_table_val(user_id: int, date: date, task: str, check: Real):
	cursor.execute('INSERT INTO test (user_id, date, task, check) VALUES (?, ?, ?, ?)', (user_id, date, task, check))
	conn.commit()

HELP = """
help : display a list of available commands and ther function,
add : add a task to the list,
show :  display all tasks,
random : crate random task for that day,
clear : make your chat purely\n"""

@bot.message_handler(commands=["help"])
def help(message):
    bot.send_message(message.chat.id, HELP)

@bot.message_handler(commands=["clear"])
def clear(message):
    bot.delete_message(message.chat.id, message.message_id)
    bot.send_delete


bot.polling(non_stop=True)