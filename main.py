# import required python library
import random as r

# import user defined files
import art as a
import game_data as gd
import game_functions as gf

# print the logo
print(a.logo)

score = 0
candidates = gd.data


# print text for first randomly chosen item from game_data.py item of comparison
candidate = gf.random_selection(candidates)
print(f"Compare A: {candidate['name']}, a {candidate['description']}, from {candidate['country']}")

# print "vs" art
print(a.vs)

# print text for the secondly randomly chosen item from the game_data.py item of comparison
candidate2 = gf.random_selection(candidates)
print(f"Compare B: {candidate2['name']}, a {candidate2['description']}, from {candidate2['country']}")

# ask user for their input as to whom has the most followers on instagram
user_choice = input("Who has more followers? Type 'A' or 'B': ").upper()
if user_choice == 'A':
    result = gf.compare(candidate, candidate2)
elif user_choice == 'B':
    result = gf.compare(candidate2, candidate)

if result == 1:
    score += 1
elif result == 0:
    score

# we will need to loop the program each time the player gets the answer right
# we need to increase their score for every right answer
# if the player gets the answer wrong then the game ends (displaying only heading)
# and prints the "Sorry, that's wrong. Your final score was: {answers} (no vs logo or comparison texts)

# we will need to create another loop to handle when the player wants to play again