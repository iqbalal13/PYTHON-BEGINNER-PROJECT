mobil = ""
while mobil != "exit":
  mobil = str(input("masukkan perintah: "))
  if mobil == "nyala":
    print("mobil menyala")
  elif mobil == "jalan":
    print("mobil melaju")
  elif mobil == "stop":
    print("mobil berhenti")
  else:
    print("Input Salah")

