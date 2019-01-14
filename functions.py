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

def change_case(name, uppercasing_function):
    """"
    Use function passed in parameter to uppercase a name.
    A function getting a function in parameters is called higher-order function.
    """
    return uppercasing_function(name)

def whisper(text):
    """A function defining an inner function."""
    def to_lower(t):
        return t.lower() + '...'
    return to_lower(text)

def get_talking_volume(music_volume):
    """A function that will return the appropriate nested function based on a simple input."""
    def low(t):
        return t.lower() + '...'
    def high(t):
        return t.upper() + '!!!'
    
    if music_volume > 50:
        return high
    else:
        return low

def get_talking_volume2(text, music_volume):
    """An extended version of the 'get_talking_volume' function"""
    def low():
        return text.lower() + '...'
    def high():
        return text.upper() + '!!!'
    
    if music_volume > 50:
        return high
    else:
        return low

def make_multiplier(n):
    def multiply(x):
        return x * n

    return multiply

def make_list(*names):
    """Creates a list out of an undefined amount of names."""
    my_list = []
    for name in names:
        my_list.append(name)
    return my_list

def make_formatted_list(func, *names):
    """
    Creates a list with formatted names using the 'map' function.
    - list() creates a list
    - map() applies a function to multiple objects
    """
    return list(map(func, names))

def make_pizza(radius, *toppings):
    """Makes a tasty pizza (not a real one, come on!) and display what's on it."""

    diameter = radius * 2
    print("Thanks for your order, you'll shortly receive a " + str(diameter) + "cm pizza with:")

    for topping in toppings:
        print("- " + topping)

def reverse_string_generator(text):
    """Reverses a string using the generator function of Python."""
    length = len(text)
    for c in range(length - 1, -1, -1):
        yield text[c]