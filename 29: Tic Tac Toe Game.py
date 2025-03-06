import numpy as np

def draw_board(num):
    digits = [int(letter) for letter in num if letter.isdigit()]
    if digits:
        size = digits[0]
        if size > 1:
            board = np.zeros((size,size))
            return board
        elif size == 1:
            print("Board size too small")
        else:
            print("Please Enter a valid digit")
            return None

def get_winner(num):
    if num == 1:
        return "Player1 won!"
    elif num == 2:
        return "Player2 won"

def is_winner():
    size = game.shape[0]
    possible_move = 4
    if possible_move == 0:
        return "Tie!"
    for i in range(size):
        if np.all(game[i,:] != 0):
            if np.all(game[i,:] == game[i,0]):
                return get_winner(game[i][0])
            else:
                possible_move -= 1
        elif np.all(game[:,i] != 0):
            if np.all(game[:,i] == game[0,i]):
                return get_winner(game[0][i])
            else:
                possible_move -= 1
        elif np.all(game[i,i] != 0):
            return "Tie!"
    if np.all(np.diag(game) != 0):
        if np.diag(game) == game[0,0]:
            return get_winner(game[0][0])
        else:
            possible_move -= 1
    if np.all(np.diag(np.fliplr(game)) != 0):
        if np.all(np.diag(np.fliplr(game)) == game[0,size-1]):
            return get_winner(game[0][size-1])
        else:
            possible_move -= 1
    return None
    
def player_move(player):
    while True:
        move = input(f"Player{player}'s move: (row,col)")
        try:
            row, col = map(int, move.split(","))
            if game[row-1][col-1] == 0:
                game[row-1][col-1] = player
                return
            else:
                print("Invalid move! Try again!")
        except ValueError:
            print("Invalid move! Try again!")

print("Welcome to Tic Tac Toe")
board_size = input("What size do you want you board to be? (too large can be time-consuming)")
game = draw_board(board_size)
if game is not None:
    print(game)
    Player1 = 1
    Player2 = 2
    playing = True
    
    while playing:
        player_move(Player1)
        print(game)
        if (winner := is_winner()):
            print(winner)
            break
    
        player_move(Player2)
        print(game)
        if (winner := is_winner()):
            print(winner)
            break
    print("Thank you for playing!")
