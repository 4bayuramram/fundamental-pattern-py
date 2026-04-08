"""
04_INPUT_OUTPUT.py
===================

Materi: Input & Output di Python
Topik: Fungsi input() dan print()

File ini dirancang agar:
- Pemula mudah memahami (penjelasan dengan komentar)
- Berisi contoh penggunaan input() dan print()
- Bisa dijalankan tanpa error
- Mengacu pada dokumentasi resmi Python:
  https://docs.python.org/3/library/functions.html#input
  https://docs.python.org/3/library/functions.html#print

-----------------------------------------------
Apa itu Input dan Output?
-----------------------------------------------
• INPUT  : Data yang dimasukkan oleh user ke program.
           Di Python dilakukan dengan fungsi input().
• OUTPUT : Informasi yang ditampilkan oleh program.
           Di Python dilakukan dengan fungsi print().

Di JavaScript, input kadang menggunakan popup (prompt()).
Python tidak memakai popup, tetapi memakai input() dari terminal.
"""

#jalankan file : python basic/04_input_dan_output/01_input_dan_output.py

# ---------------------------------------------------------
# 1. Fungsi input()
# ---------------------------------------------------------
"""
input() digunakan untuk mengambil data dari user melalui keyboard.

SINTAX DASAR:
-------------
nama_variabel = input("Teks sebagai petunjuk: ")

CATATAN:
• input() SELALU menghasilkan string (tipe data str)
• Jika membutuhkan angka, harus dikonversi (int, float)
"""


# Contoh 1 — Input dasar
nama = input("Masukkan nama Anda: ")  # user menulis teks, lalu ENTER

# Contoh 2 — Input angka (harus konversi)
# Jika tidak dikonversi, bilangan dianggap sebagai string
usia = int(input("Masukkan usia Anda: "))  # ubah string → int

# Contoh 3 — Input float (angka desimal)
tinggi = float(input("Masukkan tinggi badan Anda (dalam cm): "))

# ---------------------------------------------------------
# 2. Fungsi print()
# ---------------------------------------------------------
"""
print() digunakan untuk menampilkan teks atau hasil ke layar.

SINTAX DASAR:
-------------
print(objek1, objek2, ..., sep=' ', end='\n')

Penjelasan parameter penting:
• sep : pemisah antar item (default spasi)
• end : karakter di akhir output (default baris baru '\n')
"""

# Contoh 4 — Output sederhana
print("Halo,", nama, "!")

# Contoh 5 — Menggabungkan teks dan variabel
print("Usia Anda adalah", usia, "tahun.")

# Contoh 6 — Menggunakan f-string (cara modern & rapi)
print(f"Tinggi badan Anda adalah {tinggi} cm.")

# ---------------------------------------------------------
# 3. Opsi print() yang sering dipakai
# ---------------------------------------------------------

# Contoh 7 — Mengubah pemisah (sep)
print("Python", "sangat", "menyenangkan", sep="-")

# Contoh 8 — Mengubah akhir baris (end)
print("Ini baris pertama", end=" | ")
print("Ini baris kedua (tidak pindah baris dari sebelumnya)")

# Contoh 9 — Menampilkan hasil perhitungan
angka1 = 10
angka2 = 5
print(f"Hasil penjumlahan {angka1} + {angka2} = {angka1 + angka2}")

# ---------------------------------------------------------
# 4. Mini latihan interaktif untuk pemula
# ---------------------------------------------------------
"""
Latihan kecil: mintalah user memasukkan dua angka,
lalu tampilkan hasil penjumlahan, pengurangan, perkalian.
"""

print("\n=== LATIHAN MINI ===")
a = float(input("Masukkan angka pertama: "))
b = float(input("Masukkan angka kedua : "))

print(f"Penjumlahan : {a + b}")
print(f"Pengurangan : {a - b}")
print(f"Perkalian   : {a * b}")
print(f"Pembagian   : {a / b if b != 0 else 'Tidak dapat membagi dengan 0'}")

# ---------------------------------------------------------
# 5. Kesimpulan
# ---------------------------------------------------------
"""
• input() -> mengambil data dari user (hasilnya string)
• print() -> menampilkan data ke layar
• Untuk angka, gunakan konversi tipe: int(), float()
• print() dapat memakai f-string untuk output yang rapi

File ini bisa dijalankan langsung dan seluruh contoh dapat dicoba sendiri.
Selamat belajar Python!
"""

