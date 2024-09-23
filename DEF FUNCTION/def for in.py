def calculate_squares(numbers):
    """
    Calculates the square of each number in the given list.

    Parameters:
    - numbers (list): A list of numbers.

    Returns:
    - list: A new list containing the squares of the input numbers.
    """
    squares = []
    for number in numbers:
        square = number ** 2
        squares.append(square)
    return squares

# Example usage:
numbers_list = [1, 2, 3, 4, 5]
result = calculate_squares(numbers_list)
print("Original List:", numbers_list)
print("Squares:", result)