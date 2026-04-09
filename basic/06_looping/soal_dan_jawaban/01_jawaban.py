"""
File: jawaban.py
Deskripsi: Jawaban lengkap 10 soal looping Python untuk pemula.
Setiap soal disertai penjelasan kode, pola pemecahan, dan output yang akan muncul saat dijalankan.
Tujuan: Membantu pemula memahami cara kerja for loop, while loop, break, continue, nested loop, dan list comprehension.
"""
#jalankan file : python basic/06_looping/soal_dan_jawaban/01_jawaban.py
# =========================
# SOAL 1
# =========================
"""
Soal 1: Buat for loop yang mencetak angka 0 sampai 4.

Penjelasan:
- Fungsi range(n) menghasilkan urutan angka dari 0 sampai n-1.
- For loop digunakan untuk iterasi setiap nilai dalam range.
- print() mencetak nilai ke terminal.
- Pola: inisialisasi iterable -> iterasi -> aksi (cetak)
"""
print("Soal 1 Output:")
for i in range(5):
    print(i)
print("-"*30)

# =========================
# SOAL 2
# =========================
"""
Soal 2: Buat while loop yang mencetak angka 1 sampai 5.

Penjelasan:
- While loop dijalankan selama kondisi True.
- Harus inisialisasi variabel sebelum loop.
- Jangan lupa update variabel agar loop berhenti.
- Pola: inisialisasi -> kondisi while -> aksi -> update variabel
"""
print("Soal 2 Output:")
count = 1
while count <= 5:
    print(count)
    count += 1
print("-"*30)

# =========================
# SOAL 3
# =========================
"""
Soal 3: Buat list nama 3 buah favorit, cetak tiap nama.

Penjelasan:
- List: kumpulan item yang diurutkan.
- For loop iterasi langsung pada list.
- print() untuk menampilkan tiap item.
- Pola: buat list -> for item in list -> print(item)
"""
print("Soal 3 Output:")
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
print("-"*30)

# =========================
# SOAL 4
# =========================
"""
Soal 4: Cetak setiap huruf pada string "Python".

Penjelasan:
- String adalah iterable, sehingga bisa langsung di-for loop.
- print() mencetak huruf per iterasi.
- Pola: string -> for char in string -> print(char)
"""
print("Soal 4 Output:")
for char in "Python":
    print(char)
print("-"*30)

# =========================
# SOAL 5
# =========================
"""
Soal 5: Dictionary {"nama": "Alice", "umur": 25}, cetak key dan value.

Penjelasan:
- Dictionary menyimpan pasangan key-value.
- For loop default iterasi pada keys.
- Akses value dengan dictionary[key].
- Pola: for key in dict -> print key dan value
"""
print("Soal 5 Output:")
person = {"nama": "Alice", "umur": 25}
for key in person:
    print(f"{key}: {person[key]}")
print("-"*30)

# =========================
# SOAL 6
# =========================
"""
Soal 6: While loop hitung mundur dari 5 ke 1, cetak "Selesai!" setelahnya.

Penjelasan:
- Inisialisasi variabel dengan nilai awal 5.
- Kondisi while: nilai > 0
- Kurangi nilai setiap iterasi.
- Setelah loop, cetak teks selesai.
- Pola: init -> while kondisi -> aksi -> update -> aksi akhir
"""
print("Soal 6 Output:")
n = 5
while n > 0:
    print(n)
    n -= 1
print("Selesai!")
print("-"*30)

# =========================
# SOAL 7
# =========================
"""
Soal 7: For loop 0-5, cetak hanya angka ganjil dengan continue.

Penjelasan:
- continue: melewati iterasi saat kondisi terpenuhi.
- Gunakan modulus (%) untuk cek genap/ganjil.
- Pola: for i in range -> if genap: continue -> print(i)
"""
print("Soal 7 Output:")
for i in range(6):
    if i % 2 == 0:
        continue
    print(i)
print("-"*30)

# =========================
# SOAL 8
# =========================
"""
Soal 8: For loop 0-5, break saat angka 3 tercapai.

Penjelasan:
- break menghentikan loop saat kondisi terpenuhi.
- Pola: for i in range -> if kondisi: break -> print(i)
"""
print("Soal 8 Output:")
for i in range(6):
    if i == 3:
        break
    print(i)
print("-"*30)

# =========================
# SOAL 9
# =========================
"""
Soal 9: Nested loop for i in range(2), j in range(3).

Penjelasan:
- Nested loop: loop di dalam loop.
- Outer loop i dari 0-1, inner loop j dari 0-2.
- print f-string untuk format output.
- Pola: for i -> for j -> print(i,j)
"""
print("Soal 9 Output:")
for i in range(2):
    for j in range(3):
        print(f"i={i}, j={j}")
print("-"*30)

# =========================
# SOAL 10
# =========================
"""
Soal 10: List comprehension kuadrat angka 0-4.

Penjelasan:
- List comprehension: cara ringkas membuat list dari iterasi.
- Format: [expression for item in iterable]
- x**2 untuk kuadrat.
- Pola: buat list comprehension -> print
"""
print("Soal 10 Output:")
squares = [x**2 for x in range(5)]
print(squares)
print("-"*30)

# =========================
# KESIMPULAN
# =========================
"""
Kesimpulan:
1. For loop cocok untuk iterasi pada iterable (list, string, dict, range).
2. While loop cocok untuk kondisi yang bergantung pada variabel.
3. Break menghentikan loop, continue melewati iterasi tertentu.
4. Nested loop dapat digunakan untuk kombinasi multi-dimensi.
5. List comprehension memudahkan pembuatan list dengan ekspresi singkat.
6. Semua teknik ini memungkinkan pemula memahami pola pengulangan dan manipulasi data di Python.
7. Komentar dan penjelasan di setiap soal membantu membaca dan memahami kode.
"""