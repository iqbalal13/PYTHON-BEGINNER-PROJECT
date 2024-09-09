class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def introduce(self):
        print("Hello, my name is", self.name, "and I am", self.age, "years old ", self.gender)

# Take user's input for name, age, and gender
name = str(input("What is your name? "))
age = int(input("How old are you? "))
gender = str(input("What is your gender? "))

# Create an object of the Person class using user's input
person1 = Person(name, age, gender)
person1.introduce()