operasi_hitung = input("Masukkan operasi hitung: ")
angka1 = input("masukkan angka pertama: ")
angka2 = input("masukkan angka kedua: ")

try:
    angka1 = float(angka1)
except ValueError:
    print("Input angka pertama salah")
    exit()

try:
    angka2 = float(angka2)
except ValueError:
    print("Input angka kedua salah")
    exit()

try:
    angka1 = int(angka1)
except ValueError:
    print("Input angka pertama salah")
    exit()

try:
    angka2 = int(angka2)
except ValueError:
    print("Input angka kedua salah")
    exit()


tambah = angka1 + angka2
kurang = angka1 - angka2
bagi = angka1 / angka2
kali = angka1 * angka2

if operasi_hitung == "+":
    print(tambah)
elif operasi_hitung == "-":
    print(kurang)
elif operasi_hitung == "/":
    print(bagi)
elif operasi_hitung == "*":
    print(kali)
else:
    print("Input operasi salah")