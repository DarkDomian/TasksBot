import sqlite3
import telebot
from datetime import date

bot = telebot.TeleBot("5217938630:AAEdkkqc4aGpedu4FRfvmnx9DKgiMIlMJfI")

conn = sqlite3.connect('db/database.db', check_same_thread=False)
cursor = conn.cursor()

def DataBaseVal(user_id: int, date: date, task: str, check: bool):
	cursor.execute('INSERT INTO test (user_id, date, task, check) VALUES (?, ?, ?, ?)', (user_id, date, task, check))
	conn.commit()

HELP = """
help : display a list of available commands and ther function,
add : add a task to the list, writing in format: "/add dd.mm.yyyy task text",
show :  display all tasks,
mark : chose complited task, and mark them,
clear : make your chat purely\n"""

@bot.message_handler(commands=["add"])
def add(message):
    UserID = message.from_user.id
    SplitMessage = message.text.split(maxsplit=2)
    DateFromMess = date.strptime(SplitMessage[1], "%d.%m.%y")  #need use date-format
    TaskFromMess = SplitMessage[2]
    DataBaseVal(user_id=UserID, date=DateFromMess, task=TaskFromMess, check=False)

@bot.message_handler(commands=["show"])
def show(message):
    if message.from_user.id in 

@bot.message_handler(commands=["help"])
def help(message):
    bot.send_message(message.chat.id, HELP)

@bot.message_handler(commands=["clear"])
def clear(message):
    bot.delete_message(message.chat.id, message.message_id)
    bot.send_delete


@bot.message_handler(content_types=['text', 'audio', 'file', 'image'])
def text(message):
    bot.send_message(message.chat.id, "It's beautiful, but what can I say?" )

bot.polling(non_stop=True)