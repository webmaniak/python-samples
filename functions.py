# ------------------------------
# Functions
# ------------------------------

def greet(name):
    """Say hello to the given name."""
    print("Hello, " + name + "!")

def greet_kids(name, isnice = True):
    """Say hello to a given name, and compliments if he/she is nice."""
    greet(name)
    if isnice:
        print("You are a nice person.")
    else:
        print("You may need to be more gentle this year...")

def uppercase_first_letter(name):
    """Uppercases the given string."""
    return name.title()

def make_list(*names):
    """Creates a list out of an undefined amount of names."""
    my_list = []
    for name in names:
        my_list.append(name)
    return my_list

def make_pizza(radius, *toppings):
    """Makes a tasty pizza (not a real one, come on!) and display what's on it."""

    diameter = radius * 2
    print("Thanks for your order, you'll shortly receive a " + str(diameter) + "cm pizza with:")

    for topping in toppings:
        print("- " + topping)
