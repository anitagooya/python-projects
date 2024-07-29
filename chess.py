def players_reader(filename):
    player_csv = {}

    try:
        with open(filename) as player_file:
            data = player_file.readlines()[1:]
    except OSError as error:
        print(error)

    for row in data:
        name, selo = row.strip().split(",")
        player_csv[name] = selo

    return player_csv


def games_reader(filename):
    games_csv = []
    try:
        with open(filename) as game_files:
            data = game_files.readlines()[1:]
    except OSError as error:
        print(error)

    for i in data:
        i = i.strip().split(",")
        games_csv.append(i)
    return games_csv


def wl_maker(game_list):
    winner_list = list()
    looser_list = list()
    draw_list = list()

    for i in game_list:
        first_player = i[0]
        second_player = i[1]
        result = i[2]

        if result == "1-0":
            winner_list.append(first_player)
            looser_list.append(second_player)
        elif result == "0-1":
            winner_list.append(second_player)
            looser_list.append(first_player)
        else:
            draw_list.append(first_player)
            draw_list.append(second_player)

    return winner_list, looser_list, draw_list


def delta(player_1, player_2):
    return 1 / (1 + 2 ** ((player_1 - player_2) / 100))


def scores(winner_list, looser_list, player_dict):
    for winner in winner_list:
        if winner in player_dict:
            for looser in looser_list:
                if looser in player_dict:
                    player_dict[winner] = int(player_dict[winner]) + delta(int(player_dict[winner]),
                                                                           int(player_dict[looser])) * 200
                    player_dict[winner] = int(player_dict[looser]) - delta(int(player_dict[winner]),
                                                                           int(player_dict[looser])) * 200
    return player_dict


def sorter(result_dict):
    res=dict()
    for key in result_dict.keys():
        res[key] = round(result_dict[key])
    new_tuples = sorted(res.items(), key=lambda x: x[1], reverse=True)
    return new_tuples


def main():
    # value = {i for i in dictionary if dictionary[i] == "2804"}
    # print("key by value:", value)
    # --------------------------------#

    players = players_reader("players.csv")
    games = games_reader("games.csv")
    winners, loosers, draws = wl_maker(games)
    results = scores(winners, loosers, players)
    list1=[]
    for i in sorter(results):
         list1.append(i)
    for i in list1:
        print(i[0] , ":" ,i[1])




if __name__ == '__main__':
    main()

