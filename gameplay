import random

def gameplay():
    """goes through the game of monty hall"""
    choices = ["box_1", "box_2", "box_3"]
    prize_box = random.choice(choices)
    # getting the user to enter a valid choice out of the three boxes
    while True:
        try:
            user_choice = int(input("Pick a box: 1, 2, or 3"))
            if 1 <= user_choice <= 3:
                break
            else:
                print("Please enter an integer between 1 and 3")
        except ValueError:
            print("Please enter an integer between 1 and 3")
    chosen_index = user_choice - 1 # gets the index for the box that the player chose
    boxes_left = choices.copy()
    del boxes_left[chosen_index]  # gets the list of boxes that the player didn't choose
    if choices[chosen_index] == prize_box:  # if the the player picked the right box at first reveal a random box
        show = random.choice(boxes_left)
        print(f"{show} does not have the prize") # displays to the user a box that did not have the prize
        boxes_left.remove(show)  # remove the box from the remaining boxes
    else:
        for box in boxes_left:  # goes through the boxes that were not chosen by the player
            if box == prize_box:
                continue
            else:
                print(f"{box} does not have the prize")  # reveals to the user the remaining box without the prize
                boxes_left.remove(box)
    while True: # prompts the user whether or no they would like to switch their selected box
        print(f'Remaining box: {boxes_left}')
        switching = input("Would you like to switch boxes? (Y/N): ")
        if switching.lower() == "y" or switching.lower() == "n":  # handles both uppercase and lowercase inputs
            break
        else:
            print("Please enter Y or N")
    if switching.lower() == "y":
        chosen_index = choices.index(boxes_left[0])
    if choices[chosen_index] == prize_box: # checks if the player has the box with the prize in it
        print("You won the prize!")
    else:
        print("You lost!")


gameplay()
