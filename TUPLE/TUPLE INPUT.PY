# Accepting input from the user to create a tuple
input_str = input("Enter elements for the tuple separated by spaces: ")
input_list = input_str.split()  # Split the input string into a list of elements
my_tuple = tuple(input_list)  # Convert the list into a tuple

# Display the tuple
print("Tuple created:", my_tuple)

# Accessing elements in the tuple
index = int(input("Enter the index to access an element: "))
if 0 <= index < len(my_tuple):
    print("Element at index", index, "is:", my_tuple[index])
else:
    print("Invalid index")

# Iterating through the tuple
for item in my_tuple:
    print(item)

# Length of the tuple
print("Length of the tuple:", len(my_tuple))