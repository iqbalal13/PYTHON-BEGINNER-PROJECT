n = int(input("Enter a number between 1 and 10: "))
for i in range(1, n+1):
    for j in range(1, n+1):
        if i == j:
            print("X", end=" ")
        else:
            print("O", end=" ")
    print()  