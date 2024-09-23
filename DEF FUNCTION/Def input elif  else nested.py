def greet():
    """This function takes user input for a name and prints a customized greeting."""
    name = input("Enter your name: ")

    # Check if the name is empty
    if not name:
        print("You didn't enter a name. Hello, mysterious person!")
    else:
        # Check if the name is a specific value
        if name.lower() == "alice":
            print("Hello, Alice! You have a special greeting.")
        elif name.lower() == "bob":
            print("Hey Bob! Nice to see you.")
        else:
            print(f"Hello, {name}!")

# Call the function
greet()