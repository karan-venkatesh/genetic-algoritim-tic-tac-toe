from cgitb import reset
from game_board import GameBoard
from player import Player
from match_controller import MatchController
import random

DEBUG = False

PLAYER_PER_GEN = 100

PLAYERS_TO_SELECT = 10

NUMBER_OF_GEN = 50

MATCHES_PER_GEN = 30

MATCH_RESULT = {
    1: 'PLAYER 1 WINS',
    -1: 'PLAYER 2 WINS',
    0: 'MATCH DRAW'
}

if __name__ == '__main__':
    match_controller = MatchController()
    player_list = [Player() for _ in range(PLAYER_PER_GEN)]

    
    for _ in range(NUMBER_OF_GEN):
        player_score = {i:0 for i in range(PLAYER_PER_GEN)}
        
        for _ in range(MATCHES_PER_GEN):
            player_index_list = [i for i in range(PLAYER_PER_GEN)]
            while len(player_index_list)>=2:
                player_1_id = player_index_list[random.randint(0,len(player_index_list)-1)]
                player_index_list.remove(player_1_id)

                result = match_controller.play_match(player_list[player_1_id],None)
                if DEBUG: print('Player ',player_1_id,' vs Player BOT : ',MATCH_RESULT[result])
                player_score[player_1_id] += result

        selected_players = [top_player_id for top_player_id, _ in sorted(player_score.items(), key=lambda item: item[1])][-PLAYERS_TO_SELECT:]
        player_list = [Player(player_list[selected_players[index % PLAYERS_TO_SELECT]].logic) for index in range(PLAYER_PER_GEN)]




    print({top_player_id:score for top_player_id, score in sorted(player_score.items(), key=lambda item: item[1])})
    best_player = sorted(player_score.items(), key=lambda item: item[1])[-1]
    print(player_list[best_player[0]])

    match_controller.manual_match(player_list[best_player[0]],play_first = False)
    match_controller.manual_match(player_list[best_player[0]],play_first = True)
    match_controller.manual_match(player_list[best_player[0]],play_first = False)
    match_controller.manual_match(player_list[best_player[0]],play_first = True)
    match_controller.manual_match(player_list[best_player[0]],play_first = False)

# if __name__ == '__main__':
#     match_controller = MatchController()
#     player_list = [Player() for _ in range(PLAYER_PER_GEN)]

    
#     for _ in range(NUMBER_OF_GEN):
#         player_score = {i:0 for i in range(PLAYER_PER_GEN)}
        
#         for _ in range(MATCHES_PER_GEN):
#             player_index_list = [i for i in range(PLAYER_PER_GEN)]
#             while len(player_index_list)>=2:
#                 player_1_id = player_index_list[random.randint(0,len(player_index_list)-1)]
#                 player_index_list.remove(player_1_id)
                
#                 player_2_id = player_index_list[random.randint(0,len(player_index_list)-1)]
#                 player_index_list.remove(player_2_id)

#                 result = match_controller.play_match(player_list[player_1_id],player_list[player_2_id])
#                 if DEBUG: print('Player ',player_1_id,' vs Player ',player_2_id,' : ',MATCH_RESULT[result])
#                 player_score[player_1_id] += result
#                 player_score[player_2_id] -= result

#         selected_players = [top_player_id for top_player_id, _ in sorted(player_score.items(), key=lambda item: item[1])][-PLAYERS_TO_SELECT:]
#         player_list = [Player(player_list[selected_players[index % PLAYERS_TO_SELECT]].logic) for index in range(PLAYER_PER_GEN)]




#     print({top_player_id:score for top_player_id, score in sorted(player_score.items(), key=lambda item: item[1])})
#     best_player = sorted(player_score.items(), key=lambda item: item[1])[-1]
#     print(player_list[best_player[0]])

#     match_controller.manual_match(player_list[best_player[0]],play_first = False)
#     match_controller.manual_match(player_list[best_player[0]],play_first = True)
#     match_controller.manual_match(player_list[best_player[0]],play_first = False)
#     match_controller.manual_match(player_list[best_player[0]],play_first = True)
#     match_controller.manual_match(player_list[best_player[0]],play_first = False)

