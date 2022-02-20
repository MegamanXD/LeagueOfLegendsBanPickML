from riotwatcher import LolWatcher
import csv

api_key = 'RGAPI-6a95ed04-2f44-40f4-b232-2120415d79ed'
watcher = LolWatcher(api_key)
my_region = 'americas'

player_list = []


# region_short_name = ["na1", "euw1", "eun1", "kr", "br1", "jp1", "ru", "oc1", "tr1", "la1", "la2"] ==> not work here !!
# region_long_name = ["europe", "asia", "americas"]
# The reason is because riot changed their APIs but some of methods are still not updated

def get_match_data(region_short_name, region_long_name, name):
    result_list = []
    player = watcher.summoner.by_name(region_short_name, name)
    print('Getting data from player:' + player['name'])
    print()
    player_uuid = player.get("puuid")
    print('Uuid:' + player_uuid)
    player_matches = watcher.match.matchlist_by_puuid(region_long_name, player_uuid)
    for match in player_matches:
        match_detail = watcher.match.by_id(my_region, match)
        match_participants = match_detail['info']['participants']
        player_champ_id = 'NaN'
        player_champ_name = 'NaN'
        player_position = 'NaN'
        player_team = 'NaN'
        is_player_win = False
        for participant in match_participants:
            if participant['puuid'] == player_uuid:
                player_champ_id = participant['championId']
                player_champ_name = participant['championName']
                player_position = participant['teamPosition']
                player_team = participant['teamId']
                is_player_win = participant['win']
        print(name + " used champ id:" + str(player_champ_id) + "\n"
                                                                + " used champ name:" + str(player_champ_name) + "\n"
                                                                "role:" + player_position + "\n"
                                                                                            "team id:" + str(
            player_team))
        ally_champ1 = 'NaN'
        ally_champ2 = 'NaN'
        enemy_champ1 = 'NaN'
        enemy_champ2 = 'NaN'
        ally_champ1_name = 'NaN'
        ally_champ2_name = 'NaN'
        enemy_champ1_name = 'NaN'
        enemy_champ2_name = 'NaN'
        for participant in match_participants:
            if participant['puuid'] != player_uuid:
                if ally_champ1 == 'NaN' and participant['teamId'] == player_team:
                    ally_champ1 = participant['championId']
                    ally_champ1_name = participant['championName']
                if (ally_champ2 == 'NaN' or ally_champ1 == ally_champ2) and participant['teamId'] == player_team:
                    ally_champ2 = participant['championId']
                    ally_champ2_name = participant['championName']
                if enemy_champ1 == 'NaN' and participant['teamId'] != player_team:
                    enemy_champ1 = participant['championId']
                    enemy_champ1_name = participant['championName']
                if (enemy_champ2 == 'NaN' or enemy_champ2 == enemy_champ1) and participant['teamId'] != player_team:
                    enemy_champ2 = participant['championId']
                    enemy_champ2_name = participant['championName']
        print("Ally 1:{0} Name: {1}\nAlly 2:{2} Name: {3}\nEnemy 1:{4} Name: {5}\nEnemy 2:{6} Name: {7}".format(
            ally_champ1, ally_champ1_name, ally_champ2, ally_champ2_name, enemy_champ1, enemy_champ1_name, enemy_champ2,
            enemy_champ2_name))
        print()
        print("Was " + name + " win ? " + str(is_player_win))
        result_list.append(
            [player_champ_id, player_champ_name, player_position, is_player_win, ally_champ1, ally_champ2, enemy_champ1, enemy_champ2])
        print("-----------------------------------------------------------")
    return result_list


# Add "+ get_match_data('na1', 'americas', 'Player Name That you Like')"
list_to_csv = get_match_data('na1', 'americas', 'Doublelift') \
              + get_match_data('na1', 'americas', 'Professor Akali') \
              + get_match_data('na1', 'americas', 'Aconko') \
              + get_match_data('na1', 'americas', 'Sajed2') \
              + get_match_data('na1', 'americas', 'MUSTACHEmanFIGHT') \
              + get_match_data('na1', 'americas', 'Froggen') \
              + get_match_data('na1', 'americas', 'scott joseph') \
              + get_match_data('na1', 'americas', 'raínyday')

print(list_to_csv)

# Write on csv with format below:
# player_champ,player_champ_name,player_position,is_player_win,ally_champ1,ally_champ2,enemy_champ1,enemy_champ2

with open('match-list.csv', 'w') as csvfile:
    writer = csv.writer(csvfile)
    # Because the first row has error so I will put it in another file then add it again
    for row in list_to_csv:
        print(row)
        writer.writerow(row)
