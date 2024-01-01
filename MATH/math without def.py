import random

print("Welcome to the Math Game!")

num_rounds = 3  # You can change this to the desired number of rounds

for _ in range(num_rounds):
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    operation = random.choice(['+', '-', '*'])
    expression = f"{num1} {operation} {num2}"
    correct_answer = eval(expression)

    print(f"Solve the following math problem: {expression}")

    user_answer = float(input("Your answer: "))

    if user_answer == correct_answer:
        print("Correct! Well done.")
    else:
        print(f"Sorry, the correct answer is {correct_answer}.")

print("Thanks for playing. Goodbye!")