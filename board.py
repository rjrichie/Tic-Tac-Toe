from typing import Any
from player import Player


class Board:
    # Constructor for the Board class that initializes the board with the given size
    def __init__(self, board_size, mode):
        if (board_size < 3 or board_size > 10):
            raise ValueError("Board size should be at least 3 or not more than 10")
            
        self.board_size = board_size
        self.__board = [[' ' for i in range(board_size)] for j in range(board_size)]
        self.__num_free_cells = board_size * board_size;
        self.mode = mode

    # Place method that places the player's move on the board
    def do_move(self, x, y, player):
        if self.__board[x][y] == ' ':
            self.__board[x][y] = player.symbol
            self.__num_free_cells -= 1
            return True
        else:
            print("The cell is already occupied. Please choose another cell.")
            return False

    # Undo method that removes the player's move from the board
    def undo_move(self, x, y):
        if self.__board[x][y] == ' ':
            return
        self.__board[x][y] = ' '
        self.__num_free_cells += 1

    # Count Free Cells method that returns the number of free cells on the board
    def count_free_cells(self):
        count = 0
        for i in range(self.board_size):
            for j in range(self.board_size):
                if self.__board[i][j] == ' ':
                    count += 1
        self.__num_free_cells = count
        return count

    # Set Board method that sets the board with the given state
    def set_board(self, board):
        self.__board = board
        self.count_free_cells()

    # Check Win method that checks if the player has won
    def check_win(self, player1, player2):
        for i in range(self.board_size):
            for j in range(self.board_size):
                if self.__board[i][j] == ' ':
                    continue
                if self.check_row(i, j) or self.check_col(i, j) or self.check_diag(i, j):
                    if self.__board[i][j] == player1.symbol:
                        player1.win = True
                        player2.win = False
                        return player1
                    else:
                        player1.win = False
                        player2.win = True
                        return player2
        return None

    # Check Row method that checks if the player has won in a row
    def check_row(self, x, y):
        for i in range(self.board_size):
            if self.__board[x][i] != self.__board[x][y]:
                return False
        return True

    # Check Column method that checks if the player has won in a column
    def check_col(self, x, y):
        for i in range(self.board_size):
            if self.__board[i][y] != self.__board[x][y]:
                return False
        return True

    # Check Diagonal method that checks if the player has won in a diagonal
    def check_diag(self, x, y):
        if x == y:
            for i in range(self.board_size):
                if self.__board[i][i] != self.__board[x][y]:
                    return False
            return True
        if x + y == self.board_size - 1:
            for i in range(self.board_size):
                if self.__board[i][self.board_size - 1 - i] != self.__board[x][y]:
                    return False
            return True
        return False


    # Get Attribute method that returns the attribute of the class
    def __getattribute__(self, name: str) -> Any:
        return super().__getattribute__(name)

    # Print Board method that displays the current state
    def printBoard(self):
        print("\n")
        for i in range(self.board_size):
            print(" ---" * self.board_size)
            for j in range(self.board_size):
                print("| " + self.__board[i][j] + " ", end="")
            print("|")
        print(" ---" * self.board_size)
        print("\n")

    # Draw method that checks if the game is a draw
    def draw(self, player1, player2):
        return (self.__num_free_cells == 0) and (not self.check_win(player1, player2))
    
    # Return valid moves in the board
    def get_valid_moves(self):
        valid_moves = []
        for i in range(self.board_size):
            for j in range(self.board_size):
                if self.__board[i][j] == ' ':
                    valid_moves.append((i, j))
        return valid_moves

# Test the Board class

# # Create a new board (Constructor Test)
# board = Board(3,1)
# board.printBoard()
# player = Player("RJ", "X")
# player2 = Player("Bot", "O")

# # Test the do_move method
# board.do_move(0, 0, player)
# board.do_move(0, 0, player)
# board.printBoard()
# board.do_move(0, 1, player)
# board.printBoard()

# # Test the undo_move method
# board.undo_move(0, 1)
# board.printBoard()

# # Test the check_win method
# board.do_move(1, 1, player)
# board.do_move(2, 2, player)
# board.printBoard()

# winner = board.check_win()
# if winner:
#     print(f"The winner is: {winner}\n")
# else:
#     print("No winner yet.\n")

# # Test the draw method
# board.set_board([
#     ['X', 'X', 'O'],
#     ['O', 'O', 'X'],
#     ['X', 'O', 'X']
#     ])


# board.printBoard()
# draw = board.draw()
# print(draw)

# if board.draw():
#     print("The game is a draw.\n")

# # Test the get_valid_moves method
# board.set_board([
#     ['X', ' ', ' '],
#     ['O', ' ', ' '],
#     ['X', 'O', ' ']
#     ])
# print(board.get_valid_moves())