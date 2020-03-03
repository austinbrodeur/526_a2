import re
import sys
import os
from argon2 import PasswordHasher  # Ensure you have done pip install argon2-cffi for this dependency to work


class Enroll:
    dict_words = []
    password_file = None
    ph = PasswordHasher()

    def __init__(self):
        with open('words.txt') as words_file:
            self.dict_words = words_file.read().splitlines()
        words_file.close()

    def check_username_valid(self, username):
        """
        Checks that the username is good (alphanumeric chars and underscores only, between 5 and 15 chars) before
        enrolling. I picked the range of 5-15 arbitrarily, but I felt allowing usernames to be very short or very
        long is a poor idea. Returns True is username is valid.

        :param username:
        :return:
        """
        if re.match("^[A-Za-z0-9_]{5,15}$", username):
            return True
        else:
            print("Invalid username. Username must only contain letters, numbers and underscores and must be between "
                  "5 and 15 characters long.")
            return False

    def check_password_valid(self, password):
        """
        Checks that the password entered is good before enrolling. Again, I arbitrarily picked lengths between 8 and
        100 (the long max length is to support secure password generators). Returns True if password is valid.

        :param password:
        :return:
        """
        stripped_password = re.sub('\d', '', password)

        if not re.match("^[A-Za-z0-9!@#$%^&*()_+=:.,/|-]{8,100}$", password):
            print("Invalid password. Password must be between 8 and 100 characters long and only contain alphanumeric "
                  "characters and standard english keyboard symbols.")
            return False

        if re.match("^[0-9]*$", password):
            print("Invalid password. Password must contain letters.")
            return False
        elif stripped_password in self.dict_words:
            print("Invalid password. Password must not be a dictionary word or a dictionary word starting/ending with "
                  "numbers.")
            return False
        else:
            return True

    def check_for_user(self, username):
        """
        Checks that the username chosen has not already been registered. Returns True if username is in use.

        :param username:
        :return:
        """
        users_file = open("users.txt", "r")
        file_content = users_file.readlines()
        for line in file_content:
            try:
                check_username = line.split(":")[0]
                if check_username == username:
                    print("Username already in use")
                    users_file.close()
                    return True
            except IndexError:
                pass
        users_file.close()
        return False

    def enroll_user(self, username, password):
        """
        Securely enrolls a new user into the user database

        :param username:
        :param password:
        :return:
        """
        if not os.path.isfile("users.txt"):
            users_file = open("users.txt", "w+")
            users_file.write("\n")
            users_file.close()

        if not self.check_username_valid(username): # split if statements for easier debugging
            print("rejected")
            sys.exit(-1)
        if not self.check_password_valid(password):
            print("rejected")
            sys.exit(-1)
        if self.check_for_user(username):
            print("rejected")
            sys.exit(-1)
        else:

            users_file_append = open("users.txt", "a")
            hashed_password = self.ph.hash(password)

            users_file_append.write(username + ":" + hashed_password + "\n")

            print("accepted")
            users_file_append.close()
            sys.exit(0)
