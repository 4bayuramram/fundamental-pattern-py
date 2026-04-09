"""
File ini berisi ringkasan tentang LIST di Python
python basic/02_list/01_list.py (for run)
Ringkasan berdasarkan dokumentasi resmi Python.
'''
List adalah tipe data bawaan Python yang **mutable**, 
dapat menyimpan urutan elemen dari berbagai tipe. 
Berbeda dengan tuple (immutable), list bisa diubah setelah dibuat. 
List mirip array di bahasa lain, namun lebih fleksibel.
'''
"""
# jalankan file : python basic/09_list/01_list.py

# 1. PENGENALAN LIST
"""
List menyimpan elemen dalam urutan tertentu.
Elemen bisa dari tipe berbeda.
"""

fruits = ["apple", "banana", "cherry"]
numbers = [1, 2, 3, 4]
mixed = [1, "two", 3.0, True]

print("fruits =", fruits)
print("numbers =", numbers)
print("mixed =", mixed)


# 2. MENGAKSES ELEMEN
"""
Gunakan indeks, dimulai dari 0.
Indeks negatif untuk dari belakang.
"""

print("fruits[0] =", fruits[0])
print("fruits[-1] =", fruits[-1])


# 3. MENGUBAH ELEMEN
fruits[1] = "blueberry"
print("fruits setelah ubah =", fruits)


# 4. MENAMBAH DAN MENGHAPUS ELEMEN
"""
append() - tambah di akhir
insert() - tambah di indeks tertentu
extend() - tambah list lain
remove() - hapus berdasarkan nilai
pop() - hapus berdasarkan indeks, kembalikan nilai
clear() - hapus semua elemen
"""

fruits.append("orange")
print("append orange ->", fruits)

fruits.insert(1, "kiwi")
print("insert kiwi index 1 ->", fruits)

fruits.extend(["mango", "grape"])
print("extend dengan list lain ->", fruits)

fruits.remove("apple")
print("remove apple ->", fruits)

last = fruits.pop()
print("pop terakhir ->", last, fruits)

fruits.clear()
print("clear list ->", fruits)


# 5. SLICING LIST
"""
list[start:end:step]
"""

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print("numbers[2:5] ->", numbers[2:5])
print("numbers[:4] ->", numbers[:4])
print("numbers[5:] ->", numbers[5:])
print("numbers[::2] ->", numbers[::2])
print("numbers[::-1] ->", numbers[::-1])  # reverse


# 6. PENGULANGAN DAN MEMBERSHIP
for n in numbers:
    print(n, end=" ")
print()

print("5 in numbers?", 5 in numbers)
print("10 in numbers?", 10 in numbers)


# 7. METODE LIST LAINNYA
numbers.sort()
print("sort ->", numbers)

numbers.reverse()
print("reverse ->", numbers)

print("count 2 ->", numbers.count(2))
print("index 4 ->", numbers.index(4))

# copy list
numbers_copy = numbers.copy()
print("copy ->", numbers_copy)


# 8. LIST COMPREHENSION
"""
Membuat list baru dari list lama secara ringkas.
"""

squares = [x**2 for x in range(10)]
print("squares =", squares)

even_squares = [x**2 for x in range(10) if x % 2 == 0]
print("even_squares =", even_squares)


# 9. NESTED LIST
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("matrix =", matrix)
print("matrix[1][2] =", matrix[1][2])  # baris 2, kolom 3


# Kesimpulan:
# - List adalah urutan mutable
# - Bisa diakses via indeks, diubah, ditambah, dihapus
# - Mendukung slicing, pengulangan, membership
# - Banyak metode bawaan untuk manipulasi
# - List comprehension untuk pembuatan list baru
# - Bisa berisi list lain (nested list)