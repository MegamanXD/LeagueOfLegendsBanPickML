from riotwatcher import LolWatcher
import csv

api_key = 'RGAPI-d4cd1ee0-792a-40b5-a23d-a95607879a20'
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
              + get_match_data('na1', 'americas', 'raínyday') \
              + get_match_data('na1', 'americas', 'Mérthos') \
              + get_match_data('na1', 'americas', 'Kross') \
              + get_match_data('na1', 'americas', 'lightrocket2') \
              + get_match_data('na1', 'americas', 'Xehru') \
              + get_match_data('na1', 'americas', 'ttv Doglightning') \
              + get_match_data('na1', 'americas', 'MAMMOTHMAN65') \
              + get_match_data('na1', 'americas', 'CanOfB3ans') \
              + get_match_data('na1', 'americas', 'Raveydemon') \
              + get_match_data('na1', 'americas', 'TTV vsekai') \
              + get_match_data('na1', 'americas', 'Viet Conq Heimer') \
              + get_match_data('na1', 'americas', 'Sweaty Intern') \
              + get_match_data('na1', 'americas', 'DiaKs') \
              + get_match_data('na1', 'americas', 'Suddy') \
              + get_match_data('na1', 'americas', 'Cypher 7') \
              + get_match_data('na1', 'americas', 'Biker Man 420') \
              + get_match_data('na1', 'americas', 'Willie fkn P') \
              + get_match_data('na1', 'americas', 'Fąng') \
              + get_match_data('na1', 'americas', 'DRMARIO94') \
              + get_match_data('na1', 'americas', 'Citric') \
              + get_match_data('na1', 'americas', 'ScottsYorick') \
              + get_match_data('na1', 'americas', 'Sìnax') \
              + get_match_data('na1', 'americas', 'Yuriyumilol') \
              + get_match_data('na1', 'americas', 'Clean Kev') \
              + get_match_data('na1', 'americas', 'hooligan on rift') \
              + get_match_data('na1', 'americas', 'quantumfan') \
              + get_match_data('na1', 'americas', 'NewFruit') \
              + get_match_data('na1', 'americas', 'RAMbo10') \
              + get_match_data('na1', 'americas', 'JUG GOD1') \
              + get_match_data('na1', 'americas', 'Qube') \
              + get_match_data('na1', 'americas', 'BenTbeyondrepair') \
              + get_match_data('na1', 'americas', 'U Say Ur Horse') \
              + get_match_data('na1', 'americas', 'King Kog') \
              + get_match_data('na1', 'americas', 'Plizak') \
              + get_match_data('na1', 'americas', 'th eggsalad') \
              + get_match_data('na1', 'americas', 'ˆAgarPro ˆ') \
              + get_match_data('na1', 'americas', 'Spećtra') \
              + get_match_data('na1', 'americas', 'Dua Lissa NYC') \
              + get_match_data('na1', 'americas', 'zyra þorn') \
              + get_match_data('na1', 'americas', 'Slaleph') \
              + get_match_data('na1', 'americas', 'CheeseLeaguer') \
              + get_match_data('na1', 'americas', 'The 25th Justin') \
              + get_match_data('na1', 'americas', 'o fafa o') \
              + get_match_data('na1', 'americas', 'CIoak and Dagger') \
              + get_match_data('na1', 'americas', 'FateFalls Live') \
              + get_match_data('na1', 'americas', 'Màmamoo') \
              + get_match_data('na1', 'americas', 'Neversaw') \
              + get_match_data('na1', 'americas', 'Mouten') \
              + get_match_data('na1', 'americas', 'Jurassiq') \
              + get_match_data('na1', 'americas', 'Arctic Myths') \
              + get_match_data('na1', 'americas', 'Maja') \
              + get_match_data('na1', 'americas', 'TTV beefyy') \
              + get_match_data('na1', 'americas', 'Fishlord') \
              + get_match_data('na1', 'americas', 'PAlNTHEON') \
              + get_match_data('na1', 'americas', 'BatVayne') \
              + get_match_data('na1', 'americas', 'PIant based') \
              + get_match_data('na1', 'americas', 'Corgi the Pig') \
              + get_match_data('na1', 'americas', 'SkiTzee') \
              + get_match_data('na1', 'americas', 'Tempos Time') \
              + get_match_data('na1', 'americas', 'Sepeku AW') \
              + get_match_data('na1', 'americas', 'Mundologist') \
              + get_match_data('na1', 'americas', 'Łightshield') \
              + get_match_data('na1', 'americas', 'scoobyy') \
              + get_match_data('na1', 'americas', 'STRONGSIDE HERO') \
              + get_match_data('na1', 'americas', 'swordyshield') \
              + get_match_data('na1', 'americas', 'ydbpmdxnh') \
              + get_match_data('na1', 'americas', 'Le Gom') \
              + get_match_data('na1', 'americas', 'Lazy Lambo') \
              + get_match_data('na1', 'americas', 'koôgi') \
              + get_match_data('na1', 'americas', 'ID ToT') \
              + get_match_data('na1', 'americas', '8120830219') \
              + get_match_data('na1', 'americas', 'Eric1') \
              + get_match_data('na1', 'americas', 'Kaizer Morde') \
              + get_match_data('na1', 'americas', 'AquaÐog') \
              + get_match_data('na1', 'americas', 'DevilUnikorn') \
              + get_match_data('na1', 'americas', 'KKYY') \
              + get_match_data('na1', 'americas', 'devalasd') \
              + get_match_data('na1', 'americas', 'Kai Lunari') \
              + get_match_data('na1', 'americas', 'The Master Yeezy') \
              + get_match_data('na1', 'americas', 'KOREA CURRY') \
              + get_match_data('na1', 'americas', 'Singleton') \
              + get_match_data('na1', 'americas', 'SHEEP123') \
              + get_match_data('na1', 'americas', 'Bleeeeeeeeeeeeep') \
              + get_match_data('na1', 'americas', 'Thad') \
              + get_match_data('na1', 'americas', 'Bonedoc27') \
              + get_match_data('na1', 'americas', 'DeepFukingValue') \
              + get_match_data('na1', 'americas', '1Shen') \
              + get_match_data('na1', 'americas', 'MateoDeItalia') \
              + get_match_data('na1', 'americas', 'BCBG') \
              + get_match_data('na1', 'americas', 'MrIpeeFreely') \
              + get_match_data('na1', 'americas', 'Secillia TwTv') \
              + get_match_data('na1', 'americas', 'Survivinq') \
              + get_match_data('na1', 'americas', 'griffinsofneph') \
              + get_match_data('na1', 'americas', 'Doaenel') \
              + get_match_data('na1', 'americas', 'Tha Artist') \
              + get_match_data('na1', 'americas', 'PositivePower')

print(list_to_csv)

# Write on csv with format below:
# player_champ,player_champ_name,player_position,is_player_win,ally_champ1,ally_champ2,enemy_champ1,enemy_champ2

with open('match-list.csv', 'w') as csvfile:
    writer = csv.writer(csvfile)
    # Because the first row has error so I will put it in another file then add it again
    for row in list_to_csv:
        print(row)
        writer.writerow(row)
