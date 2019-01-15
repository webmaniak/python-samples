"""This file shows how to use decorators."""

from decorators import uppercase_all, prepare_to_greatness, trace

@uppercase_all
def say_hello():
    return 'Hello World!'

@prepare_to_greatness
def greet(name):
    return f'Hello {name}!'

@trace
def monitor_me(name, age, city):
    """Introduce somebody (with trace enabled)"""
    return f'Hi, my name is {name}, I\'m {age} years old and live in {city}.'

def introduce(name, age, city):
    """Introduce somebody (without trace)"""
    return f'Hi, my name is {name}, I\'m {age} years old and live in {city}.'

print(say_hello())
print(greet('Jack'))
print(monitor_me('Simon', 26, 'London'))

# The following is also possible, yet not recommended:
decorated_intro = trace(introduce('Jane', 37, 'York'))
#decorated_intro()

# You can check a function's name and comment using:
print(f'Comment on the {introduce.__name__} function (no decorator): {introduce.__doc__}')
print(f'Comment on the {say_hello.__name__} function (decorator): {say_hello.__doc__}')
print(f'Comment on the {monitor_me.__name__} function (decorator + functools): {monitor_me.__doc__}')