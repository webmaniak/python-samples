"""Shows how to implement a custom exception"""

class MyCustomError(Exception):
    
    def __init__(self, message):
        self.message = message

class UnhandledCustomError(Exception):
    pass
