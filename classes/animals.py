class Animal():
    """A simple representation of an animal."""

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_noise(self):
        print("WTF?!?")
    
    def present(self):
        print("This is an animal called " + self.name + " aged of "
        + str(self.age) + " years.")


class Dog(Animal):
    """A simple representation of a dog."""

    def __init__(self, name, age):
        super().__init__(name, age)

    def make_noise(self):
        print("Bark! Bark!")