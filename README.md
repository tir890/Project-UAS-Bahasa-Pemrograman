# Project-UAS-Bahasa-Pemrograman

Nama: Tiara Hayatul Khoir

NIM: 312410474

Kelas: TI.24.A.5

# Alur Program Pemesanan Tiket Bioskop

Program ini dirancang menggunakan konsep modular dan OOP, dengan pembagian sebagai berikut:

## 1. Data Management
- **File:** `data/data.py`
- **Deskripsi:**
  Class `Data` menyimpan informasi tentang daftar film, termasuk judul, jumlah kursi tersedia, dan harga tiket. Data ini digunakan di seluruh program.

## 2. Tampilan (View)
- **File:** `view/view.py`
- **Deskripsi:**
  Class `View` bertanggung jawab untuk menampilkan data kepada pengguna dalam bentuk tabel, serta menampilkan pesan error atau konfirmasi.

## 3. Logika Pemrosesan (Process)
- **File:** `process/process.py`
- **Deskripsi:**
  Class `Process` menangani logika utama, seperti:
  - Menampilkan daftar film.
  - Memvalidasi input user (pilihan film, jumlah tiket, pembayaran).
  - Mengurangi jumlah kursi setelah tiket dipesan.
  - Menghitung total harga dan uang kembalian.

## 4. Program Utama
- **File:** `main.py`
- **Deskripsi:**
  Mengatur menu utama yang memungkinkan pengguna:
  - Menampilkan daftar film.
  - Memesan tiket.
  - Keluar dari program.

### Alur Program
1. Pengguna memilih menu utama:
   - **1:** Menampilkan daftar film dalam tabel.
   - **2:** Memesan tiket.
     - Input nomor film dan jumlah tiket.
     - Validasi jumlah kursi tersedia.
     - Input jumlah uang yang dibayar.
     - Hitung kembalian jika pembayaran mencukupi.
   - **0:** Keluar dari program.
2. Data film diperbarui setelah setiap pemesanan tiket.
3. Program berjalan hingga pengguna memilih keluar.

## Hasil Output Kode Program

![foto](https://github.com/tir890/Project-UAS-Bahasa-Pemrograman/blob/505745514c76a6ec279c41ca14770f5b2458e7fe/Screenshot%202025-01-08%20081352.png)

## Link Video YouTube
- [Video Penjelasan](https://youtu.be/xATcgaTClbE)
