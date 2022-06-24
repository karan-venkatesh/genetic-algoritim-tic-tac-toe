from distutils.debug import DEBUG
import random
import math

DEBUG= False

class Player:
    def __init__(self, parent_logic = None, mutation_rate = 20):
        if parent_logic:
            self.logic = parent_logic
        else:
            self.logic = [[0 for _ in range(9)] for _ in range(9)]
        for _ in range(mutation_rate):
            self.mutate()
    
    def __str__(self):
        return '\n'.join(['\t'.join([str(item) for item in row]) for row in self.logic])

    def mutate(self):
        self.logic[random.randint(0,8)][random.randint(0,8)] += random.randint(-1,1)

    def set_player_id(self,player_id):
        self.player_id = player_id
    
    def score_move(self, logic_row, board):
        score = 0
        for i in range(8):
            score += board[i//3][i%3] * self.player_id * logic_row[i] + logic_row[i]
        return score

    def map_number(self,value):
        if value in (0,2,6,8):
            return 0
        if value in (1,3,5,7):
            return 1
        else:
            return 2 


    def get_move(self, board):
        best_move = -math.inf
        play_move = None
        for i in range(3):
            for j in range(3):
                if board[i][j] == 0:
                    move_score = self.score_move(self.logic[3*i + j], board)
                    if DEBUG: print(i,j,move_score)
                    if move_score > best_move:
                        if DEBUG: print("NEW BEST MOVE",i,j,move_score,best_move)
                        best_move = move_score
                        play_move = (i,j)
        return play_move
                        


