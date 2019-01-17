class Animal():
    """A simple representation of an animal."""

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_noise(self):
        print("WTF?!?")
    
    def present(self):
        print(str(self))

    def __str__(self):
        return f'This is an animal called {self.name}' \
                f' aged of {str(self.age)} years.'

    def __repr__(self):
        return f'{self.__class__.__name__}({self.name!r}, {self.age!r})'


class Dog(Animal):
    """A simple representation of a dog."""

    def __init__(self, name, age, breed):
        super().__init__(name, age)
        self.breed = breed

    def make_noise(self):
        print("Bark! Bark!")

    def __repr__(self):
        return f'{self.__class__.__name__}({self.name!r}, {self.age!r}, {self.breed!r})'