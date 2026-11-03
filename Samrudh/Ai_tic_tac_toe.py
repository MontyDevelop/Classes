# Create a Basic 3x3 Game Board UI

import tkinter as tk
import random
from tkinter import messagebox

window = tk.Tk()
window.title("Tic tac toe game")
window.geometry("400x400")

all_buttons = []
for i in range(9):
    button = tk.Button(window, text=" ", width=5,height=2,font=("Helvetica", 32),command=lambda i=i:handle_click(i))
    button.grid(row=i//3, column=i%3)
    all_buttons.append(button)

# Add the Game Board Logic

board = [" " for _ in range(9)]

# Handle Button Clicks (User Turn)
def handle_click(index):
    if board[index] == " ":
        board[index] = "x"
        all_buttons[index].config(text='x', state='disabled')

        # player moves
        if check_winner('x'):
            messagebox.showinfo("Tic Tac Toe", "You Win!")
            window.quit()
            return
        elif is_draw():
            messagebox.showinfo("Tic Tac Toe", "Its Draw!")
            window.quit()
            return

        # Ai move
        ai_index = ai_move()
        if ai_index is not None:
            board[ai_index] == "o"
            all_buttons[ai_index].config(text='o', state='disabled')
            if check_winner("o"):
                messagebox.showinfo("Tic Tac Toe", "You Win!")
                window.quit()
                return
            elif is_draw():
                messagebox.showinfo("Tic Tac Toe", "Its Draw!")
                window.quit()
                return


# Add Game Over Check (Win or Draw)
win_patterns = [[0,1,2],[0,3,6],[0,4,8],[3,4,5],[1,4,7],[2,5,8],[6,7,8],[2,4,6]]
def check_winner(player):
    for i in win_patterns:
        if board[i[0]] == player and board[i[1]] == player and board[i[2]] == player:
            return True
    return False


def is_draw():
    if " " not in board:
        return True



# Add AI Move (Computer Turn)
def ai_move():
    empty_spots = [i for i in range(9) if board[i] == " "]
    if empty_spots:
         return random.choice(empty_spots)
    return None


window.mainloop()