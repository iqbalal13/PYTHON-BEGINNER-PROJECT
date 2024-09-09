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


dog = Dog("Fido", "Canis lupus familiaris", "Golden Retriever")
cat = Cat("Fluffy", "Felis catus", "Calico")

print(dog.name)  # Output: Fido
print(cat.species)  # Output: Felis catus
dog.speak()  # Output: Woof! I am a dog.
cat.speak()  # Output: Meow! I am a cat.