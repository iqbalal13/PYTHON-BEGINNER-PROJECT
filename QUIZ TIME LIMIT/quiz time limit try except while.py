import random
import time

def generate_question():
    num1 = random.randint(1, 20)
    num2 = random.randint(1, 20)
    operator = random.choice(['+', '-'])
    question = f"{num1} {operator} {num2}"
    correct_answer = eval(question)  # Evaluate the expression to get the correct answer
    return question, correct_answer

def display_intro():
    print(f"Welcome to the Math Quiz! You have {quiz_time_limit} seconds.")
    input("Press Enter to start the quiz.")

def get_user_input():
    try:
        user_input = input("Your answer (type 'skip' to skip, 'quit' to quit): ")
        return user_input.lower()
    except ValueError:
        return None

def process_question(question, correct_answer):
    global score
    print(f"\nQuestion: {question}")

    user_input = get_user_input()

    if user_input == 'quit':
        print("\nQuiz terminated. Your current score:", score)
        return True
    elif user_input == 'skip':
        print("Question skipped. Score reset to 0.\n")
        score = 0
        return False
    elif user_input.isdigit():
        user_answer = int(user_input)

        if user_answer == correct_answer:
            print("Correct! You get +1 point.\n")
            score += 1
        else:
            print(f"Wrong! The correct answer is: {correct_answer}. You get -1 point.\n")
            score -= 1
    else:
        print("Invalid input. Please enter a number, 'skip', or 'quit'.\n")

    return False

quiz_time_limit = 30  # Set the time limit for the quiz in seconds
number_of_questions = 10  # Set the number of questions in the quiz

score = 0
start_time = time.time()

display_intro()

question_index = 0
while question_index < number_of_questions:
    question, correct_answer = generate_question()
    should_break = process_question(question, correct_answer)

    if should_break:
        break

    elapsed_time = time.time() - start_time
    if elapsed_time >= quiz_time_limit:
        print(f"\nTime's up! Quiz completed.")
        break

    question_index += 1

print(f"\nYour final score: {score}/{number_of_questions}")