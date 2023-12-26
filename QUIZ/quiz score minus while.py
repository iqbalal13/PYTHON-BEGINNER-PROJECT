def display_question(question, options):
    print(question)
    for i, option in enumerate(options, start=1):
        print(f"{i}. {option}")

def quiz_game(questions):
    score = 0
    question_index = 0
    total_questions = len(questions)

    while question_index < total_questions:
        question, options, correct_answer = questions[question_index]
        display_question(question, options)

        try:
            user_answer = int(input("Enter the number of your answer: "))
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
        except ValueError:
            print("Invalid input. Please enter a number.\n")
            score -= 1

        question_index += 1

    print(f"Quiz completed! Your final score: {score}/{total_questions}")

if __name__ == "__main__":
    # Define your quiz questions as tuples: (question, options, correct_answer)
    quiz_questions = [
        ("What is the capital of France?", ["Paris", "Berlin", "Rome", "Madrid"], "Paris"),
        ("Which planet is known as the Red Planet?", ["Earth", "Mars", "Venus", "Jupiter"], "Mars"),
        ("What is the largest mammal in the world?", ["Elephant", "Giraffe", "Blue Whale", "Hippopotamus"], "Blue Whale"),
    ]

    quiz_game(quiz_questions)