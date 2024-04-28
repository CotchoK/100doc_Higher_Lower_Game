# import required python library
import random as r
import os  # used to import the clear screen functionality

# import user defined files
import game_data as gd
import game_functions as gf
import art as a


def cls():
    """
    Clear screen function
    NOTE: ensure to check the Emulate Terminal in Output Console in the Configurations settings
    :return:
    """
    os.system('cls' if os.name == 'nt' else 'clear')


def run_game(game_list=gd.data, round_end=False):
    """
    Dictates and executes the game loop
    :param game_list: the starting list of all characters that will be a part of the comparison game
    :param round_end: flag that indicates whether the round has ended and will determine when to exit game loop
    :return:
    """
    # game variables variables
    score = 0
    # create a copy of the game_list to be used, otherwise list mutation will be applied to global variable
    # the live list is a list that will have reducing number of options the computer can select from.
    live_list = game_list.copy()
    # initial candidate selected from the live_list
    candidate = gf.random_selection(live_list)

    # execute round looping
    while not round_end:
        # extract the second candidate from the live list
        candidate2 = gf.random_selection(live_list)

        # prints the visuals for the player
        gf.game_display(candidate, candidate2, False, score)

        # ask user for their input as to whom has the most followers on instagram
        user_choice = input("Who has more followers? Type 'A' or 'B': ").lower()

        # execute comparison of both candidates and return a result
        if user_choice == 'a':
            result = gf.compare(candidate, candidate2)
        elif user_choice == 'b':
            result = gf.compare(candidate2, candidate)

        # with the result execute game logic
        # increase score and map candidate 1 with candidate 2. will loop again
        if result == 1:
            cls()
            score += 1
            candidate = candidate2
        # if player doesn't guess correctly then output a specific sets of visuals on screen
        # with player score and request to whether they want to play again terminates round loop
        elif result == 0:
            cls()
            gf.game_display(candidate, candidate2, True, score)
            response = input(f"Did you want to play again 'y' or 'n'? ")
            round_end = True
            if response == 'y':
                run_game()
            else:
                exit()

        # checks the live list to see if there are any candidates remaining. if not the player wins the game
        # asks user if want to play again
        if len(live_list) == 0:
            print(a.logo)
            response = input(f"You have beat the game with {score} points.\n"
                             "Did you want to play again 'y' or 'n'? ")
            round_end = True
            if response == 'y':
                run_game()
            else:
                exit()


run_game()

