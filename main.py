from user import User
import json
import hashlib

# Constant value defining the name of the datafile
DATA_FILE = "users.json"

# The program runs until exited by the user
while True:
    # Sets out available options for the user
    menu = int(input("1) Log In\n2) Sign Up\n3) Delete Account\n4) Exit\n: "))

    # When the user decides to log in
    if menu == 1:
        # Asks for the username and password from the user
        username = input("Enter your username: ")
        password = input("Enter your password: ")

        # If the user does not exist
        user = None

        # If there are no errors, the program will run this code
        try:
            # Opens DATAFILE(user.json) in read mode
            with open(DATA_FILE, "r") as f:
                current_users = json.load(f)
                # Reads all the users in "current_users" as "i"
                for i in current_users:
                    # If the user's username equals their username, the variable "user" will equal the username
                    if i == username:
                        user = current_users[username]
        # If there is a "FileNotFoundError", pass
        except FileNotFoundError:
            pass

        # If there is no user, output an error message
        if not user:
            print("Username is not recognised.")
        # Otherwise, if the user's hashed password is equal to the hashed password stored in "users.json" output "Logged in"
        else:
            if user["password_hash"] == hashlib.sha3_512(f"{password}{user['salt']}".encode("UTF-8")).hexdigest():
                print("Logged in.")
                # Otherwise output an error message and do nothing
            else:
                print("Login unsuccessful.")

    # If the menu choice is equal to "2"
    elif menu == 2:
        # Store the users credentials in variables
        username = input("Enter a username: ")
        password = input("Enter a password: ")
        name = input("Enter your full name: ")

        # Make a "username_available" variable
        username_available = False

        # If there are no errors, continue with this code
        try:
            # Open "DATAFILE"(users.json) in read mode
            with open(DATA_FILE, "r") as f:
                for user in json.load(f):
                    # If the stored username is equal to what the user entered
                    if user == username:
                        # Error message
                        print("Username unavailable. Please try again.")
                        # Re-runs code from "while True:"
                        continue
                # The username is available
                username_available = True
        # Except any errors
        except:
            # The username is available
            username_available = True

        # Variable for new user
        new_user = User(username, name, password)

        # Make a "current_users" variable a dictionary
        current_users = {}

        # If there are no errors, run this code
        try:
            # Open "DATA_FILE"(users.json) in read mode
            with open(DATA_FILE, "r") as f:
                # Takes the json file and turns it into a dictionary
                current_users = json.load(f)
        # If there are any errors; pass
        except:
            pass

        # Open "DATA_FILE"(users.json) in write mode
        with open(DATA_FILE, "w+") as f:
            # The username in current users is equal to "new_user"
            current_users[username] = new_user.__dict__
            json.dump(current_users, f)

    # If menu choice is equal to 3:
    elif menu == 3:
        # Store users creds in variables
        username = input("Enter your username: ")
        password = input("Enter your password: ")

        # user does not exist
        user = None

        # If there are no errors
        try:
            # Open DATA_FILE(users.json) in read mode
            with open(DATA_FILE, "r") as f:
                # Takes the json file and turns it into a dictionary
                current_users = json.load(f)
                # Checks all the users in the current users dictionary
                for user in current_users:
                    # If the user is equal to username; user will be in the current users list as a username
                    if user == username:
                        user = current_users[username]
        # If there is a "FileNotFoundError" (meaning users.json does not exist or there are no users), continue the code
        except FileNotFoundError:
            pass

        # Not logged in
        logged_in = False

        # Output an error message if "user" is not equal to True
        if not user:
            print("Username is not recognised.")
        # Otherwise hash the password they entered and see if it matches with a pre-hashed password in users.json
        else:
            if user["password_hash"] == hashlib.sha3_512(f"{password}{user['salt']}".encode("UTF-8")).hexdigest():
                # Log in the user
                logged_in = True
            else:
                print("Login unsuccessful.")
                continue

        if logged_in:
            current_users = {}

            try:
                with open(DATA_FILE, "r") as f:
                    current_users = json.load(f)
            except:
                pass

            confirmation = input(
                "Are you sure you want to delete your account? Enter 'Y' for yes, else enter any other key: ").upper()

            if confirmation == "Y":
                del current_users[username]

                with open(DATA_FILE, "w+") as f:
                    json.dump(current_users, f)
                    print("Account deleted. Goodbye")
                    continue
            else:
                print("Request cancelled.")
                continue

    elif menu == 4:
        print("Goodbye.")
        break