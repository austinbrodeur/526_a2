import re


class Enroll:
    dict_words = []

    def __init__(self):
        pass

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
        if not re.match("^[A-Za-z0-9!@#$%^&*()_+=:.,/|-]{8,100}$", password):
            print("Invalid password. Password must be between 8 and 100 characters long and only contain alphanumeric "
                  "characters and standard english keyboard symbols.")
            return False

        if re.match("^[0-9]*$", password):
            print("Invalid password. Password must contain letters.")
            return False
        elif re.sub('0-9', '', password) in self.dict_words:
            print("Invalid password. Password must not be a dictionary word or a dictionary word starting/ending with "
                  "numbers.")
            return False
        else:
            return True

    def parse_dict(self):
        f = open('words.txt', 'r')
        with open('words.txt') as f:
            self.dict_words = f.read().splitlines()
        f.close()

    def enroll_username(self):
        print("enroll user")

    def enroll_password(self):
        print("enroll pass")
