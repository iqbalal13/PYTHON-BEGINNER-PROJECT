def check_even_odd(number):
    if number % 2 == 0:
        result = "even"
    else:
        result = "odd"
    return result

# Example usage:
num = 7
result_str = check_even_odd(num)
print(f"The number {num} is {result_str}.")