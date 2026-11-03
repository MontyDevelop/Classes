import random

# Initialize the board
board = [" " for _ in range(9)]

# Function to print the board
def print_board():
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("-" * 10)
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("-" * 10)
    print(f"{board[6]} | {board[7]} | {board[8]}")

# Function to check if someone won
def check_winner(player):
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # columns
        [0, 4, 8], [2, 4, 6]              # diagonals
    ]
    for condition in win_conditions:
        if all(board[i] == player for i in condition):
            return True
    return False

# Function for AI move
def ai_move():
    empty_spots = [i for i in range(9) if board[i] == " "]
    move = random.choice(empty_spots)
    board[move] = "O"

# Function for Player move
def player_move():
    while True:
        try:
            move = int(input("Choose your spot (1-9): ")) - 1
            if board[move] == " ":
                board[move] = "X"
                break
            else:
                print("Spot already taken!")
        except (IndexError, ValueError):
            print("Invalid input. Choose a number between 1 and 9.")

# Main game loop
def play_game():
    print("Welcome to Tic-Tac-Toe! You are 'X', AI is 'O'.")
    print_board()

    for turn in range(9):
        if turn % 2 == 0:
            player_move()
        else:
            ai_move()

        print_board()

        # Check for win
        if check_winner("X"):
            print("You Win! 🎉")
            return
        if check_winner("O"):
            print("AI Wins! 🤖")
            return

    print("It's a Tie!")

# Start the game
play_game()
