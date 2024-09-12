count = int(input("masukkan perintah: "))

while True:
    if count % 2 == 0:
        print(count, "is even")
    else:
        print(count, "is odd")
    count += 1
    if count > 10:
        quit()