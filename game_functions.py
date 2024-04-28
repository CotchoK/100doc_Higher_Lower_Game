import random as r
import art as a

# create function to randomly select the person from the list
def random_selection(list):
    selected = r.choice(list)
    list.pop(list.index(selected))
    #print(new_list)
    return selected


# create a function that conducts the comparison
def compare(person1, person2):
    """
    Compares the follower count of the two candidates passed to it
    :param person1: candidate 1
    :param person2: candidate 2
    :return: either 1 or 0
    """
    if person1["follower_count"] > person2["follower_count"]:
        return 1
    else:
        return 0


def game_display(person1, person2, player_lost=False, score=0):
    """
    Displays specific text to the player based on what flags are passed to it
    :param person1: candidate 1 for the game
    :param person2: candidate 2 for the game
    :param player_lost: flag if the player lost which prints out alternative messaging
    :param score: score to print score
    :return:
    """
    if not player_lost:
        # print the logo
        print(a.logo)

        if score > 0:
            print(f"You're right! Current score: {score}")

        # print text for first randomly chosen item from game_data.py item of comparison
        print(f"Compare A: {person1['name']}, a {person1['description']}, from {person1['country']}")

        # print "vs" art
        print(a.vs)

        # print text for the secondly randomly chosen item from the game_data.py item of comparison
        print(f"Compare B: {person2['name']}, a {person2['description']}, from {person2['country']}")
    else:
        # print the logo
        print(a.logo)

        print(f"Sorry, that's wrong. Final score: {score}")
