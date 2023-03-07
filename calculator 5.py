def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

# Display the menu
print("Select an operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

# Ask the user to enter their choice
choice = input("Enter choice (1/2/3/4): ")

# Ask the user to enter two numbers
num1 = input("Enter first number: ")
num2 = input("Enter second number: ")

try:
    num1 = float(num1)
except ValueError:
    print("Input angka pertama salah")
    exit()

try:
    num2 = float(num2)
except ValueError:
    print("Input angka kedua salah")
    exit()

try:
    num1 = int(num1)
except ValueError:
    print("Input angka pertama salah")
    exit()

try:
    num2 = int(num2)
except ValueError:
    print("Input angka kedua salah")
    exit()



# Perform the selected operation
if choice == '1':
    print(num1, "+", num2, "=", add(num1, num2))

elif choice == '2':
    print(num1, "-", num2, "=", subtract(num1, num2))

elif choice == '3':
    print(num1, "*", num2, "=", multiply(num1, num2))

elif choice == '4':
    print(num1, "/", num2, "=", divide(num1, num2))

else:
    print("Invalid input")