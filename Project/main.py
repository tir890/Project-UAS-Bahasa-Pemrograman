from data.data import Data
from view.view import View
from process.process import Process

# Membuat objek untuk setiap class
data_manager = Data()
view = View()
process = Process(data_manager, view)

def menu():
    while True:
        print("\n=== Menu Pemesanan Tiket ===")
        print("1. Tampilkan Daftar Film")
        print("2. Pesan Tiket")
        print("0. Keluar")
        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            view.display_films(data_manager.films)  # Tampilkan daftar film
        elif pilihan == "2":
            process.book_ticket()  # Proses pemesanan tiket
        elif pilihan == "0":
            print("Terima kasih telah menggunakan sistem kami!")
            break
        else:
            print("Pilihan tidak valid, coba lagi.")

if __name__ == "__main__":
    menu()
