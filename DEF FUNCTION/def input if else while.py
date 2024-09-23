def greet():
    """This function takes user input for a name and prints a customized greeting."""
    while True:
        name = input("Enter your name (or type 'exit' to end): ")

        # Check if the user wants to exit
        if name.lower() == 'exit':
            print("Goodbye!")
            break  # Exit the loop if the user types 'exit'

        # Check if the name is empty
        if not name:
            print("You didn't enter a name. Hello, mysterious person!")
        elif name.lower() == "alice":
            print("Hello, Alice! You have a special greeting.")
        elif name.lower() == "bob":
            print("Hey Bob! Nice to see you.")
        else:
            print(f"Hello, {name}!")

# Call the function
greet()