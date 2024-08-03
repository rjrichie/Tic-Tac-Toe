# from board import Board

import random


class Player:
    def __init__(self, name: str, symbol: str):
        self.name = name
        self.win = None
        self.symbol = symbol
        self.best_move = None
    
    # Do Player Move method that prompts the player to make a move
    def do_player_move(self, board, player2):
        print(self.name + "'s turn.")
        print("Please enter the coordinates of your move.")
        print("Valid moves", board.get_valid_moves())
        
        # Get the coordinates of the move
        while True:
            input_str = input("Enter the x and y coordinates (row, column): ")
            
            try:
                # Split the input string and remove unwanted characters
                input_str = input_str.replace("(", "").replace(")", "").replace(","," ")
                x, y = input_str.split()
                x = int(x)
                y = int(y)
                
                # Check if the move is valid
                if x < 0 or x >= board.board_size or y < 0 or y >= board.board_size:
                    print("Invalid move. Please try again.\n")
                    continue
                
                # Attempt to make the move
                if board.do_move(x, y, self):
                    print("Player " + self.name + " has placed a move at (" + str(x) + ", " + str(y) + ")")
                    break

            except ValueError:
                print("Invalid move. Please try again.\n")
                continue
        
        # Check win condition for player
        if board.check_win(self, player2):
            return True
        return False

    # Do Bot Move method that prompts the bot to make a move with a random valid move
    def do_bot_move_easy(self, board, player1):
        # Check if there are valid moves
        if len(board.get_valid_moves()) == 0:
            return False

        print("Bot's turn.")
        print("Bot is thinking...")

        # Get a random move
        length = len(board.get_valid_moves())
        rand_index = random.randint(0, length - 1)
        move = board.get_valid_moves()[rand_index]
        x, y = move

        # Attempt to make the move (Always a valid move)
        board.do_move(x, y, self)
        print("Bot has placed a move at (" + str(x) + ", " + str(y) + ")")


        # Check win condition for bot
        if board.check_win(self, player1):
            return True
        return False

    def do_bot_move_hard(self, board, player1):
        # Check if there are valid moves
        if len(board.get_valid_moves()) == 0:
            return False

        print("Bot's turn.")
        print("Bot is thinking...")

        # Get the best move using minimax algorithm
        _, best_move = self.minimax(board, player1, True, 0, -1000000, 1000000)
        # _, best_move = self.alphaBeta(board, player1, True, 0, -1000000, 1000000)
        if best_move is None:
            return False
        x, y = best_move
        x = int(x)
        y = int(y)
        
        # Attempt to make the move (Always a valid move)
        board.do_move(x, y, self)
        print("Bot has placed a move at (" + str(x) + ", " + str(y) + ")")

        # Check win condition for bot
        if board.check_win(self, player1):
            return True
        return False

    # Minimax algorithm (Alpha-Beta-Pruning)
    def minimax(self, board, player1, isMaximizingPlayer, depth, alpha, beta, max_depth=5):
        if (board.check_win(self, player1) == player1): # player1 wins
            return -(board.count_free_cells() + 1), None
        elif (board.check_win(self, player1) == self): # bot wins
            return (board.count_free_cells() + 1), None
        
        # Draw condition
        if (board.draw(self, player1)):
            return 0, None

        if isMaximizingPlayer: 
            bestVal = float('-inf')
            best_move = None
            for move in board.get_valid_moves():
                x, y = move
                board.do_move(x, y, self)
                value, _ = self.minimax(board, player1, False, depth + 1, alpha, beta, max_depth)
                board.undo_move(x, y)
                if value > bestVal:
                    bestVal = value
                    best_move = move
                alpha = max(alpha, bestVal)
                if beta <= alpha:
                    break
            return bestVal, best_move
        else:
            bestVal = float('inf')
            best_move = None
            for move in board.get_valid_moves():
                x, y = move
                board.do_move(x, y, player1)
                value, _ = self.minimax(board, player1, True, depth + 1, alpha, beta, max_depth)
                board.undo_move(x, y)
                if value < bestVal:
                    bestVal = value
                    best_move = move
                beta = min(beta, bestVal)
                if beta <= alpha:
                    break
            return bestVal, best_move
        
    def result(self):
        if self.win == False:
            print(self.name + " loses!")
            print("Try your best next time!")
        elif self.win == True:
            print(self.name + " wins!")
            print("Congratulations!")
        else:
            return