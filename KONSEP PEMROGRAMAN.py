import calendar
import os

# Konstanta
MIN_BULAN = 1
MAX_BULAN = 12
MIN_TANGGAL = 1
FILENAME = 'schedule.txt'

# Fungsi untuk menampilkan kalender bulanan
def tampilkan_kalender(tahun, bulan):
    print(calendar.month(tahun, bulan))

# Fungsi untuk menampilkan kalender tahunan
def tampilkan_kalender_tahunan(tahun):
    print(calendar.calendar(tahun))

# Fungsi untuk menulis jadwal ke dalam file
def write_to_file(jadwal):
    with open(FILENAME, 'w') as file:
        for date, descriptions in jadwal.items():
            for description in descriptions:
                file.write(f"{date}: {description}\n")

# Fungsi untuk membaca jadwal dari file
import calendar
import os

# Konstanta
MIN_BULAN = 1
MAX_BULAN = 12
MIN_TANGGAL = 1
FILENAME = 'schedule.txt'

# Fungsi untuk menampilkan kalender bulanan
def tampilkan_kalender(tahun, bulan):
    print(calendar.month(tahun, bulan))

# Fungsi untuk menampilkan kalender tahunan
def tampilkan_kalender_tahunan(tahun):
    print(calendar.calendar(tahun))

# Fungsi untuk menulis jadwal ke dalam file
def write_to_file(jadwal):
    with open(FILENAME, 'w') as file:
        for date, descriptions in jadwal.items():
            for description in descriptions:
                file.write(f"{date}: {description}\n")

