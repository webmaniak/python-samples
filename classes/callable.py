"""A callable Class (can be used almost like a function)."""

class Divider():

    def __init__(self, divider):
        self._divider = divider

    def __call__(self, number):
        return number / self._divider
        