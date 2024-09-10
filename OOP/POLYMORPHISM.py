class Animal:
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        pass


class Dog(Animal):
    def make_sound(self):
        print(self.name + " says woof woof!!")


class Cat(Animal):
    def make_sound(self):
        print(self.name + " says meow!!")


dog1 = Dog("Max")
cat1 = Cat("Fluffy")

dog1.make_sound()
cat1.make_sound()