# Question 1:
answer_q1 = input("Q1: What is the capital of France? \n a) Paris \n b) Rome \n c) Berlin \n Your answer: ")

if answer_q1.lower() == "a":
    print("Correct! Paris is the capital of France.")
else:
    if answer_q1.lower() == "b":
        print("Incorrect. Rome is not the capital of France.")
    elif answer_q1.lower() == "c":
        print("Incorrect. Berlin is not the capital of France.")
    else:
        print("Invalid input. Please choose a, b, or c.")

# Question 2:
answer_q2 = input("Q2: Which programming language is known for its readability and simplicity? \n a) Java \n b) Python \n c) C++ \n Your answer: ")

if answer_q2.lower() == "b":
    print("Correct! Python is known for its readability and simplicity.")
else:
    if answer_q2.lower() == "a":
        print("Incorrect. Java is not the language known for its readability and simplicity.")
    elif answer_q2.lower() == "c":
        print("Incorrect. C++ is not the language known for its readability and simplicity.")
    else:
        print("Invalid input. Please choose a, b, or c.")

# Question 3:
answer_q3 = input("Q3: What is the result of 2 + 3 * 4? \n a) 20 \n b) 14 \n c) 18 \n Your answer: ")

if answer_q3.lower() == "c":
    print("Correct! The result of 2 + 3 * 4 is 14.")
else:
    if answer_q3.lower() == "a":
        print("Incorrect. The result of 2 + 3 * 4 is not 20.")
    elif answer_q3.lower() == "b":
        print("Incorrect. The result of 2 + 3 * 4 is not 14.")
    else:
        print("Invalid input. Please choose a, b, or c.")