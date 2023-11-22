# Question 1:
x = 10
y = 5

answer_q1 = input("Q1: If x > y, what will be the output? \n a) x is greater than y \n b) y is greater than x \n Your answer: ")

if answer_q1.lower() == "a":
    print("Correct! x is greater than y.")
else:
    print("Incorrect. The correct answer is a) x is greater than y.")

# Question 2:
number = 15

answer_q2 = input("Q2: Is the number even or odd? \n a) Even \n b) Odd \n Your answer: ")

if answer_q2.lower() == "b":
    print("Correct! 15 is an odd number.")
else:
    print("Incorrect. The correct answer is b) Odd.")

# Question 3:
age = 25

answer_q3 = input("Q3: Based on the age, is the person a minor, adult, or senior citizen? \n a) You are a minor. \n b) You are an adult. \n c) You are a senior citizen. \n Your answer: ")

if answer_q3.lower() == "b":
    print("Correct! A 25-year-old is considered an adult.")
else:
    print("Incorrect. The correct answer is b) You are an adult.")