class Animal:
    def __init__(self, name):
        self.name = name

class Dog(Animal):
    def bark(self):
        print("Woof woof!")

class Cat(Animal):
    def meow(self):
        print("Meow!")

dog = Dog("Fido")
cat = Cat("Whiskers")

print(isinstance(dog, Animal)) # Output: True
print(isinstance(cat, Animal)) # Output: True
print(isinstance(dog, Cat))    # Output: False