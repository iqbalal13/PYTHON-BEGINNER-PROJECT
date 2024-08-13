import random

def generate_math_problem():
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    operation = random.choice(['+', '-', '*'])
    expression = f"{num1} {operation} {num2}"
    return expression, eval(expression)

def main():
    print("Welcome to the Math Game!")

    while True:
        problem, correct_answer = generate_math_problem()

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

if __name__ == "__main__":
    main()