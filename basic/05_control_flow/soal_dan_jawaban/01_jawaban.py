"""
FILE: jawaban.py
Materi: Control Flow (if, elif, else)

File ini berisi:
- Jawaban 10 soal
- Penjelasan tiap soal
- Penjelasan syntax
- Contoh output

Tujuan:
Membantu pemula memahami cara berpikir (logic) dalam membuat percabangan
"""

# =========================================================
# SOAL 1
# =========================================================
"""
Soal:
Input usia → tampilkan "Dewasa" jika >=18, selain itu "Anak-anak"

Pola:
1. Ambil input
2. Konversi ke int
3. Gunakan if-else
"""

usia = int(input("Soal 1 - Masukkan usia: "))

# pengecekan kondisi
if usia >= 18:
    print("Dewasa")
else:
    print("Anak-anak")

# Output contoh:
# Input: 20 → Dewasa


# =========================================================
# SOAL 2
# =========================================================
"""
Pola sama:
- Gunakan perbandingan >=
"""

nilai = int(input("\nSoal 2 - Masukkan nilai: "))

if nilai >= 75:
    print("Lulus")
else:
    print("Tidak lulus")


# =========================================================
# SOAL 3
# =========================================================
"""
Gunakan if - elif - else untuk 3 kondisi
"""

angka = int(input("\nSoal 3 - Masukkan angka: "))

if angka > 0:
    print("Positif")
elif angka < 0:
    print("Negatif")
else:
    print("Nol")


# =========================================================
# SOAL 4
# =========================================================
"""
Pola:
Urutkan kondisi dari terbesar ke terkecil
"""

nilai = int(input("\nSoal 4 - Masukkan nilai (0-100): "))

if nilai >= 90:
    print("A")
elif nilai >= 75:
    print("B")
elif nilai >= 60:
    print("C")
else:
    print("D")


# =========================================================
# SOAL 5
# =========================================================
"""
Bandingkan 2 angka
"""

a = float(input("\nSoal 5 - Angka pertama: "))
b = float(input("Angka kedua: "))

if a > b:
    print("Angka pertama lebih besar")
elif b > a:
    print("Angka kedua lebih besar")
else:
    print("Kedua angka sama")


# =========================================================
# SOAL 6
# =========================================================
"""
Gunakan operator AND
"""

username = input("\nSoal 6 - Username: ")
password = input("Password: ")

if username == "admin" and password == "123":
    print("Login berhasil")
else:
    print("Login gagal")


# =========================================================
# SOAL 7
# =========================================================
"""
Gabungan kondisi:
umur < 18 DAN pelajar
"""

umur = int(input("\nSoal 7 - Umur: "))
pelajar = input("Pelajar (True/False): ")

# ubah string ke boolean
is_pelajar = pelajar == "True"

if umur < 18 and is_pelajar:
    print("Diskon pelajar")
else:
    print("Tidak dapat diskon")


# =========================================================
# SOAL 8
# =========================================================
"""
Gunakan OR
"""

hari = input("\nSoal 8 - Masukkan hari: ")

if hari == "Sabtu" or hari == "Minggu":
    print("Libur")
else:
    print("Hari kerja")


# =========================================================
# SOAL 9
# =========================================================
"""
Gunakan operator modulus (%)
% → sisa bagi
"""

angka = int(input("\nSoal 9 - Masukkan angka: "))

if angka % 2 == 0:
    print("Genap")
else:
    print("Ganjil")


# =========================================================
# SOAL 10
# =========================================================
"""
Mencari terbesar dari 3 angka

Pola:
Bandingkan satu per satu
"""

a = float(input("\nSoal 10 - Angka 1: "))
b = float(input("Angka 2: "))
c = float(input("Angka 3: "))

if a >= b and a >= c:
    print("Terbesar:", a)
elif b >= a and b >= c:
    print("Terbesar:", b)
else:
    print("Terbesar:", c)


# =========================================================
# KESIMPULAN
# =========================================================
"""
Dari 10 soal ini kita belajar:

1. if → untuk satu kondisi
2. elif → untuk banyak kondisi
3. else → kondisi terakhir/default
4. Operator penting:
   - >=, <=, ==, !=
   - and, or
   - % (modulus)
5. Pola berpikir:
   - Ambil input
   - Tentukan kondisi
   - Susun logika dari yang paling spesifik

Jika sudah paham file ini,
berarti kamu sudah menguasai dasar control flow Python.
"""