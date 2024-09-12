mobil = ""
while True:
  mobil = str(input("masukkan perintah: "))
  if mobil == "nyala":
    print("mobil menyala")
  elif mobil == "jalan":
    print("mobil melaju")
  elif mobil == "stop":
    print("mobil berhenti")
  elif mobil == "exit":
    print("anda keluar dari program")
    break
  else:
    print("Input Salah")
    quit()
