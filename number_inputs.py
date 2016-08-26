"""

"""


def main():
    numbers = []
    NUM_OF_NUMBERS = 5
    for i in range(0, NUM_OF_NUMBERS):
        numbers.append(int(input(" please enter number {} ".format(i + 1))))
    print("The first number is {}".format(numbers[0]))
    print("The last number is {}".format(numbers[NUM_OF_NUMBERS-1]))
    print("The smallest number is {}".format(min(numbers)))
    print("The largest number is {}".format(max(numbers)))
    print("The average of the numbers is {}".format(sum(numbers)/NUM_OF_NUMBERS))


if __name__ == "__main__":
        main()