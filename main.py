import randomize
import telebot
from config import TOKEN


def data_preparation():
    users = open("db_users.txt", "r").readlines()
    users = map(lambda x: x.replace("\n", ""), users)
    users = map(int, users)
    first_command, second_command = randomize.sort_for_two_commands(users)
    first_command = randomize.mafia_or_no(first_command)
    second_command = randomize.mafia_or_no(second_command)
    return first_command, second_command


def mailing(first_command, second_command):
    bot = telebot.TeleBot(TOKEN)
    for player_id, player_role in first_command.items():
        bot.send_message(player_id, f"Вы {player_role}")
    #for player_id, player_role in second_command.items():
    #    bot.send_message(player_id, f"Вы {player_role}")
    
    bot.polling(none_stop = True, interval = 0)


if __name__ == "__main__":
    #mailing(data_preparation())
    mailing({709595886:"мафия"}, {})


