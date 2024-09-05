n = int(input("Enter a number: "))

if n >= 0:
    for x in range(1, n):
        print(x)
elif n < 0:
    for x in range(n+1, 0, 1):
        print(x)
else:
    print("Invalid input")