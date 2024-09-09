class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def introduce(self):
        print("Hello, my name is", self.name, "and I am", self.age, "years old ", self.gender)

person1 = Person("John", 30, "male" )
person1.introduce()
