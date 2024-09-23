def check_value_type(value):
    if isinstance(value, int):
        print("The value is an integer.")
    elif isinstance(value, float):
        print("The value is a float.")
    elif isinstance(value, str):
        print("The value is a string.")
    elif isinstance(value, list):
        print("The value is a list.")
    elif isinstance(value, dict):
        print("The value is a dictionary.")
    elif isinstance(value, tuple):
        print("The value is a tuple.")
    elif isinstance(value, bool):
        print("The value is a boolean.")
    elif isinstance(value, set):
        print("The value is a set.")
    else:
        print("Unknown type.")

# Example usage:
check_value_type(42)         # Output: The value is an integer.
check_value_type(3.14)       # Output: The value is a float.
check_value_type("hello")    # Output: The value is a string.
check_value_type([1, 2, 3])   # Output: The value is a list.
check_value_type({'a': 1})    # Output: The value is a dictionary.
check_value_type((1, 2, 3))   # Output: The value is a tuple.
check_value_type(True)        # Output: The value is a boolean.
check_value_type({1, 2, 3})    # Output: The value is a set.
check_value_type(None)        # Output: