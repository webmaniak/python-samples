import json

def greet_user():
    """Displays a short text to greet a logged in user"""
    username = load_user_data()
    if username != None:
        print("Welcome back, " + username)
    else:
        register_user()

def load_user_data():
    """Loads user data from a json file"""
    try:
        with open(filename) as file_obj:
            username = json.load(file_obj)
    except FileNotFoundError:
        return None
    else:
        return username

def register_user():
    """Registers an unknown user"""
    username = input("What's your name, dear? ")
    try:
        with open(filename, 'w') as file_obj:
            json.dump(username, file_obj)
            print("Hello, " + username + ", we'll make sure to remember you!")
    except FileNotFoundError:
        print("Sorry, we have a temporary issue, we can't register you yet.")

filename = 'data/user-prefs.json'

greet_user()

"""try:
     with open(filename) as file_obj:
        username = json.load(file_obj)
except FileNotFoundError:
    username = input("What's your name, dear? ")
    with open(filename, 'w') as file_obj:
        json.dump(username, file_obj)
        print("Hello, " + username + ", we'll make sure to remember you!")
else:
    print("Welcome back, " + username) """