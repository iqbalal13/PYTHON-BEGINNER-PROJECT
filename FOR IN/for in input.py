fruits = ["apple", "banana", "cherry"]
search = input("Enter a fruit to search for: ")

for fruit in fruits:
    if fruit == search:
        print(f"{search} is in the list.")
        break
else:
    print(f"{search} is not in the list.")