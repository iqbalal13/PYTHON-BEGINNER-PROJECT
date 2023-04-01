import random

pemain_score = 0
cpu_score = 0
pilihan =  ["gunting", "kertas", "batu"]
while True:
    pemain_input = input("Gunting, Kertas, Batu, plih salah satu atau pilih q untuk keluar ")
    if pemain_input == "q":
        break
    if pemain_input not in pilihan:
        print("tidak ada dipilihan")
        continue
    
    random_pilihan = random.randint(0, 2)
    cpu_pilih = pilihan[random_pilihan]
    print("cpu pilih", cpu_pilih)

    if pemain_input == "batu" and cpu_pilih == "gunting":
        print("kamu menang !")
        pemain_score += 1
    elif pemain_input == "batu" and cpu_pilih == "batu":
        print("seri!!")
        pemain_score += 0
    elif pemain_input == "kertas" and cpu_pilih == "kertas":
        print("seri!!")
        pemain_score += 0
    elif pemain_input == "gunting" and cpu_pilih == "gunting":
        print("seri!!")
        pemain_score += 0
    elif pemain_input == "batu" and cpu_pilih == "kertas":
        print("kamu kalah")
        cpu_score += 1
    elif pemain_input == "kertas" and cpu_pilih == "batu":
        print("kamu menang")
        pemain_score += 1
    elif pemain_input == "gunting" and cpu_pilih == "batu":
        print("kamu kalah")
        cpu_score += 1
    else:
        print("input salah")
if pemain_score > cpu_score:
       print("kamu menang " + str(pemain_score) +" kali")
if pemain_score < cpu_score:
       print("kamu kalah" + str(cpu_score) +" kali")
if pemain_score == cpu_score:
       print("hasil seri")