import numpy as np

class Board:
    def __init__(self):
        self.game_active = True
        self.x_turn = True
        self.board = np.array([[0, 0, 0], [0, 0, 0], [0, 0, 0]])
        self.x_mask = np.array([
            [[1, 1, 1], [0, 0, 0], [0, 0, 0]],
            [[0, 0, 0], [1, 1, 1], [0, 0, 0]],
            [[0, 0, 0], [0, 0, 0], [1, 1, 1]], 
            [[1, 0, 0], [1, 0, 0], [1, 0, 0]], 
            [[0, 1, 0], [0, 1, 0], [0, 1, 0]], 
            [[0, 0, 1], [0, 0, 1], [0, 0, 1]], 
            [[0, 0, 1], [0, 1, 0], [1, 0, 0]], 
            [[1, 0, 0], [0, 1, 0], [0, 0, 1]]])
        self.o_mask = -1 * self.x_mask
        self.x_evals = np.zeros(9)
        self.o_evals = np.zeros(9)
        self.winner = ""
        self.turns = 0

    def move(self, movement):
        if self.check_valid_move(movement):
            if self.x_turn:
                self.board.reshape(9)[movement-1] = 1
            else:
                self.board.reshape(9)[movement-1] = -1
            self.evaluate_board()
    
    def check_valid_move(self, movement):
        if self.board.reshape(9)[movement-1] == 0: # stretch out board and see if no move in index
            return True
    
    def evaluate_board(self):
        if self.x_turn:
            self.x_evals = np.sum(np.sum(self.board * self.x_mask, axis=2), axis=1) # evaluate board for X sequences
        else:
            self.o_evals = np.sum(np.sum(self.board * self.o_mask, axis=2), axis=1) # evaluate board for O sequences
        
        self.turns += 1
        self.x_turn = not self.x_turn

        # Sequences will sum to 3 if there's a win
        if np.any(self.x_evals[:] == 3):
            self.winner = "X"
            self.game_active = False
        elif np.any(self.o_evals[:] == 3):
            self.winner = "O"
            self.game_active = False
        elif self.turns == 9:
            self.winner = "-"
            self.game_active = False

if __name__ == "__main__":
    game = Board()

    while game.game_active == True:
        
        print(game.board)

        if game.x_turn:
            choice = input("X move: ")
        else:
            choice = input("O move: ")

        game.move(int(choice))

        if game.game_active == False:
            print(game.board)
            print("{0} wins!".format(game.winner))
    
    
        

