"""
File: jawaban.py
Deskripsi:
Menjawab 10 soal List Python untuk pemula.
Setiap jawaban disertai:
- Penjelasan soal
- Penjelasan syntax Python yang digunakan
- Pola berpikir untuk menyelesaikan soal
- Output yang akan muncul di terminal
Tujuan: Membantu pemula memahami list di Python secara praktis.
"""

# jalankan : python basic/09_list/soal_dan_jawaban/01_jawaban.py

# 1. Buat list bernama 'buah' yang berisi: "apel", "pisang", "jeruk"
# Penjelasan:
# - List dibuat dengan tanda kurung siku []
# - Elemen dipisah dengan koma
# - Variabel bisa menampung list
buah = ["apel", "pisang", "jeruk"]
print("Soal 1 - List awal:", buah)
# Output: ['apel', 'pisang', 'jeruk']


# 2. Tambahkan elemen "mangga" ke list 'buah'
# Penjelasan:
# - append() menambahkan elemen di akhir list
# - Tidak mengubah elemen lain
buah.append("mangga")
print("Soal 2 - Setelah append:", buah)
# Output: ['apel', 'pisang', 'jeruk', 'mangga']


# 3. Ubah elemen kedua dalam list 'buah' menjadi "blueberry"
# Penjelasan:
# - Akses elemen list dengan indeks (0-based)
# - Assignment langsung mengubah nilai
buah[1] = "blueberry"
print("Soal 3 - Setelah ubah elemen kedua:", buah)
# Output: ['apel', 'blueberry', 'jeruk', 'mangga']


# 4. Hapus elemen "jeruk" dari list 'buah'
# Penjelasan:
# - remove() menghapus elemen berdasarkan nilainya
# - Jika ada beberapa sama, hanya yang pertama dihapus
buah.remove("jeruk")
print("Soal 4 - Setelah remove 'jeruk':", buah)
# Output: ['apel', 'blueberry', 'mangga']


# 5. Ambil elemen terakhir dari list 'buah' dan simpan di variabel 'terakhir'
# Penjelasan:
# - Indeks negatif (-1) mengambil elemen terakhir
# - Variabel 'terakhir' menampung nilai itu
terakhir = buah[-1]
print("Soal 5 - Elemen terakhir:", terakhir)
# Output: mangga


# 6. Buat list angka dari 1 sampai 10, cetak elemen indeks 3 sampai 7
# Penjelasan:
# - range(1,11) menghasilkan angka 1-10
# - list() mengubah range menjadi list
# - slicing list[start:end] mengambil elemen indeks start sampai end-1
angka = list(range(1, 11))
print("Soal 6 - Elemen indeks 3 sampai 7:", angka[3:8])
# Output: [4, 5, 6, 7, 8]


# 7. Buat list 'kuadrat_genap' dari kuadrat angka genap 0-10 menggunakan list comprehension
# Penjelasan:
# - List comprehension: [expression for variable in iterable if condition]
# - x**2 menghitung kuadrat x
# - if x % 2 == 0 memfilter angka genap
kuadrat_genap = [x**2 for x in range(11) if x % 2 == 0]
print("Soal 7 - Kuadrat angka genap 0-10:", kuadrat_genap)
# Output: [0, 4, 16, 36, 64, 100]


# 8. Buat nested list 2x2 angka 1-4, cetak elemen baris kedua kolom pertama
# Penjelasan:
# - Nested list: list di dalam list
# - Akses elemen: list[row][column]
matrix = [[1,2],[3,4]]
print("Soal 8 - Nested list matrix:", matrix)
print("Elemen baris 2 kolom 1:", matrix[1][0])
# Output matrix: [[1,2],[3,4]]
# Output elemen: 3


# 9. Balik urutan list 'angka' menggunakan metode list
# Penjelasan:
# - reverse() membalik list in-place
# - Tidak perlu assignment baru
angka.reverse()
print("Soal 9 - List 'angka' setelah reverse:", angka)
# Output: [10,9,8,7,6,5,4,3,2,1]


# 10. Cek apakah angka 5 ada di list 'angka'
# Penjelasan:
# - Operator 'in' mengembalikan True jika elemen ada di list, False jika tidak
cek = 5 in angka
print("Soal 10 - Apakah 5 ada di list 'angka'?", cek)
# Output: True


"""
Kesimpulan:
- Semua soal menggunakan konsep dasar list Python: membuat, mengakses, mengubah, menambah, menghapus.
- Menggunakan metode list bawaan seperti append, remove, reverse.
- Memahami slicing dan indeks negatif membantu manipulasi elemen.
- List comprehension memudahkan pembuatan list baru dengan kondisi.
- Nested list bisa diakses dengan dua indeks [row][column].
- Operator 'in' memudahkan pengecekan keberadaan elemen.
- Dengan membaca komentar, pemula dapat memahami setiap langkah dan logika penggunaan list.
"""