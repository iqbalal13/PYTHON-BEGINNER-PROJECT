n = int(input("Enter a number: "))

if n >= 0:
    for x in range(n):
        print(x)

else:
    for x in range(n, 0, 1):
        print(x)