import calendar

# Konstanta
MIN_BULAN = 1
MAX_BULAN = 12
MIN_TANGGAL = 1

# Fungsi untuk menampilkan kalender bulanan
def tampilkan_kalender(tahun, bulan):
    print(calendar.month(tahun, bulan))

# Fungsi untuk menampilkan kalender tahunan
def tampilkan_kalender_tahunan(tahun):
    print(calendar.calendar(tahun))

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
    for kunci, keterangan in jadwal.items():
        if kunci.endswith(f"-{tahun}") and kunci[3:5] == f"{bulan:02d}":
            print(f"{kunci}: {', '.join(keterangan)}")
            found = True
    if not found:
        print("Tidak ada jadwal untuk bulan ini.")

# Fungsi untuk menampilkan jadwal pada tahun tertentu
def tampilkan_jadwal_tahun(jadwal, tahun):
    found = False
    for kunci, keterangan in jadwal.items():
        if kunci.endswith(f"-{tahun}"):
            print(f"{kunci}: {', '.join(keterangan)}")
            found = True
    if not found:
        print("Tidak ada jadwal pada tahun ini.")

# Fungsi untuk meminta input tahun dan bulan
def input_tahun_bulan():
    while True:
        try:
            tahun = int(input("Masukkan tahun\t\t: "))
            bulan = int(input("Masukkan bulan (1-12)\t: "))
            if MIN_BULAN <= bulan <= MAX_BULAN:
                return tahun, bulan
            else:
                print(f"Bulan tidak valid. Silakan masukkan bulan antara {MIN_BULAN} dan {MAX_BULAN}.")
        except ValueError:
            print("Input tidak valid. Silakan masukkan angka untuk tahun dan bulan.")

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
    jadwal = {}
    while True:
        print(25 * "=", "PILIHAN", 25 * "=")
        pilihan = int(input('''1. Kalender bulanan
2. Kalender tahunan
3. Tampilkan jadwal pada bulan tertentu
4. Tampilkan jadwal pada tahun tertentu
5. Keluar
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
            print(25 * "=", "TERIMA KASIH", 25 * "=")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")
if __name__ == "__main__":
    main()