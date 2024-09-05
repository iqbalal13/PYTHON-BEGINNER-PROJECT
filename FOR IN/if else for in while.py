fruits = ["apple", "banana", "cherry"]

while True:
    search = input("Enter a fruit to search for (or type 'exit' to quit): ")

    if search.lower() == 'exit':
        break

    found = False
    for fruit in fruits:
        if fruit == search:
            print(f"{search} is in the list.")
            found = True
            break

    if not found:
        print(f"{search} is not in the list.")