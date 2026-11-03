import random

choices = ['rock', 'paper', 'scissors']
win_rules = {
    'rock': 'scissors',
    'paper': 'rock',
    'scissors': 'paper'
}

player_history = {
    'rock': 0,
    'paper': 0,
    'scissors': 0
}

player_score = 0
ai_score = 0

def predict_player_move():
    most_common_move = max(player_history, key=player_history.get)
    predicted_counter = None
    for move, beats in win_rules.items():
        if beats == most_common_move:
            predicted_counter = move
            break
    return predicted_counter


print("Smart Rock-Paper-Scissors AI Game!")
print("Type 'exit' to quit the game.")

while True:
    player = input("Your move (rock/paper/scissors): ").lower()
    if player == 'exit':
        break
    if player not in choices:
        print("Invalid move. Try again.")
        continue

    player_history[player] += 1

    ai = predict_player_move()


    if player == ai:
        print("It's a tie!")
    elif win_rules[player] == ai:
        print("You win this round!")
        player_score += 1
    else:
        print("AI wins this round!")
        ai_score += 1

    print(f"Score -> You: {player_score} | AI: {ai_score}")
    print("-" * 30)

print("Game over! Thanks for playing!")
