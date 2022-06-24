from cgitb import reset
from game_board import GameBoard
from player import Player
from match_controller import MatchController
import random

DEBUG = False

PLAYER_PER_GEN = 100

PLAYERS_TO_SELECT = 10

NUMBER_OF_GEN = 100

MATCHES_PER_GEN = 30

MATCH_RESULT = {
    1: 'PLAYER 1 WINS',
    -1: 'PLAYER 2 WINS',
    0: 'MATCH DRAW'
}



def random_opponents():
    match_controller = MatchController()
    player_list = [Player() for _ in range(PLAYER_PER_GEN)]
    selected_players = None
    
    for _ in range(NUMBER_OF_GEN):
        if selected_players: player_list = [Player(selected_players[index % PLAYERS_TO_SELECT].logic) for index in range(PLAYER_PER_GEN)]

        player_score = {i:0 for i in range(PLAYER_PER_GEN)}
        
        for _ in range(MATCHES_PER_GEN):
            player_index_list = [i for i in range(PLAYER_PER_GEN)]
            while len(player_index_list)>=2:
                player_1_id = player_index_list[random.randint(0,len(player_index_list)-1)]
                player_index_list.remove(player_1_id)
                
                player_2_id = player_index_list[random.randint(0,len(player_index_list)-1)]
                player_index_list.remove(player_2_id)

                result = match_controller.play_match(player_list[player_1_id],player_list[player_2_id])
                if DEBUG: print('Player ',player_1_id,' vs Player ',player_2_id,' : ',MATCH_RESULT[result])
                player_score[player_1_id] += result
                player_score[player_2_id] -= result

        selected_players = [player_list[top_player_id] for top_player_id, _ in sorted(player_score.items(), key=lambda item: item[1])][-PLAYERS_TO_SELECT:]


    best_player = selected_players[-1]
    return best_player

def play_all_opponents():
    match_controller = MatchController()
    player_list = [Player() for _ in range(PLAYER_PER_GEN)]
    selected_players = None
    
    for _ in range(NUMBER_OF_GEN):
        if selected_players: player_list = [Player(selected_players[index % PLAYERS_TO_SELECT].logic) for index in range(PLAYER_PER_GEN)]

        player_score = {i:0 for i in range(PLAYER_PER_GEN)}
        
        for p1 in range(MATCHES_PER_GEN):
            for p2 in range(p1 + 1,MATCHES_PER_GEN):

                    result = match_controller.play_match(player_list[p1],player_list[p2])
                    if DEBUG: print('Player ',p1,' vs Player ',p2,' : ',MATCH_RESULT[result])
                    player_score[p1] += result
                    player_score[p2] -= result

                    result = match_controller.play_match(player_list[p2],player_list[p1])
                    if DEBUG: print('Player ',p2,' vs Player ',p1,' : ',MATCH_RESULT[result])
                    player_score[p2] += result
                    player_score[p1] -= result

        sorted_player_score = sorted(player_score.items(), key=lambda item: item[1])
        print(sorted_player_score)
        selected_players = [player_list[top_player_id] for top_player_id, _ in sorted_player_score][-PLAYERS_TO_SELECT:]


    best_player = selected_players[-1]
    return best_player

def play_against_manual(player):
    match_controller = MatchController()
    match_controller.manual_match(player,play_first = False)
    match_controller.manual_match(player,play_first = True)
    match_controller.manual_match(player,play_first = False)
    match_controller.manual_match(player,play_first = True)
    match_controller.manual_match(player,play_first = False)

if __name__ == '__main__':
    best_player = play_all_opponents()
    play_against_manual(best_player)

