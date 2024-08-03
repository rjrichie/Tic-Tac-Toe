# from board import Board

class Player:
    def __init__(self, name: str, symbol: str):
        self.name = name
        self.win = None
        self.symbol = symbol
    
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
        return
    
    def do_bot_move_hard(self, board, player1):
        return
    
    def result(self):
        if self.win == False:
            print(self.name + " loses!")
            print("Try your best next time!")
        elif self.win == True:
            print(self.name + " wins!")
            print("Congratulations!")
        else:
            return