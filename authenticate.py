from argon2 import PasswordHasher  # Ensure you have done pip install argon2-cffi for this dependency to work

class Authenticate:
    ph = PasswordHasher()

    def auth_user(self, username, password):
        users_file = open("users.txt", "r")
        file_content = users_file.readlines()
        for line in file_content:
            line_split = line.split(":")
            file_username = line_split[0]
            hash = line_split[1]
            print(hash)
            if file_username == username:
                self.ph.verify(hash, password)


def main():
    authenticate = Authenticate()
    username = input("Enter username: ")
    password = input("Enter password: ")
    authenticate.auth_user(username, password)

main()