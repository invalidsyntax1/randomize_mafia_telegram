#распределение на 2 команды

from random import randint


def sort_for_two_commands(players: list) -> list:
    first_len_players_command = len(players) / 2
    first_command = []
    while len(players) != first_len_players_command:
        index_random_player = randint(0, len(players)-1)
        random_player = players[index_random_player]
        first_command.append(random_player)
        del players[index_random_player]
    second_command = players
    return first_command, second_command


def mafia_or_no(players_in_command, roles = ["мирный житель","мирный житель","мирный житель","мафия"]):
    player_and_role = dict()
    for player in players_in_command:
        random_index_role = randint(0, len(roles)-1)
        player_and_role[player] = roles[random_index_role]
        del roles[random_index_role]
    return player_and_role


#tests
if __name__ == "__main__":
    print(sort_for_two_commands([1,2,3,4,5,6,7,8]))
    print(mafia_or_no([856567, 634534, 454534, 354634]))