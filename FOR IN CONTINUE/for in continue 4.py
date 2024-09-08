numbers = input("Enter a list of numbers separated by spaces: ")
numbers = [int(x) for x in numbers.split()]

for x in numbers:
    if x % 3 != 0:
        continue
    print(x)