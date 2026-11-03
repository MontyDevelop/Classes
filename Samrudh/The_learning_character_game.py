# # Agent - character
#
# # Environment
#
# # Action
#
# # Reward
# # ----------------------------------
# import random
# import time
# from tkinter import *
#
# grid_size = 5
#
# position = [0,0]
# treasure = [4,4]
#
# ai_rewards = {}
#
#
#
# screen = Tk()
# screen.title("Treasure Hunt Game")
#
#
# # movement characters
#
# def move(action):
#     global position
#     if action == 'up' and position[1] < grid_size - 1:
#         position[1] += 1
#     if action == 'down' and position[1] > 0:
#         position[1] -= 1
#     if action == 'left' and position[1] > 0:
#         position[1] -= 1
#     if action == 'right' and position[0] < grid_size - 1:
#         position[1] += 1
#
# actions = ['up','down','left','right']
#
# # Training of AI character
#
# for i in range(10):
#     position = [0,0]
#     print(f"Episode{i+1} starting....")
#     for step in range(15):
#         action = random.choice(actions)
#         move(action)
#
#         if tuple(position) not in ai_rewards:
#             ai_rewards[tuple(position)] = 0
#
#         if position == ai_rewards:
#             print("Found....")
#             ai_rewards[tuple(position)] += 10
#             break
#         else:
#             ai_rewards[tuple(position)] -= 1
#
# print(ai_rewards)
#
# screen.mainloop()

import tkinter as tk
import random

# ------ Configuration ------
GRID_SIZE = 5  # 5x5 grid
CELL_SIZE = 100  # pixels per cell
EPISODES = 15  # how many training rounds
MAX_STEPS = 20  # max moves per episode
DELAY_MS = 300  # pause between moves for visualization

# ------ Game state ------
position = [0, 0]  # agent start
treasure = [4, 4]  # fixed treasure location
rewards = {}  # memory of position rewards

actions = ["up", "down", "left", "right"]

# ------ Tkinter setup ------
root = tk.Tk()
root.title("AI Game Character That Learns!")

canvas = tk.Canvas(root,
                   width=GRID_SIZE * CELL_SIZE,
                   height=GRID_SIZE * CELL_SIZE + 50,
                   bg="white")
canvas.pack()

status_text = canvas.create_text(10, GRID_SIZE * CELL_SIZE + 25,
                                 anchor="w", font=("Arial", 14),
                                 text="Click START to teach the character!")

# Draw grid lines
for i in range(GRID_SIZE + 1):
    # vertical
    canvas.create_line(i * CELL_SIZE, 0, i * CELL_SIZE,
                       GRID_SIZE * CELL_SIZE, fill="gray")
    # horizontal
    canvas.create_line(0, i * CELL_SIZE, GRID_SIZE * CELL_SIZE,
                       i * CELL_SIZE, fill="gray")


# Helpers to map coordinates to canvas
def coord_to_xy(coord):
    x, y = coord
    # invert y so [0,0] is bottom-left visually
    return x * CELL_SIZE + CELL_SIZE // 2, (GRID_SIZE - 1 - y) * CELL_SIZE + CELL_SIZE // 2


# Draw treasure and agent icons
agent_id = None
treasure_id = None


def draw_static():
    global treasure_id
    # Treasure
    tx, ty = coord_to_xy(treasure)
    if treasure_id:
        canvas.delete(treasure_id)
    treasure_id = canvas.create_text(tx, ty, text="💎", font=("Arial", 32))


def draw_agent():
    global agent_id
    ax, ay = coord_to_xy(position)
    if agent_id:
        canvas.delete(agent_id)
    agent_id = canvas.create_text(ax, ay, text="🙂", font=("Arial", 32))


def update_status(msg):
    canvas.itemconfig(status_text, text=msg)
    root.update_idletasks()


# Movement function
def move(action):
    global position
    x, y = position
    if action == "up" and y < GRID_SIZE - 1:
        y += 1
    elif action == "down" and y > 0:
        y -= 1
    elif action == "right" and x < GRID_SIZE - 1:
        x += 1
    elif action == "left" and x > 0:
        x -= 1
    position = [x, y]


# Main training loop (runs asynchronously)
def train_episode(ep=0):
    if ep >= EPISODES:
        update_status("Training complete! Check rewards in console.")
        print("\nFinal AI Rewards Memory:", rewards)
        return

    # Reset start
    global position
    position = [0, 0]
    update_status(f"Episode {ep + 1} / {EPISODES} starting...")
    draw_agent()

    def step(step_num=0):
        if step_num >= MAX_STEPS:
            # end episode
            root.after(500, lambda: train_episode(ep + 1))
            return

        action = random.choice(actions)
        move(action)
        draw_agent()

        key = tuple(position)
        if key not in rewards:
            rewards[key] = 0

        if position == treasure:
            update_status(f"Episode {ep + 1}: 🎉 Found treasure in {step_num + 1} steps!")
            rewards[key] += 10  # reward
            # proceed to next episode after short pause
            root.after(800, lambda: train_episode(ep + 1))
            return
        else:
            rewards[key] -= 1  # penalty
            update_status(f"Episode {ep + 1}: Step {step_num + 1}, moved {action}.")

        # Continue next step
        root.after(DELAY_MS, lambda: step(step_num + 1))

    step(0)


# Button to start training
def start_training():
    draw_static()
    train_episode(0)

 
start_button = tk.Button(root, text="START Training", font=("Arial", 12, "bold"),
                         command=start_training, bg="#4CAF50", fg="white", padx=10, pady=5)
canvas.create_window(GRID_SIZE * CELL_SIZE // 2, GRID_SIZE * CELL_SIZE + 25,
                     window=start_button)

# Initial draw
draw_static()
draw_agent()

# Run GUI
root.mainloop()
