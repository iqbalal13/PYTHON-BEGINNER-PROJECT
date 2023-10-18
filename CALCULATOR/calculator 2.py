operasi_hitung = input("Masukkan operasi hitung: ")
angka1 = float(input("masukkan angka pertama: "))
angka2 = float(input("masukkan angka kedua: "))
tambah = angka1 + angka2
kurang = angka1 - angka2
bagi = angka1 / angka2
kali = angka1 * angka2

if operasi_hitung == "+":
    print(tambah)
elif operasi_hitung == "-":
    print(kurang)
elif operasi_hitung == "'/":
    print(bagi)
elif operasi_hitung == "*":
    print(kali)
else:
    print("input salah ")