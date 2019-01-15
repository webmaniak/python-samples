"""This file shows how to implement decorators."""

import functools

def uppercase_all(func):
    """Uppercases the result of a function."""
    #@functools.wraps(func)
    def wrapper():
        func_result = func()
        return func_result.upper()

    return wrapper

def prepare_to_greatness(func):
    """Makes an introduction before announcing the result of a function."""
    #@functools.wraps(func)
    def wrapper(*args, **kwargs):
        func_result = func(*args, **kwargs)
        return f'Result in 3... 2... 1... {func_result}'

    return wrapper

def trace(func):
    """Traces what a function does (args, name, exit)."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        func_name = func.__name__
        print(f'[TRACE] Triggering function {func_name}() with {args}, {kwargs}.')
        result = func(*args, **kwargs)
        print(f'[TRACE] Exited function {func_name}() with: {result}')

        return result

    return wrapper