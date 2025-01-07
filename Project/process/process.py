class Process:
    def __init__(self, data, view):
        self.data = data
        self.view = view

    def book_ticket(self):
        try:
            self.view.display_films(self.data.films)
            choice = int(input("Pilih nomor film: "))
            
            # Validasi pilihan film
            if choice < 1 or choice > len(self.data.films):
                raise ValueError("Pilihan tidak valid!")
            
            selected_film = self.data.films[choice - 1]
            
            # Input jumlah tiket
            ticket_count = int(input("Masukkan jumlah tiket: "))
            if ticket_count < 1:
                raise ValueError("Jumlah tiket minimal 1!")
            
            # Cek ketersediaan kursi
            if selected_film["seats"] >= ticket_count:
                total_price = ticket_count * selected_film["price"]
                print(f"Total harga: Rp{total_price}")
                
                # Input jumlah uang yang dibayar
                while True:
                    paid_amount = int(input("Masukkan jumlah uang yang dibayar: Rp"))
                    if paid_amount >= total_price:
                        change = paid_amount - total_price
                        self.view.display_message(
                            f"Tiket berhasil dipesan! Uang kembalian: Rp{change}"
                        )
                        selected_film["seats"] -= ticket_count  # Kurangi kursi yang tersedia
                        break
                    else:
                        self.view.display_message("Uang yang Anda masukkan kurang, coba lagi.")
            else:
                self.view.display_message("Maaf, kursi tidak cukup.")
        except ValueError as e:
            self.view.display_message(f"Error: {e}")
