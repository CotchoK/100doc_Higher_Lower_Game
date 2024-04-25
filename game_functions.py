import random as r

# create function to randomly select the person from the list
def random_selection(list):
    selected = r.choice(list)
    list.pop(list.index(selected))
    #print(list)
    return selected


# create a function that conducts the comparison
def compare(person1, person2):
    if person1["follower_count"] > person2["follower_count"]:
        return 1
    else:
        return 0