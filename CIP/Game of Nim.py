import random

STONES = 20
MIN_RAND = 1
MAX_RAND = 2
DICE_MAX_NUM = 6

def main():
    computer = False
    
    print("Welcome to the game of Nimm")
    print("1. Player vs. Player")
    print("2. Player vs. Computer")
    print("3. Exit")
    user_select = input("Please make a selection (1-3): ")
    
    try: 
        if ((int(user_select) < 3) and (int(user_select) > 0)):
            if (int(user_select) == 1):
                player = randomize_player_turn(computer)
                game(computer, player)
            elif (int(user_select) == 2):
                computer = True
                player = randomize_player_turn(computer)
                game(computer, player)
        else:
            print("Invalid Input.")
    except:
        print("Invalid Input.")

"""
* Main game controller, loop through game_internal will there are zero stones left
* param: boolean, int
"""
def game(computer, player):
    stones_left = STONES
    player_switch_counter = 0
    # checks if player 2 or computer go first, else player 1 default
    if (player == 2):
        player_switch_counter = 1

    while (stones_left > 0):
        stones_left = game_internal(computer, player_switch_counter, stones_left)
        player_switch_counter += 1
        
    if (stones_left < 0):
        print("Game Over")
    else:
        print(current_player(player_switch_counter, computer)  + " wins!")

"""
* Game logic 
* param: boolean, int, int
* return int
"""
def game_internal(computer, p_switch, stones_remaining):
    print("There are " + str(stones_remaining) + " stones left.")
        
    # condition to check if player vs player, or player vs computer
    if (current_player(p_switch, computer) == "Computer"):
        player_input = random.randint(MIN_RAND, MAX_RAND)
        if (stones_remaining == 1):
            player_input = 1
        print(current_player(p_switch, computer) + " would you like to remove 1 or 2 stones?")
        print(player_input)
    else:
        player_input = input(current_player(p_switch, computer) + " would you like to remove 1 or 2 stones? ")
        player_input = check_entry(player_input)
    print("")

    return (stones_remaining - player_input)

""" 
* Determine current player
* Player 1 =>  n=even, (n%2 = 0)
* Player 2 =>  n=odd,  (n%2 = 1)
* Computer =>  n=odd,  (n%2 = 1) and (Computer)
* parameter: int, boolean
* return: string
"""
def current_player(n, computer):
    player = ""
    if ((n%2) == 0):
        player = "Player 1"
    elif (((n%2) == 1) and (not computer)):
        player = "Player 2"
    else:
        player = "Computer"
    return player

""" 
* check if user input is valid, else ask user to retry
* parameter: string
* return: int
"""
def check_entry(user_input):
    player_input = user_input
    while (player_input.isdigit() == False):
        player_input = input("Please enter 1 or 2: ")
        if (player_input.isdigit() == True):
            if (float(player_input) < 1) or (float(player_input) > 2) or ((float(player_input) > 1) and (float(player_input) < 2)):
                player_input = input("Please enter 1 or 2: ")
    try:
        while ((int(player_input) < 1) or (int(player_input) > 2)):
            player_input = input("Please enter 1 or 2: ")
    except:
        player_input = check_entry(user_input)
    return int(player_input)

"""
* Roll a dice to determine which player goes first
* Else default to player 1
* param: boolean
* return int
"""
def randomize_player_turn(computer):
    player = 1
    selection = input("Would you like to roll a dice (Y or N)? ")
    if ((selection == "Y") or (selection == "y")):
        dice1 = random.randint(MIN_RAND, DICE_MAX_NUM)
        dice2 = random.randint(MIN_RAND, DICE_MAX_NUM)
        print("Player 1 dice: " + str(dice1))
        print(current_player(1, computer) + " dice: " + str(dice2))
        if (dice1 > dice2):
            print("Player 1 go first")
        else:
            print(current_player(1, computer) + " go first")
            player = 2
    else:
        print("Game default to Player 1 first")
    print("")

    return player

# to call the main() function.
if __name__ == '__main__':
    main()
