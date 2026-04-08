'''Jawaban dan penjelasan untuk 10 soal variabel Python'''
# jalankan untuk melihat output : python basic/03_variabel/soal_dan_jawaban/01_jawaban.py

# 1. Mengubah nilai variabel
# Variabel bisa berubah tipe karena Python bersifat dynamic typing
x = 10
x = "sepuluh"  # mengubah menjadi string
print(x)

# 2. Multiple assignment
# Python memungkinkan menetapkan beberapa variabel dalam satu baris
a, b, c = 1, 2, 3
print(a, b, c)

# 3. Swap nilai tanpa variabel tambahan
# Python mendukung tuple unpacking untuk menukar nilai
m, n = 5, 9
m, n = n, m
print(m, n)

# 4. List dan penambahan elemen
# List bersifat mutable, sehingga bisa diubah setelah dibuat
data = [1, 2, 3]
data.append(4)
print(data)

# 5. Mengubah nilai variabel dan menampilkan sebelum-sesudah
nama = "Ali"
print(nama)  # sebelum
nama = "Budi"
print(nama)  # sesudah

# 6. Mutable vs Immutable
# int adalah immutable sehingga perubahan membuat objek baru
num = 10
print(id(num))
num += 1
print(id(num))  # id berubah

# list adalah mutable sehingga perubahan tidak membuat objek baru
items = [1, 2, 3]
print(id(items))
items.append(4)
print(id(items))  # id tetap

# 7. Type hint
# Type hint membantu dokumentasi, tidak memengaruhi eksekusi
age: int = 25
name: str = "Bob"
print(age, name)

# 8. Unpacking
x1, x2, x3 = [4, 5, 6]
print(x1, x2, x3)

# 9. Operasi +=
counter = 0
counter += 1
print(counter)

# 10. Dua variabel ke list sama
# Perubahan pada satu variabel berdampak pada keduanya karena referensi sama
list_a = [1, 2, 3]
list_b = list_a  # menunjuk list yang sama
list_a.append(4)
print(list_a, list_b)
