#python basic/07_kondisi_dan_looping/soal_dan_jawaban/01_jawaban.py

# File: jawaban.py
# Jawaban soal Conditional & Looping Python
# Penjelasan lengkap ditujukan untuk pemula belajar syntax, pola pemecahan masalah,
# dan contoh output yang akan muncul di terminal saat dijalankan.

# ==============================
# SOAL 1
# Cek apakah angka positif, negatif, atau nol
# ==============================
"""
Penjelasan:
- Menggunakan input() untuk meminta input user.
- Menggunakan int() untuk konversi string input menjadi integer.
- Struktur if-elif-else untuk mengecek kondisi.
- Output dicetak menggunakan print().
Contoh output:
> Masukkan angka: 5
x positif
"""
x = int(input("Masukkan angka untuk soal 1: "))
if x > 0:
    print("x positif")
elif x == 0:
    print("x nol")
else:
    print("x negatif")

# ==============================
# SOAL 2
# Cek angka genap atau ganjil
# ==============================
"""
Penjelasan:
- Operator modulus % digunakan untuk cek sisa pembagian.
- Jika x % 2 == 0, berarti angka genap; selain itu ganjil.
- Struktur if-else sederhana digunakan.
Contoh output:
> Masukkan angka: 4
x genap
"""
x = int(input("Masukkan angka untuk soal 2: "))
if x % 2 == 0:
    print("x genap")
else:
    print("x ganjil")

# ==============================
# SOAL 3
# Cetak angka 1 sampai 10 menggunakan while loop
# ==============================
"""
Penjelasan:
- while loop digunakan ketika jumlah iterasi diketahui atau kondisi harus dicek.
- Variable counter diincrement untuk menghindari infinite loop.
- print() untuk menampilkan setiap angka.
Contoh output:
while loop: 1
while loop: 2
...
while loop: 10
"""
count = 1
while count <= 10:
    print("while loop:", count)
    count += 1

# ==============================
# SOAL 4
# Cetak semua item dalam list menggunakan for loop
# ==============================
"""
Penjelasan:
- List = struktur data urut.
- for loop iterasi langsung setiap item dalam list.
- print() menampilkan item.
Contoh output:
for loop: apple
for loop: banana
for loop: cherry
"""
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print("for loop:", fruit)

# ==============================
# SOAL 5
# Cetak angka 1 sampai 10, stop ketika angka == 7 (break)
# ==============================
"""
Penjelasan:
- for loop dengan range.
- break menghentikan perulangan ketika kondisi terpenuhi.
Contoh output:
break loop: 1
...
break loop: 6
"""
for i in range(1, 11):
    if i == 7:
        break
    print("break loop:", i)

# ==============================
# SOAL 6
# Cetak angka 1 sampai 10, lewati angka 5 (continue)
# ==============================
"""
Penjelasan:
- continue melewati iterasi saat ini.
- i = 5 dilewati sehingga tidak dicetak.
Contoh output:
continue loop: 1
...
continue loop: 4
continue loop: 6
...
continue loop: 10
"""
for i in range(1, 11):
    if i == 5:
        continue
    print("continue loop:", i)

# ==============================
# SOAL 7
# Nested loop cetak pasangan (i,j)
# ==============================
"""
Penjelasan:
- Nested loop: for di dalam for.
- i dari 1 sampai 2, j dari 1 sampai 3.
- Membantu pemula memahami iterasi berlapis.
Contoh output:
i=1 j=1
i=1 j=2
i=1 j=3
i=2 j=1
i=2 j=2
i=2 j=3
"""
for i in range(1, 3):
    for j in range(1, 4):
        print(f"i={i} j={j}")

# ==============================
# SOAL 8
# Cetak bilangan genap dari list menggunakan list comprehension
# ==============================
"""
Penjelasan:
- List comprehension: cara ringkas membuat list baru dari list lama.
- Kondisi if n % 2 == 0 hanya menyertakan bilangan genap.
Contoh output:
even_numbers = [2, 4, 6, 8, 10]
"""
numbers = [1,2,3,4,5,6,7,8,9,10]
even_numbers = [n for n in numbers if n % 2 == 0]
print("even_numbers =", even_numbers)

# ==============================
# SOAL 9
# FIZZBUZZ sederhana
# ==============================
"""
Penjelasan:
- Input angka user.
- Gunakan if-elif-else untuk kondisi Fizz, Buzz, FizzBuzz, atau default.
- Operator modulus % digunakan untuk cek kelipatan.
Contoh output:
Masukkan angka: 15
FIZZBUZZ
"""
num = int(input("Masukkan angka untuk soal 9: "))
if num % 3 == 0 and num % 5 == 0:
    print("FIZZBUZZ")
elif num % 3 == 0:
    print("FIZZ")
elif num % 5 == 0:
    print("BUZZ")
else:
    print(num)

# ==============================
# SOAL 10
# Hitung jumlah semua angka 1 sampai 100
# ==============================
"""
Penjelasan:
- Gunakan for loop untuk iterasi dari 1 sampai 100.
- Variable total menampung hasil penjumlahan setiap iterasi.
- Print total di akhir.
Contoh output:
Jumlah semua angka 1 sampai 100 = 5050
"""
total = 0
for i in range(1, 101):
    total += i
print("Jumlah semua angka 1 sampai 100 =", total)

# ==============================
# Kesimpulan
# ==============================
"""
Dari 10 soal di atas, pemula belajar:
- Struktur if, elif, else untuk conditional
- Modulus % untuk genap/ganjil dan kelipatan
- while loop untuk iterasi dengan kondisi
- for loop untuk iterasi list, range, dan nested loop
- break dan continue untuk kontrol alur perulangan
- List comprehension untuk membuat list baru dengan kondisi
- Menggunakan input() untuk menerima data dari user
- Menjumlahkan angka menggunakan for loop

File ini membantu pemula memahami sintaks, pola pemecahan masalah, dan output yang dihasilkan.
"""