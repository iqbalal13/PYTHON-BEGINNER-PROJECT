while True:
    score = 0
    print("Welcome to the Quiz Game!")
    print("Answer the following questions with 'A', 'B', or 'C'.")
    print("Let's get started!")

    # Question 1
    print("\nQuestion 1: What is the capital of France?")
    print("A. London")
    print("B. Berlin")
    print("C. Paris")

    answer1 = input("Your answer: ")

    if answer1.lower() == "c":
        print("Correct!")
        score += 1
    else:
        print("Incorrect.")
        if answer1.lower() == "a":
            print("The correct answer is 'C. Paris'.")
        elif answer1.lower() == "b":
            print("The correct answer is 'C. Paris'.")

    # Question 2
    print("\nQuestion 2: Which planet is known as the Red Planet?")
    print("A. Mars")
    print("B. Venus")
    print("C. Jupiter")

    answer2 = input("Your answer: ")

    if answer2.lower() == "a":
        print("Correct!")
        score += 1
    else:
        print("Incorrect.")
        if answer2.lower() == "b":
            print("The correct answer is 'A. Mars'.")
        elif answer2.lower() == "c":
            print("The correct answer is 'A. Mars'.")

    # Question 3
    print("\nQuestion 3: What is the largest mammal in the world?")
    print("A. Elephant")
    print("B. Blue Whale")
    print("C. Giraffe")

    answer3 = input("Your answer: ")

    if answer3.lower() == "b":
        print("Correct!")
        score += 1
    else:
        print("Incorrect.")
        if answer3.lower() == "a":
            print("The correct answer is 'B. Blue Whale'.")
        elif answer3.lower() == "c":
            print("The correct answer is 'B. Blue Whale'.")

    # Display the final score
    print("\nQuiz complete! Your score is:", score, "out of 3.")
    
    play_again = input("Do you want to play again? (yes/no): ")
    if play_again.lower() != "yes":
        break