import random

def gameplay_switch():
    """goes through the game of monty hall when the user always switches"""
    choices = ["box_1", "box_2", "box_3"] # creates three boxes
    prize_box = random.choice(choices) # chooses a random box to be the one with the prize
    random_pick = random.choice(choices)  # choosing box at random to simulate user choice
    boxes_left = choices.copy()
    boxes_left.remove(random_pick)  # list of boxes not chosen yet
    remaining_box = None
    if random_pick == prize_box: # picks a random box to reveal if the user has already chosen the prize box
        show = random.choice(boxes_left)
        boxes_left.remove(show)
    else:  # reveals and removes the empty box if the user did not pick the prize box
        for box in boxes_left:
            if box == prize_box:
                remaining_box = box
            else:
                continue
    random_pick = remaining_box
    if random_pick == prize_box: # returns 1 if the user won
        win = 1
        return win
    else:
        loss = 0
        return loss # returns 0 if the user lost

def gameplay_no_switch():
    """goes through the game of monty hall when the user does not switch"""
    choices = ["box_1", "box_2", "box_3"]  # creates three boxes
    prize_box = random.choice(choices)  # chooses a random box to be the one with the prize
    random_pick = random.choice(choices)  # choosing box at random to simulate user choice
    if random_pick == prize_box: # returns 1 if random pick was correct
        win = 1
        return win
    else: # returns 0 if random pick was incorrect
        loss = 0
        return loss

# initiating the number of wins for the experiment as 0
switch_wins = 0
no_switch_wins = 0

# simulating 10,000 games for each play style
for game in range(10000):
    switch_wins += gameplay_switch()

for game in range(10000):
    no_switch_wins += gameplay_no_switch()

# turning the win proportions to a percentage
switch_win_percentage = (switch_wins / 10000) * 100
no_switch_percentage = (no_switch_wins / 10000) * 100

# Displaying the win percentages to the user
print(f'The chances for winning if the player always switches is {switch_win_percentage}%')
print(f'The chances for winning if the player never switches is {no_switch_percentage}%')
