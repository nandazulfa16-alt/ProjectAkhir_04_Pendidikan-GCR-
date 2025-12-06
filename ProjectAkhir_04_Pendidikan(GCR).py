pengguna = {}             
daftar_kelas = []         
daftar_tugas = []         
pengumpulan_tugas = []   

# register
def daftar():
    print("\n=== DAFTAR AKUN ===")
    username = input("Username: ")
    if username in pengguna:
        print("Username sudah dipakai!")
        return
    
    password = input("Password: ")
    peran = input("Peran (guru/siswa): ").lower()

    if peran not in ["guru", "siswa"]:
        print("Peran tidak valid!")
        return

    pengguna[username] = {"password": password, "peran": peran}
    print("Akun berhasil dibuat!\n")


# login
def masuk():
    print("\n=== LOGIN ===")
    username = input("Username: ")
    password = input("Password: ")

    if username in pengguna and pengguna[username]["password"] == password:
        print(f"Login berhasil sebagai {pengguna[username]['peran']}\n")
        return username
    else:
        print("Login gagal!")
        return None


# menu guru 
def menu_guru(username):
    while True:
        print("=== MENU GURU ===")
        print("1. Buat Kelas")
        print("2. Lihat Kelas")
        print("3. Edit Kelas")
        print("4. Hapus Kelas")
        print("5. Buat Tugas")
        print("6. Lihat Tugas")
        print("7. Edit Tugas")
        print("8. Hapus Tugas")
        print("9. Lihat Pengumpulan Tugas")
        print("10. Logout")
        pilihan = input("Pilih menu: ")

        if pilihan == "1": buat_kelas(username)
        elif pilihan == "2": lihat_kelas_guru(username)
        elif pilihan == "3": edit_kelas(username)
        elif pilihan == "4": hapus_kelas(username)
        elif pilihan == "5": buat_tugas(username)
        elif pilihan == "6": lihat_tugas_guru(username)
        elif pilihan == "7": edit_tugas(username)
        elif pilihan == "8": hapus_tugas(username)
        elif pilihan == "9": lihat_pengumpulan(username)
        elif pilihan == "10": break


# CRUD kelas (guru)
def buat_kelas(username):
    nama = input("Nama kelas: ")
    kelas_id = len(daftar_kelas) + 1

    daftar_kelas.append({
        "kelas_id": kelas_id,
        "nama": nama,
        "guru": username,
        "siswa": []
    })

    print(f"Kelas '{nama}' berhasil dibuat!\n")

# melihat kelas (guru)
def lihat_kelas_guru(username):
    print("\n=== KELAS ANDA ===")
    for k in daftar_kelas:
        if k["guru"] == username:
            print(f"{k['kelas_id']}. {k['nama']} (Siswa: {len(k['siswa'])})")
    print("")

# edit kelas (guru)
def edit_kelas(username):
    lihat_kelas_guru(username)
    kelas_id = int(input("Masukkan ID kelas: "))

    for k in daftar_kelas:
        if k["kelas_id"] == kelas_id and k["guru"] == username:
            k["nama"] = input("Nama kelas baru: ")
            print("Kelas berhasil diubah!\n")
            return

    print("Kelas tidak ditemukan!\n")

# hapus kelas (guru)
def hapus_kelas(username):
    lihat_kelas_guru(username)
    kelas_id = int(input("Masukkan ID kelas yang ingin dihapus: "))

    for k in daftar_kelas:
        if k["kelas_id"] == kelas_id and k["guru"] == username:
            daftar_kelas.remove(k)
            print("Kelas berhasil dihapus!\n")
            return

    print("Kelas tidak ditemukan!\n")


# CRUD tugas (guru)
def buat_tugas(username):
    kelas_id = int(input("ID Kelas: "))

    if not any(k["kelas_id"] == kelas_id and k["guru"] == username for k in daftar_kelas):
        print("Kelas tidak ditemukan atau bukan milik Anda!\n")
        return

    judul = input("Judul Tugas: ")
    deskripsi = input("Deskripsi Tugas: ")

    daftar_tugas.append({
        "tugas_id": len(daftar_tugas) + 1,
        "kelas_id": kelas_id,
        "judul": judul,
        "deskripsi": deskripsi
    })

    print("Tugas berhasil dibuat!\n")

# lihat tugas (guru)
def lihat_tugas_guru(username):
    print("\n=== DAFTAR TUGAS ===")
    for t in daftar_tugas:
        for k in daftar_kelas:
            if k["kelas_id"] == t["kelas_id"] and k["guru"] == username:
                print(f"{t['tugas_id']}. {t['judul']} (Kelas {k['nama']})")
                print(f"   Deskripsi: {t['deskripsi']}")
    print("")

# edit tugas (guru)
def edit_tugas(username):
    lihat_tugas_guru(username)
    tugas_id = int(input("Masukkan ID tugas: "))

    for t in daftar_tugas:
        for k in daftar_kelas:
            if t["tugas_id"] == tugas_id and k["kelas_id"] == t["kelas_id"] and k["guru"] == username:
                t["judul"] = input("Judul baru: ")
                t["deskripsi"] = input("Deskripsi baru: ")
                print("Tugas berhasil diubah!\n")
                return

    print("Tugas tidak ditemukan!\n")

