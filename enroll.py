import re
import sys
import secrets
from argon2 import PasswordHasher # Ensure you have done pip install argon2-cffi for this dependency to work


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
        Ensures that the username is good (alphanumeric chars and underscores only, between 5 and 15 chars) before
        enrolling. I picked the range of 5-15 arbitrarily, but I felt allowing usernames to be very short or very
        long is a poor idea.

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
        Ensures that the password entered is good before enrolling. Again, I arbitrarily picked lengths between 8 and
        100 (the long max length is to support secure password generators).

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

    def enroll_user(self, username, password):
        users_file = open("users.txt", "w+")
        users_file.close()
        users_file = open("users.txt", "a")

        if self.check_username_valid(username) and self.check_password_valid(password):
            hashed_password = self.ph.hash(password) # According to the argon2 docs, the passwords are automatically
            # salted and stretched via this library, so no code is included to do so manually (I'd probably make a
            # mistake doing it manually anyways)

            users_file.write(username + ":" + hashed_password + "\n")

            print("accepted")
            users_file.close()
            sys.exit(0)
        else:
            print("rejected")
            users_file.close()
            sys.exit(-1)
