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

from functions import *
greet_kids("Josh")
print(make_list('list', 'array', 'collection', 'iterable'))