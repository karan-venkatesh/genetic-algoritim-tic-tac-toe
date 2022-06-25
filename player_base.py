import random


class PlayerBase:

    def set_player_id(self,player_id):
        self.player_id = player_id
    
    def get_move(self, board):
        moves = [(i,j) for i in range(3) for j in range(3) if board[i][j] == 0]
        return random.choice(moves)