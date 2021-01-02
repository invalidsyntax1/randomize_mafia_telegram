# сбор всех пользователей с телеграмма, кто будет участвовать
import telebot
from config import TOKEN





bot = telebot.TeleBot(TOKEN)


@bot.message_handler(content_types = ['text'])
def get_text_messages(message):
    usr_id = message.from_user.id
    usr_id = str(usr_id)
    db_users = open("db_users.txt", "a")
    db_users_in_text = open("db_users.txt", "r").readlines()
    
    if usr_id + "\n" not in db_users_in_text:
        db_users.write(usr_id)
        db_users.write("\n")
    db_users.close()



bot.polling(none_stop = True, interval = 0)
