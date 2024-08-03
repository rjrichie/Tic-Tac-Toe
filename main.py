from messages import intro, exitGame
from player import Player
from board import Board


intro()

# Select game mode
print("Please select the game mode:")

while True:
    print("1. Player vs Player")
    print("2. Player vs Bot (Easy)")
    print("3. Player vs Bot (Hard)")
    mode = input("Enter the number of the game mode: ")

    if mode == "1" or mode == "2" or mode == "3":
        break

    print("Please pick a correct mode.\n")

print("You have selected mode " + mode + ".\n")

# Input board size
print("Please select the board size:")
while True:
    board_size = int(input("Enter the board size (3-10): "))

    if board_size < 3 or board_size > 10:
        print("Board size should be at least 3 or not more than 10.")
    else:
        break

print("You have selected board size " + str(board_size) + ".\n")
board = Board(board_size, mode)

# Input player names
while True:
    player1 = Player(input("Enter the name of Player 1 (O): "), 'O')

    if mode == "2" or mode == "3":
        player2 = Player("Bot")
    else:
        player2 = Player(input("Enter the name of Player 2 (X): "), 'X')

    if player1.name == player2.name:
        print("Player names should be different.")
    else:
        break

print()

# Game loop for mode 1
while mode == "1":
    # Player 1 turn
    board.printBoard()
    if player1.do_player_move(board, player2):
        break

    # Player 2 turn
    board.printBoard()
    if player2.do_player_move(board, player1):
        break

# Game loop for bot
while mode == "2" or mode == "3":
    # Player 1 turn
    board.printBoard()
    if player1.do_player_move(board, player2):
        break

    # Bot turn
    board.printBoard()
    if mode == "2": # Easy bot
        if player2.do_bot_move_easy(board, player1):
            break
    else: # Hard bot
        if player2.do_bot_move_hard(board, player1):
            break

    
board.printBoard()
player1.result()
print()
player2.result()
print()
exitGame()