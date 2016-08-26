"""
A lottery ticket creater and picker that accepts the maximum, minimum numbers allowed, the number of unique numbers
to be used and the number of numbers that are being chosen.
"""
import random
__author__ = 'Gareth'


def main():
    NUM_OF_CHOICES = 6
    MIN_CHOICE = 1
    MAX_CHOICE = 45
    ticket_numbers = []
    num_of_quick_picks = int(input("How many quick picks? "))

    ticket_numbers = randomize_choices(MAX_CHOICE, MIN_CHOICE, NUM_OF_CHOICES, num_of_quick_picks, ticket_numbers)
    ticket_numbers = reorder(NUM_OF_CHOICES, num_of_quick_picks, ticket_numbers)
    picks = quick_pick_indexs(ticket_numbers, NUM_OF_CHOICES, num_of_quick_picks)

    print_ticket(NUM_OF_CHOICES, num_of_quick_picks, ticket_numbers)

    print("Your quick picks are {}".format(picks))


def reorder(NUM_OF_CHOICES, num_of_quick_picks, ticket_numbers):
    # Reorder the ticket numbers one row, one number at a time.
    for i in range(0, num_of_quick_picks):
        for j in range(0, NUM_OF_CHOICES - 1):
            # The index of the smallest number is found
            min_index = ticket_numbers.index(min(ticket_numbers[(i * NUM_OF_CHOICES) + j:(i + 1) * NUM_OF_CHOICES]),
                                             i * NUM_OF_CHOICES)
            # Check that the smallest number isn't going to be the one changed.
            if min_index != j + (i * NUM_OF_CHOICES):
                # The the number that is to be changed is backed up for the origin of the smallest number.
                number_backup = ticket_numbers[j + (i * NUM_OF_CHOICES)]
                ticket_numbers[j + (i * NUM_OF_CHOICES)] = ticket_numbers[min_index]
                # With the smallest number moved, the number it replaced is moved to it's origin.
                ticket_numbers[min_index] = number_backup
    return ticket_numbers


def print_ticket(NUM_OF_CHOICES, num_of_quick_picks, ticket_numbers):
    print()
    for i in range(0, num_of_quick_picks):
        for j in range(0, NUM_OF_CHOICES - 1):
            print("{:2} ".format(ticket_numbers[i * NUM_OF_CHOICES + j]), end=" ")
        print()
    print()


def quick_pick_indexs(ticket_numbers, NUM_OF_CHOICES, num_of_quick_picks):
    picks = []
    # Randomly pick a number from each row of the ticket
    for i in range(0, num_of_quick_picks):
        picks.append(ticket_numbers[random.randint(0, NUM_OF_CHOICES - 1) + i * NUM_OF_CHOICES])
    return picks


def randomize_choices(MAX_CHOICE, MIN_CHOICE, NUM_OF_CHOICES, num_of_quick_picks, ticket_numbers):
    # Randomly create a set of unique numbers a row at a time, adding them to the ticket.
    for i in range(0, num_of_quick_picks):
        random_choice = random.randint(MIN_CHOICE, MAX_CHOICE)
        for j in range(0, NUM_OF_CHOICES):
            while random_choice in ticket_numbers[i * NUM_OF_CHOICES:]:
                random_choice = random.randint(MIN_CHOICE, MAX_CHOICE)
            ticket_numbers.append(random_choice)
    return ticket_numbers


if __name__ == "__main__":
        main()