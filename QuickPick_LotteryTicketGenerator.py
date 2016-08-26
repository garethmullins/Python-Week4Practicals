"""
A lottery ticket creater and picker that accepts the maximum, minimum numbers allowed, the number of unique numbers to be used
and the number of numbers that are being chosen.
"""
__author__ = 'Gareth'


import random


def main():
    NUM_OF_CHOICES = 6
    MIN_CHOICE = 0
    MAX_CHOICE = 45
    possible_picks = []
    num_of_quick_picks = int(input("How many quick picks? "))

    possible_picks = randomize_choices(MAX_CHOICE, MIN_CHOICE, NUM_OF_CHOICES, num_of_quick_picks, possible_picks)

    print("")

    for i in range(0, num_of_quick_picks):
        for j in range(0, NUM_OF_CHOICES - 1):
            print("{:2} ".format(possible_picks[i * NUM_OF_CHOICES + j]), end=" ")
        print()

    print("")

    possible_picks = order(NUM_OF_CHOICES, num_of_quick_picks, possible_picks)

    # TODO: Code the quick picks/auto picks.


def order(NUM_OF_CHOICES, num_of_quick_picks, possible_picks):
    for i in range(0, num_of_quick_picks):
        for j in range(0, NUM_OF_CHOICES - 1):
            temp_min = possible_picks.index(min(possible_picks[(i * NUM_OF_CHOICES) + j:(i + 1) * NUM_OF_CHOICES]),
                                            i * NUM_OF_CHOICES)
            temp_backup = possible_picks[j + (i * NUM_OF_CHOICES)]
            possible_picks[j + (i * NUM_OF_CHOICES)] = possible_picks[temp_min]
            possible_picks[temp_min] = temp_backup
    return possible_picks


def randomize_choices(MAX_CHOICE, MIN_CHOICE, NUM_OF_CHOICES, num_of_quick_picks, possible_picks):
    random_choice = 0
    for i in range(0, num_of_quick_picks):
        for j in range(0, NUM_OF_CHOICES):
            while random_choice in possible_picks[i * NUM_OF_CHOICES:]:
                random_choice = random.randint(MIN_CHOICE, MAX_CHOICE)
            possible_picks.append(random_choice)
    return possible_picks


if __name__ == "__main__":
        main()