# Fungsi untuk membaca jadwal dari file
# Fungsi untuk membaca jadwal dari file
def read_from_file():
    jadwal = {}
    if os.path.exists(FILENAME):
        with open(FILENAME, 'r') as file:
            for line in file:
                try:
                    date, description = line.strip().split(': ', 1)
                    if date in jadwal:
                        jadwal[date].append(description)
                    else:
                        jadwal[date] = [description]
                except ValueError:
                    print(f"Format baris tidak valid: {line.strip()})
    return jadwal

# Fungsi untuk menampilkan seluruh jadwal
def tampilkan_seluruh_jadwal():
    jadwal = read_from_file()  # Membaca jadwal dari file
    if not jadwal:
        print("Tidak ada jadwal yang tersedia.")
    else:
        print("Seluruh Jadwal:")
        for date, descriptions in jadwal.items():
            print(f"{date}: {', '.join(descriptions)}")

# Fungsi untuk menghapus jadwal dari file
def delete_schedule():
    if os.path.exists(FILENAME):
        os.remove(FILENAME)
        print(15*"=","Catatan jadwal telah dihapus", 15*"=")
    else:
        print(13*"=", "Catatan jadwal tidak ditemukan", 14*"=")

# Fungsi untuk menambahkan jadwal
def tambah_jadwal(jadwal, tahun, bulan, tanggal, keterangan):
    kunci = f"{tanggal:02d}-{bulan:02d}-{tahun}"  # Format kunci
    if kunci in jadwal:
        jadwal[kunci].append(keterangan)
    else:
        jadwal[kunci] = [keterangan]

# Fungsi untuk menampilkan jadwal pada bulan tertentu
def tampilkan_jadwal_bulan(jadwal, tahun, bulan):
    found = False
    for tampilkanJadwalBln, keterangan in jadwal.items():
        if tampilkanJadwalBln.endswith(f"-{tahun}") and tampilkanJadwalBln[3:5] == f"{bulan:02d}":
            print(f"{tampilkanJadwalBln}: {', '.join(keterangan)}")
            print("\n")
            found = True
    if not found:
        print(13*"=", "Tidak ada jadwal pada bulan ini", 13*"=", "\n")

# Fungsi untuk menampilkan jadwal pada tahun tertentu
def tampilkan_jadwal_tahun(jadwal, tahun):
    found = False
    for kunci, keterangan in jadwal.items():
        if kunci.endswith(f"-{tahun}"):
            print(f"{kunci}: {', '.join(keterangan)}")
            found = True
    if not found:
        print(13*"=", "Tidak ada jadwal pada tahun ini", 13*"=", "\n")


# Fungsi untuk meminta input tahun dan bulan
def input_tahun_bulan():
    while True:
        try:
            tahun = int(input("Masukkan tahun\t\t: "))
            while True:
                try:
                    bulan = int(input("Masukkan bulan (1-12)\t: "))
                    if MIN_BULAN <= bulan <= MAX_BULAN:
                        return tahun, bulan
                    else:
                        print(f"Bulan tidak valid. Silakan masukkan bulan antara {MIN_BULAN} dan {MAX_BULAN}.")
                except ValueError:
                    print("Input tidak valid. Silahkan masukkan angka untuk bulan.")
        except ValueError:
            print("Input tidak valid. Silakan masukkan angka untuk tahun.")

# Fungsi untuk menambahkan jadwal
def add_schedule(jadwal, tahun, bulan=None):
    while True:
        tambahan_jadwal = input("Apakah ada jadwal? (y/n)\t: ")
        if tambahan_jadwal.lower() == "y":
            while True:
                try:
                    # Jika bulan belum ditentukan, minta bulan terlebih dahulu
                    if bulan is None:
                        bulan = int(input("Masukkan bulan (1-12)\t\t: "))
                        if not (MIN_BULAN <= bulan <= MAX_BULAN):
                            print(f"Bulan tidak valid. Silakan masukkan bulan antara {MIN_BULAN} dan {MAX_BULAN}.")
                            continue  # Kembali ke awal loop untuk meminta bulan lagi

                    # Minta tanggal setelah bulan ditentukan
                    tanggal = int(input("Masukkan tanggal\t\t: "))
                    if MIN_TANGGAL <= tanggal <= calendar.monthrange(tahun, bulan)[1]:
                        keterangan = input("Masukkan keterangan jadwal\t: ")
                        tambah_jadwal(jadwal, tahun, bulan, tanggal, keterangan)
                        write_to_file(jadwal)  # Menyimpan ke file setelah menambahkan jadwal
                        print(f"Jadwal ditambahkan pada\t\t: {tanggal}-{bulan}-{tahun}\n")
                        break  # Keluar dari loop setelah menambahkan jadwal
                    else:
                        print(f"Tanggal tidak valid. Silakan masukkan tanggal antara {MIN_TANGGAL} dan {calendar.monthrange(tahun, bulan)[1]}.")
                except ValueError:
                    print("Input tidak valid. Silakan masukkan angka untuk tanggal.")
                
            break
        elif tambahan_jadwal.lower() == "n":
            print("Terima kasih telah melihat kalender\n")
            break
        else:
            print("Input tidak valid. Silakan masukkan 'y' atau 'n'.")

# Fungsi utama
def main():
    jadwal = read_from_file()
    while True:
        try:
            print(25 * "=", "PILIHAN", 25 * "=")
            pilihan = int(input('''1. Kalender bulanan
2. Kalender tahunan
3. Tampilkan jadwal pada bulan tertentu
4. Tampilkan jadwal pada tahun 
5. Tampilkan seluruh jadwal baik pada tahun dan bulan manapun
6. Hapus catatan jadwal
7. Keluar
Masukkan pilihan\t: '''))
            
            if pilihan == 1:
                tahun, bulan = input_tahun_bulan()
                print(25 * "=", "KALENDER", 25 * "=")
                tampilkan_kalender(tahun, bulan)
                print(25 * "=", "SCHEDULE", 25 * "=")
                add_schedule(jadwal, tahun, bulan)
            elif pilihan == 2:
                while True:
                    try:
                        tahun = int(input("Masukkan tahun\t\t: "))
                        print(30 * "=", "KALENDER", 30 * "=")
                        tampilkan_kalender_tahunan(tahun)
                        print(30 * "=", "SCHEDULE", 30 * "=")
                        add_schedule(jadwal, tahun)  # Menambahkan jadwal untuk tahun
                        break
                    except ValueError:
                        print("Input tidak valid. Silahkan coba lagi.")
            elif pilihan == 3:
                tahun, bulan = input_tahun_bulan()
                tampilkan_kalender(tahun, bulan)
                tampilkan_jadwal_bulan(jadwal, tahun, bulan)
            elif pilihan == 4:
                tahun = int(input("Masukkan tahun\t\t: "))
                tampilkan_kalender_tahunan(tahun)
                tampilkan_jadwal_tahun(jadwal, tahun)
            elif pilihan == 5:
                tampilkan_seluruh_jadwal()
            elif pilihan == 6:
                delete_schedule()  # Menghapus seluruh jadwal
                jadwal.clear()  # Mengosongkan dictionary jadwal
            elif pilihan == 7:
                print(23 * "=", "TERIMA KASIH", 22 * "=")
                break
            else:
                print("Pilihan tidak valid. Silakan coba lagi.")
        except ValueError:
            print("Input tidak valid. Silahkan masukkan angka.")
        except exception as e:
            print(f"Terjadi kesalahan {e}")
if __name__ == "__main__":
    main()

# Fungsi untuk menampilkan seluruh jadwal
def tampilkan_seluruh_jadwal():
    jadwal = read_from_file()  # Membaca jadwal dari file
    if not jadwal:
        print("Tidak ada jadwal yang tersedia.")
    else:
        print("Seluruh Jadwal:")
        for date, descriptions in jadwal.items():
            print(f"{date}: {', '.join(descriptions)}")

# Fungsi untuk menghapus jadwal dari file
def delete_schedule():
    if os.path.exists(FILENAME):
        os.remove(FILENAME)
        print(15*"=","Catatan jadwal telah dihapus", 15*"=")
    else:
        print(13*"=", "Catatan jadwal tidak ditemukan", 14*"=")

# Fungsi untuk menambahkan jadwal
def tambah_jadwal(jadwal, tahun, bulan, tanggal, keterangan):
    kunci = f"{tanggal:02d}-{bulan:02d}-{tahun}"  # Format kunci
    if kunci in jadwal:
        jadwal[kunci].append(keterangan)
    else:
        jadwal[kunci] = [keterangan]

# Fungsi untuk menampilkan jadwal pada bulan tertentu
def tampilkan_jadwal_bulan(jadwal, tahun, bulan):
    found = False
    for tampilkanJadwalBln, keterangan in jadwal.items():
        if tampilkanJadwalBln.endswith(f"-{tahun}") and tampilkanJadwalBln[3:5] == f"{bulan:02d}":
            print(f"{tampilkanJadwalBln}: {', '.join(keterangan)}")
            print("\n")
            found = True
    if not found:
        print(13*"=", "Tidak ada jadwal pada bulan ini", 13*"=", "\n")

# Fungsi untuk menampilkan jadwal pada tahun tertentu
def tampilkan_jadwal_tahun(jadwal, tahun):
    found = False
    for kunci, keterangan in jadwal.items():
        if kunci.endswith(f"-{tahun}"):
            print(f"{kunci}: {', '.join(keterangan)}")
            found = True
    if not found:
        print(13*"=", "Tidak ada jadwal pada tahun ini", 13*"=", "\n")


# Fungsi untuk meminta input tahun dan bulan
def input_tahun_bulan():
    while True:
        try:
            tahun = int(input("Masukkan tahun\t\t: "))
            while True:
                try:
                    bulan = int(input("Masukkan bulan (1-12)\t: "))
                    if MIN_BULAN <= bulan <= MAX_BULAN:
                        return tahun, bulan
                    else:
                        print(f"Bulan tidak valid. Silakan masukkan bulan antara {MIN_BULAN} dan {MAX_BULAN}.")
                except ValueError:
                    print("Input tidak valid. Silahkan masukkan angka untuk bulan.")
        except ValueError:
            print("Input tidak valid. Silakan masukkan angka untuk tahun.")

# Fungsi untuk menambahkan jadwal
def add_schedule(jadwal, tahun, bulan=None):
    while True:
        tambahan_jadwal = input("Apakah ada jadwal? (y/n)\t: ")
        if tambahan_jadwal.lower() == "y":
            while True:
                try:
                    # Jika bulan belum ditentukan, minta bulan terlebih dahulu
                    if bulan is None:
                        bulan = int(input("Masukkan bulan (1-12)\t\t: "))
                        if not (MIN_BULAN <= bulan <= MAX_BULAN):
                            print(f"Bulan tidak valid. Silakan masukkan bulan antara {MIN_BULAN} dan {MAX_BULAN}.")
                            continue  # Kembali ke awal loop untuk meminta bulan lagi

                    # Minta tanggal setelah bulan ditentukan
                    tanggal = int(input("Masukkan tanggal\t\t: "))
                    if MIN_TANGGAL <= tanggal <= calendar.monthrange(tahun, bulan)[1]:
                        keterangan = input("Masukkan keterangan jadwal\t: ")
                        tambah_jadwal(jadwal, tahun, bulan, tanggal, keterangan)
                        write_to_file(jadwal)  # Menyimpan ke file setelah menambahkan jadwal
                        print(f"Jadwal ditambahkan pada\t\t: {tanggal}-{bulan}-{tahun}\n")
                        break  # Keluar dari loop setelah menambahkan jadwal
                    else:
                        print(f"Tanggal tidak valid. Silakan masukkan tanggal antara {MIN_TANGGAL} dan {calendar.monthrange(tahun, bulan)[1]}.")
                except ValueError:
                    print("Input tidak valid. Silakan masukkan angka untuk tanggal.")
                
            break
        elif tambahan_jadwal.lower() == "n":
            print("Terima kasih telah melihat kalender\n")
            break
        else:
            print("Input tidak valid. Silakan masukkan 'y' atau 'n'.")

# Fungsi utama
def main():
    jadwal = read_from_file()
    while True:
        try:
            print(25 * "=", "PILIHAN", 25 * "=")
            pilihan = int(input('''1. Kalender bulanan
2. Kalender tahunan
3. Tampilkan jadwal pada bulan tertentu
4. Tampilkan jadwal pada tahun 
5. Tampilkan seluruh jadwal baik pada tahun dan bulan manapun
6. Hapus catatan jadwal
7. Keluar
Masukkan pilihan\t: '''))
            
            if pilihan == 1:
                tahun, bulan = input_tahun_bulan()
                print(25 * "=", "KALENDER", 25 * "=")
                tampilkan_kalender(tahun, bulan)
                print(25 * "=", "SCHEDULE", 25 * "=")
                add_schedule(jadwal, tahun, bulan)
            elif pilihan == 2:
                while True:
                    try:
                        tahun = int(input("Masukkan tahun\t\t: "))
                        print(30 * "=", "KALENDER", 30 * "=")
                        tampilkan_kalender_tahunan(tahun)
                        print(30 * "=", "SCHEDULE", 30 * "=")
                        add_schedule(jadwal, tahun)  # Menambahkan jadwal untuk tahun
                        break
                    except ValueError:
                        print("Input tidak valid. Silahkan coba lagi.")
            elif pilihan == 3:
                tahun, bulan = input_tahun_bulan()
                tampilkan_kalender(tahun, bulan)
                tampilkan_jadwal_bulan(jadwal, tahun, bulan)
            elif pilihan == 4:
                tahun = int(input("Masukkan tahun\t\t: "))
                tampilkan_kalender_tahunan(tahun)
                tampilkan_jadwal_tahun(jadwal, tahun)
            elif pilihan == 5:
                tampilkan_seluruh_jadwal()
            elif pilihan == 6:
                delete_schedule()  # Menghapus seluruh jadwal
                jadwal.clear()  # Mengosongkan dictionary jadwal
            elif pilihan == 7:
                print(23 * "=", "TERIMA KASIH", 22 * "=")
                break
            else:
                print("Pilihan tidak valid. Silakan coba lagi.")
        except ValueError:
            print("Input tidak valid. Silahkan masukkan angka.")
        except exception as e:
            print(f"Terjadi kesalahan {e}")
if __name__ == "__main__":
    main()
