import time

questions = [
    ("What is the capital of France?", ["Paris", "Berlin", "Rome", "Madrid"], "Paris"),
    ("Which planet is known as the Red Planet?", ["Earth", "Mars", "Venus", "Jupiter"], "Mars"),
    ("What is the largest mammal in the world?", ["Elephant", "Giraffe", "Blue Whale", "Hippopotamus"], "Blue Whale"),
]

score = 0
total_questions = len(questions)

question_index = 0

if total_questions >= 1:
    question, options, correct_answer = questions[question_index]
    print(question)

    option_index = 1
    if len(options) >= 1:
        print(f"{option_index}. {options[option_index - 1]}")
        user_input = input("Enter the number of your answer: ")

        if user_input.isdigit():
            user_answer = int(user_input)
            if 1 <= user_answer <= len(options):
                user_choice = options[user_answer - 1]
                if user_choice == correct_answer:
                    print("Correct! You get +1 point.\n")
                    score += 1
                else:
                    print(f"Wrong! The correct answer is: {correct_answer}. You get -1 point.\n")
                    score -= 1
            else:
                print("Invalid choice. Please enter a valid number.\n")
                score -= 1
        else:
            print("Invalid input. Please enter a number.\n")
            score -= 1

    question_index += 1

print(f"Quiz completed! Your final score: {score}/{total_questions}")