# hapus tugas (guru)
def hapus_tugas(username):
    lihat_tugas_guru(username)
    tugas_id = int(input("Masukkan ID tugas: "))

    for t in daftar_tugas:
        for k in daftar_kelas:
            if t["tugas_id"] == tugas_id and k["kelas_id"] == t["kelas_id"] and k["guru"] == username:
                daftar_tugas.remove(t)
                print("Tugas berhasil dihapus!\n")
                return

    print("Tugas tidak ditemukan!\n")


# lihat pengumpulan tugas dari siswa (guru)
def lihat_pengumpulan(username):
    print("\n=== PILIH KELAS ===")

    kelas_guru = [k for k in daftar_kelas if k["guru"] == username]

    for k in kelas_guru:
        print(f"{k['kelas_id']}. {k['nama']}")

    pilih = int(input("ID kelas: "))
    kelas = next((k for k in kelas_guru if k["kelas_id"] == pilih), None)

    if not kelas:
        print("Kelas tidak valid!\n")
        return

    tugas_di_kelas = [t for t in daftar_tugas if t["kelas_id"] == kelas["kelas_id"]]

    print("\n=== PILIH TUGAS ===")
    for t in tugas_di_kelas:
        print(f"{t['tugas_id']}. {t['judul']}")

    pilih_tugas = int(input("ID tugas: "))

    print("\n=== PENGUMPULAN TUGAS ===")
    jawaban = [p for p in pengumpulan_tugas if p["tugas_id"] == pilih_tugas]

    if not jawaban:
        print("Belum ada pengumpulan.\n")
        return

    for p in jawaban:
        print(f"- {p['siswa']} mengumpulkan jawaban : {p['file']}")
    print("")


# menu siswa
def menu_siswa(username):
    while True:
        print("=== MENU SISWA ===")
        print("1. Gabung Kelas")
        print("2. Lihat Tugas")
        print("3. Kumpulkan Tugas (Max 2x)")
        print("4. Hapus Pengumpulan")
        print("5. Logout")
        pilihan = input("Pilih menu: ")

        if pilihan == "1": gabung_kelas(username)
        elif pilihan == "2": lihat_tugas_siswa(username)
        elif pilihan == "3": kumpulkan_tugas(username)
        elif pilihan == "4": hapus_pengumpulan(username)
        elif pilihan == "5": break

# gabung kelas (siswa)
def gabung_kelas(username):
    kelas_id = int(input("Masukkan ID Kelas: "))

    for k in daftar_kelas:
        if k["kelas_id"] == kelas_id:
            if username not in k["siswa"]:
                k["siswa"].append(username)
                print("Berhasil bergabung!\n")
            else:
                print("Anda sudah di kelas ini!\n")
            return

    print("Kelas tidak ditemukan!\n")

# lihat tugas (siswa)
def lihat_tugas_siswa(username):
    print("\n=== TUGAS UNTUK ANDA ===")
    for t in daftar_tugas:
        for k in daftar_kelas:
            if k["kelas_id"] == t["kelas_id"] and username in k["siswa"]:
                print(f"{t['tugas_id']}. {t['judul']} (Kelas {k['nama']})")
                print(f"   Deskripsi: {t['deskripsi']}")
    print("")

# pengumpulan tugas (siswa)
def kumpulkan_tugas(username):
    tugas_id = int(input("ID Tugas: "))
    file = input("Jawaban: ")

    jumlah = len([p for p in pengumpulan_tugas if p["tugas_id"] == tugas_id and p["siswa"] == username])

    if jumlah >= 2:
        print("Anda sudah mengirim 2 kali!\n")
        return

    pengumpulan_tugas.append({"tugas_id": tugas_id, "siswa": username, "file": file})
    print(f"Tugas berhasil dikumpulkan! (ke-{jumlah+1})\n")

# hapus jawaban/tugas (siswa)
def hapus_pengumpulan(username):
    print("\n=== PENGUMPULAN ANDA ===")
    daftar = [p for p in pengumpulan_tugas if p["siswa"] == username]

    if not daftar:
        print("Tidak ada pengumpulan!")
        return

    for i, p in enumerate(daftar, start=1):
        print(f"{i}. Tugas {p['tugas_id']} - {p['file']}")

    pilih = int(input("Pilih nomor untuk dihapus: "))

    if 1 <= pilih <= len(daftar):
        pengumpulan_tugas.remove(daftar[pilih-1])
        print("Pengumpulan dihapus!\n")
    else:
        print("Pilihan tidak valid!\n")


# menu utama
while True:
    print("=== SISTEM PENGUMPULAN TUGAS KELAS ===")
    print("1. Daftar Akun")
    print("2. Login")
    print("3. Keluar")
    pilih = input("Pilih menu: ")

    if pilih == "1": daftar()
    elif pilih == "2":
        user = masuk()
        if user:
            if pengguna[user]["peran"] == "guru": menu_guru(user)
            else: menu_siswa(user)
    elif pilih == "3":
        print("Keluar...")
        break
