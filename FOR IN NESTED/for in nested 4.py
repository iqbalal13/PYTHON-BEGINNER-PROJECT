n = int(input("Enter a value for n: "))

for i in range(n+1):
    for j in range(n+1):
        print(f"({i}, {j})", end=" ")
    print()