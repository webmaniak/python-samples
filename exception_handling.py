"""This file's aim is to demonstrate how to handle exceptions in Python."""

# Add the "classes/" subdirectory to the path accessible by this script
# This needs to be done if your subdirectory doesn't contain a __init__.py file
#import sys
#sys.path.append('classes/')

from classes.custom_exception import MyCustomError, UnhandledCustomError
import traceback
import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

print("------------------------------")
print("Exception handling")
print("------------------------------")

def divide(number, divider):
    """Divides a number by a divider, without proper exception handling."""

    if(isinstance(number, int)):
        if (isinstance(divider, int)):
            return number / divider

def divide_safely(number, divider):
    """Divides a number by a divider, with exception handling."""

    if(isinstance(number, int)):
        if (isinstance(divider, int)):
            try:
                return number / divider
            except ZeroDivisionError:
                print('You cannot divide by 0!')
                return -1

def parent_function():
    """Calls a nested function and manage the exception it will eventually raise."""

    try:
        nested_function()
    except MyCustomError as mce:
        print('This is an exception managed by the parent function: (' + type(mce).__name__ + ') ' + mce.message)

def alt_parent_function():
    """Calls a nested function and throws the exception again."""

    try:
        nested_function()
    except MyCustomError as mce:
        raise UnhandledCustomError('Raised because of MCE.') from mce

def nested_function():
    """Executes an unsafe function and throw the error further."""

    try:
        divide(5, 0)
    except ZeroDivisionError:
        # we're not managing this exception here for test purposes
        raise MyCustomError('Seems like we cannot divide by zero after all')

# ------------------------------
# Bad exception management
# (will crash with ZeroDivisionError)
# ------------------------------

#print('5 / 0 = ' + str(divide(5, 0)))

# ------------------------------
# Better exception management
# (will handle ZeroDivisionError)
# ------------------------------

result = 0
try:
    result = divide(5, 0)
except ZeroDivisionError:
    print('Oops, you cannot divide by 0!')
else:
    print('There was no exception, hurray!')
    print('5 / 0 = ' + str())
finally:
    print('Finished division.')

# ------------------------------
# Even better exception management
# (will handle ZeroDivisionError at origin)
# ------------------------------

print('5 / 0 = ' + str(divide_safely(5, 0)))

# ------------------------------
# Demo with nested functions as well
# ------------------------------

parent_function() # it will manage the error raised by its nested function

# Here's some example of logging errors:
print('-----')
try:
    alt_parent_function()
except UnhandledCustomError as uce:
    logger.log(logging.INFO,'Unhandled custom error raised: ' + uce.message)
    logger.exception(uce)
    