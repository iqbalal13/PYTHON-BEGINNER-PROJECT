import random

def ask_question(question, options, correct_option):
    print(question)
    for i, option in enumerate(options, start=1):
        print(f"{chr(64 + i)}. {option}")

    while True:
        user_input = input("Enter the letter of your answer (or 'skip' to skip the question): ").upper()

        if user_input == 'SKIP':
            return 0  # Player chose to skip the question
        elif user_input in [chr(i) for i in range(65, 65 + len(options))]:
            break
        else:
            print("Invalid input. Please enter a valid letter or 'skip'.")

    user_answer = ord(user_input) - 64
    return 1 if user_answer == correct_option else -1

def run_quiz(questions):
    score = 0
    random.shuffle(questions)

    for i, (question, options, correct_option) in enumerate(questions, start=1):
        print(f"\nQuestion {i}:")
        result = ask_question(question, options, correct_option)
        
        if result == 1:
            print("Correct! +1 point\n")
            score += 1
        elif result == -1:
            print(f"Wrong! The correct answer was {chr(64 + correct_option)}: {options[correct_option - 1]}. -1 point\n")
            score -= 1
        else:
            print("Question skipped. 0 points\n")

    print(f"Quiz completed! Your final score: {score}/{len(questions)}")

if __name__ == "__main__":
    quiz_questions = [
        ("What is the capital of France?", ["Paris", "Berlin", "Madrid", "Rome"], 1),
        ("Which planet is known as the Red Planet?", ["Earth", "Mars", "Jupiter", "Venus"], 2),
        ("What is the largest mammal in the world?", ["Elephant", "Blue Whale", "Giraffe", "Hippopotamus"], 2),
        # Add more questions as needed
    ]

    run_quiz(quiz_questions)