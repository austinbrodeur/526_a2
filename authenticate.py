from argon2 import PasswordHasher  # Ensure you have done pip install argon2-cffi for this dependency to work
from argon2 import exceptions


class Authenticate:
    ph = PasswordHasher()

    def auth_user(self, username, password):
        """
        Authenticates the user by looking for their username and validating their password from the users file

        :param username:
        :param password:
        :return:
        """
        users_file = open("users.txt", "r")
        file_content = users_file.readlines()
        for line in file_content:
            try:
                line_split = line.split(":")
                file_username = line_split[0]
                hash = line_split[1]
                hash = hash.strip()
                if file_username == username:
                    if self.ph.verify(hash, password):
                        print("Access granted")
                        users_file.close()
                        return True
                    else:
                        print("Access denied")
                        users_file.close()
                        return False
            except IndexError:
                pass
            except exceptions.VerifyMismatchError:
                print("Access denied")
                users_file.close()
                return False
        print("Access denied")
        users_file.close()
        return False


def main():
    authenticate = Authenticate()
    username = input("Enter username: ")
    password = input("Enter password: ")
    authenticate.auth_user(username, password)

main()
