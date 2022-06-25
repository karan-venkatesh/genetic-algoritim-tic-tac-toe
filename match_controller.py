from game_board import GameBoard
from player_genetic import PlayerGenetic
import random

DEBUG = False

PROMPT = '\n'.join(['\t'.join(str(i+1) for i in range(j*3,j*3+3)) for j in range(3)])

class MatchController:
    def __init__(self):
        pass
    
    def detect_move(self, player, game_board):
        if player != None:
            return player.get_move(game_board.board)
        else:
            return random.randint(0,2), random.randint(0,2)

    def play_match(self,player_1, player_2):
        game_board = GameBoard()
        if player_1 != None: player_1.set_player_id(1)
        if player_2 != None: player_2.set_player_id(-1)
        for i in range(9):
            if i%2 == 0:
                move = self.detect_move(player_1, game_board)
                # move = player_1.get_move(game_board.board)
                player_id = 1
                if DEBUG: print(move)

            else:
                move = self.detect_move(player_2, game_board)
                # move = player_2.get_move(game_board.board)
                player_id = -1
                if DEBUG: print(move)

            if move == None:
                if DEBUG: print("DRAW")
                return 0

            game_board.play_move(move[0], move[1], player_id)
            if DEBUG: print(game_board)

            if game_board.check_win(player_id):
                if DEBUG: print("WINNER",player_id)
                return player_id
        return 0

    def manual_match(self,player,play_first = True):
        game_board = GameBoard()
        turn_order = int(play_first)
        player_id = turn_order * 2 -1
        player.set_player_id(-player_id)
        for turn in range(9):
            if turn%2 != turn_order:
                print()
                print(game_board,'\n')
                print(PROMPT)
                move = int(input("Enter your value: ")) - 1
                game_board.play_move(move//3, move%3, player_id)
            else:
                print()
                print(game_board,'\n')
                move = player.get_move(game_board.board)
                game_board.play_move(move[0], move[1], -player_id)
            
            if game_board.check_win(1):
                print("WINNER",1)
                break
            
            if game_board.check_win(-1):
                print("WINNER",-1)
                break


