# Game Board Object

DEBUG= False

class GameBoard:
    def __init__(self):
        self.board = [[0 for _ in range(3)] for _ in range(3)]

    def __str__(self):
        return '\n'.join(['\t'.join([str(item) for item in row]) for row in self.board])
    
    def check_win(self,player):
        win_condition = [1 for _ in range(8)]
        for i in range(3):
            for j in range(3):
                if self.board[i][j] != player:
                    win_condition[i] = 0
                    win_condition[3+j] = 0
                    if i == j:
                        win_condition[6] = 0
                    if i == 2-j:
                        win_condition[7] = 0
        if sum(win_condition) == 0:
            return False
        else:
            return True
    
    def play_move(self,row,col,player):
        self.board[row][col] = player
        