"""
A few use cases for functions defined in functions.py. (uncomment to execute)
"""

# ------------------------------
# Importing the "functions" module
# and using it the in a raw way
# ------------------------------

#import functions
#functions.greet("Alain")

# ------------------------------
# Importing the "functions" module
# with a custom name (i.e. "f")
# ------------------------------

#import functions as f
#f.greet("Alain")

# ------------------------------
# Importing part of the "functions" module
# and using only what's been imported
# ------------------------------

#from functions import greet, greet_kids
#greet("Alain")
#greet(name='Jeff') # will also work

#name = input("Please tell me your name: ")
#greet_kids(uppercase_first_letter(name))

# ------------------------------
# Importing only one function of the "functions" module
# and giving it an alias
# ------------------------------

#from functions import greet_kids as hey
#hey("Alain")

# ------------------------------
# Importing everything from the "functions" module
# and using it without aliases
# ------------------------------

#from functions import *

#greet_kids("Josh")
#print(make_list('list', 'array', 'collection', 'iterable'))
#make_pizza(10, 'tomato sauce', 'mozarella', 'ham', 'mushrooms')

# ------------------------------
# Demonstrating how functions ARE objects.
# ------------------------------


from functions import greet, change_case, make_formatted_list, get_talking_volume

say_hello = greet
greet("Tobias")
say_hello("Mark")

del greet # remove the access to the "greet" function
#greet("Monique") # will crash, as expected!
say_hello("Mirella") # still works and references functions.greet
print(f'The say_hello function points to {say_hello.__name__}\'s definition.')

# You can create a list of functions, since they are objects
list_of_funcs = [str.title, str.upper]
for func in list_of_funcs:
    print(func('arnold'))

# You can even pass functions as function parameters
print(change_case('Bilbo', str.upper))
print(change_case('Bilbo', str.lower))

formatted_list = make_formatted_list(str.upper, 'apple', 'banana', 'pear')
for fruit in formatted_list:
    print(f'- {fruit}')

# You can also get nested functions to execute something
speak_high = get_talking_volume(63)
speak_low = get_talking_volume(20)

print(speak_high('Let\'s go party'))
print(speak_low('Sshh, it\'s only ambiant sound'))

# ------------------------------
# 
# ------------------------------