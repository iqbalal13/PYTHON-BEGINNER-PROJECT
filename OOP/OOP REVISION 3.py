class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def introduce(self):
        print("Hello, my name is", self.name, "and I am", self.age, "years old", self.gender)

# Take user's input for name, age, and gender
name = input("What is your name? ")
gender = input("What is your gender? ")

# Use try-except block to handle the case when user inputs a string instead of an integer for age
while True:
    try:
        age = int(input("How old are you? "))
        break
    except ValueError:
        print("Please enter a valid integer for age.")

# Create an object of the Person class using user's input
person1 = Person(name, age, gender)
person1.introduce()