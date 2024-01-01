import random

print("Welcome to the Math Game!")

while True:
    num_rounds = 3  # You can change this to the desired number of rounds

    # List to store tuples of math problems and correct answers
    problems_and_answers = []

    for _ in range(num_rounds):
        num1 = random.randint(1, 10)
        num2 = random.randint(1, 10)
        operation = random.choice(['+', '-', '*'])
        expression = f"{num1} {operation} {num2}"
        correct_answer = eval(expression)

        problems_and_answers.append((expression, correct_answer))

    for problem, correct_answer in problems_and_answers:
        print(f"Solve the following math problem: {problem}")

        user_answer = float(input("Your answer: "))

        if user_answer == correct_answer:
            print("Correct! Well done.")
        else:
            print(f"Sorry, the correct answer is {correct_answer}.")

    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again != 'yes':
        print("Thanks for playing. Goodbye!")
        break