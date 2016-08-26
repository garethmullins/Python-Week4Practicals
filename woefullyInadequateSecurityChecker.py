"""
A woeful security checker that checks the input against a list of strings contained in the username.txt file.
"""
__author__ = 'Gareth'


def main():
    username_list = open('usernames.txt', mode = 'r')
    username = input("Username: ")
    temp = False
    for line in username_list:
        if username in line:
            temp = True
    if temp:
        print("Access granted")
    else:
        print("Access denied")


if __name__ == "__main__":
        main()