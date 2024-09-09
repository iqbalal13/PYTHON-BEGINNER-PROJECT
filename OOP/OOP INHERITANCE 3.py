class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def speak(self):
        print("I am an animal")


class Dog(Animal):
    def __init__(self, name, species, breed):
        super().__init__(name, species)
        self.breed = breed

    def speak(self):
        print("Woof! I am a dog.")


class Cat(Animal):
    def __init__(self, name, species, color):
        super().__init__(name, species)
        self.color = color

    def speak(self):
        print("Meow! I am a cat.")


name = input("Enter the name of your dog: ")
species = input("Enter the species of your dog: ")
breed = input("Enter the breed of your dog: ")
dog = Dog(name, species, breed)

name = input("Enter the name of your cat: ")
species = input("Enter the species of your cat: ")
color = input("Enter the color of your cat: ")
cat = Cat(name, species, color)

print(dog.name)  # Output: (whatever the user entered for the dog's name)
print(cat.species)  # Output: (whatever the user entered for the cat's species)
dog.speak()  # Output: Woof! I am a dog.
cat.speak()  # Output: Meow! I am a cat.