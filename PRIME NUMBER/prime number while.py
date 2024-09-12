user_input_str = input("Enter a number: ")

if user_input_str.isdigit():
    user_input = int(user_input_str)

    if user_input < 2:
        print(f"{user_input} is not a prime number.")
    elif user_input == 2:
        print(f"{user_input} is a prime number.")
    else:
        is_prime = True
        divisor = 2

        while divisor <= user_input ** 0.5:
            if user_input % divisor == 0:
                is_prime = False
                break
            divisor += 1

        if is_prime:
            print(f"{user_input} is a prime number.")
        else:
            print(f"{user_input} is not a prime number.")
else:
    print("Error: Please enter a valid integer.")