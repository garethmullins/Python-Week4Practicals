

"""
A woeful security checker that checks the input against a list of strings contained in the username.txt file.
"""
__author__ = 'Gareth'


def main():
    # access the usernames
    username_list = open('usernames.txt', mode = 'r')
    username = input("Username: ")
    access_granted = False

    # check if the username provided is valid
    for line in username_list:
        if username in line:
            access_granted = True
    if access_granted:
        print("Access granted")
    else:
        print("Access denied")


if __name__ == "__main__":
        main()