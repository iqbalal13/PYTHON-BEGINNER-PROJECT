import random

x= random .randint(1,6)
y = random.random()

myList = ["rock","papaer", "scissors"]
z= random.choice(myList)

kartu = [1,2,3,4,5,6,7,8,12, "J","k","q","a"]

random.shuffle(kartu)

print(kartu)