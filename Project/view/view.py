class View:
    def display_films(self, films):
        print("==============================================")
        print("| No. | Judul Film        | Kursi | Harga     |")
        print("==============================================")
        for i, film in enumerate(films, start=1):
            print(f"| {i:<5} | {film['title']:<15} | {film['seats']:<5} | Rp{film['price']:<8} |")
        print("==============================================")

    def display_message(self, message):
        print(message)
