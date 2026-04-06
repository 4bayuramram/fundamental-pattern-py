

# jawaban.py
# file ini berisi jawaban dari latihan operator python dasar
# python basic/02_operator/soal_dan_jawaban/01_jawaban.py

'''
Tujuan file:
membantu memahami operator dasar python melalui latihan soal

aturan:
setiap soal ditulis bersama jawabannya
penjelasan dibuat sederhana agar mudah dipahami pemula
'''


# soal 1
# menjumlahkan 8 + 4

'''
operator + digunakan untuk menjumlahkan angka
'''

a = 8
b = 4

hasil = a + b

print("soal 1:", hasil)



# soal 2
# menghitung sisa bagi 15 % 4

'''
operator % digunakan untuk mencari sisa hasil pembagian
contoh:
15 dibagi 4 hasilnya 3 sisa 3
'''

hasil = 15 % 4

print("soal 2:", hasil)



# soal 3
# mengecek apakah 10 lebih besar dari 7

'''
operator > digunakan untuk membandingkan nilai
hasilnya berupa boolean
True berarti benar
False berarti salah
'''

hasil = 10 > 7

print("soal 3:", hasil)



# soal 4
# mengecek apakah 5 sama dengan 5

'''
operator == digunakan untuk mengecek kesamaan nilai
'''

hasil = 5 == 5

print("soal 4:", hasil)



# soal 5
# menggunakan operator logika AND

'''
operator AND hanya bernilai True jika kedua nilai True
'''

hasil = True and False

print("soal 5:", hasil)



# soal 6
# mengecek apakah angka 3 ada di dalam list

'''
operator in digunakan untuk mengecek apakah suatu nilai
ada di dalam list
'''

data = [1, 2, 3, 4, 5]

hasil = 3 in data

print("soal 6:", hasil)



# soal 7
# mengecek apakah variabel bernilai None

'''
operator is digunakan untuk mengecek identitas objek
biasanya digunakan untuk mengecek None
'''

x = None

hasil = x is None

print("soal 7:", hasil)



# soal 8
# menggunakan operator.add()

'''
module operator menyediakan versi fungsi dari operator +
'''

import operator

hasil = operator.add(6, 2)

print("soal 8:", hasil)



# soal 9
# menggunakan operator.mul()

'''
operator.mul sama dengan operator *
digunakan untuk perkalian
'''

hasil = operator.mul(7, 3)

print("soal 9:", hasil)



# soal 10
# menggunakan operator.iadd()

'''
operator.iadd sama dengan +=
digunakan untuk menambahkan nilai ke variabel
'''

nilai = 10

nilai = operator.iadd(nilai, 5)

print("soal 10:", nilai)



'''
kesimpulan:

operator python dibagi menjadi beberapa jenis

operator aritmatika
digunakan untuk perhitungan angka

operator perbandingan
digunakan untuk membandingkan nilai

operator logika
digunakan untuk logika program

operator membership
digunakan untuk mengecek isi list

operator identity
digunakan untuk mengecek None

module operator
versi fungsi dari operator python biasa
'''