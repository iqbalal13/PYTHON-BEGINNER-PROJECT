import time

class QuizGame:
    def __init__(self):
        self.questions = [
            {"question": "What is the capital of France?", "options": ["Paris", "Berlin", "London"], "answer": "Paris"},
            {"question": "Which planet is known as the Red Planet?", "options": ["Mars", "Venus", "Jupiter"], "answer": "Mars"},
            {"question": "What is the largest mammal?", "options": ["Elephant", "Blue Whale", "Giraffe"], "answer": "Blue Whale"}
            # Add more questions as needed
        ]
        self.score = 0
        self.time_limit = 10  # Time limit per question in seconds

    def ask_question(self, question_data):
        print(question_data["question"])
        for i, option in enumerate(question_data["options"], start=1):
            print(f"{i}. {option}")

    def run_quiz(self):
        print("Welcome to the Quiz Game!")
        time.sleep(1)

        for i in range(len(self.questions)):
            question_data = self.questions[i]
            self.ask_question(question_data)

            start_time = time.time()
            user_answer = input("Your answer (enter the option number): ")

            user_answer_index = int(user_answer) - 1 if user_answer.isdigit() else -1
            selected_option = question_data["options"][user_answer_index] if 0 <= user_answer_index < len(question_data["options"]) else None

            if selected_option is None:
                print("Invalid input. Skipping to the next question.\n")
            else:
                if selected_option == question_data["answer"]:
                    print("Correct! You earned 1 point.\n")
                    self.score += 1
                else:
                    print(f"Wrong! The correct answer is {question_data['answer']}\n")

            elapsed_time = time.time() - start_time
            time_left = max(0, self.time_limit - elapsed_time)
            print(f"Time left: {time_left:.2f} seconds\n")
            time.sleep(1)  # Add a pause before the next question

        print("Quiz completed!")
        print(f"Your final score: {self.score}")

if __name__ == "__main__":
    quiz_game = QuizGame()
    quiz_game.run_quiz()