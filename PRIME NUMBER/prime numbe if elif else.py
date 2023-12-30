user_input_str = input("Enter a number: ")

if user_input_str.isdigit():
    user_input = int(user_input_str)

    if user_input < 2:
        print(f"{user_input} is not a prime number.")
    elif user_input == 2 or user_input == 3:
        print(f"{user_input} is a prime number.")
    elif user_input % 2 == 0 or user_input % 3 == 0:
        print(f"{user_input} is not a prime number.")
    else:
        is_prime = True
        divisor = 5

        while divisor * divisor <= user_input:
            if user_input % divisor == 0 or user_input % (divisor + 2) == 0:
                is_prime = False
                break
            divisor += 6

        if is_prime:
            print(f"{user_input} is a prime number.")
        else:
            print(f"{user_input} is not a prime number.")
else:
    print("Error: Please enter a valid integer.")