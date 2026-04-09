# File ini berisi ringkasan tentang CONDITIONAL & LOOPING di Python
# python basic/02_control/01_conditional_looping.py (for run)
# Ringkasan berdasarkan dokumentasi resmi Python.

"""
Python menyediakan struktur kontrol untuk membuat keputusan (conditional) 
dan melakukan perulangan (looping). Struktur ini fleksibel karena Python 
menggunakan indentasi untuk menentukan blok kode, tidak seperti kurung {} di Java atau C.
"""

# jalankan file : python basic/07_kondisi_dan_looping/01_kondisi_dan_looping.py

# 1. CONDITIONAL STATEMENTS (IF, ELIF, ELSE)

# Variabel contoh
x = 10

# if statement
if x > 0:
    print("x positif")

# if-else statement
if x % 2 == 0:
    print("x genap")
else:
    print("x ganjil")

# if-elif-else statement
if x < 0:
    print("x negatif")
elif x == 0:
    print("x nol")
else:
    print("x positif")


# 2. NESTED IF
y = 15
if y > 0:
    if y % 3 == 0:
        print("y positif dan habis dibagi 3")


# 3. LOOPING

# a. while loop
count = 0
while count < 5:
    print("while count =", count)
    count += 1

# b. for loop (iterasi over sequence: list, tuple, string, range)
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print("for fruit =", fruit)

# c. for loop dengan range
for i in range(3):
    print("for range i =", i)

# d. nested loop
for i in range(2):
    for j in range(3):
        print(f"nested loop i={i} j={j}")


# 4. LOOP CONTROL STATEMENTS

# a. break (menghentikan loop)
for i in range(5):
    if i == 3:
        break
    print("break loop i =", i)

# b. continue (melewati iterasi saat ini)
for i in range(5):
    if i == 2:
        continue
    print("continue loop i =", i)

# c. else pada loop (dijalankan jika loop normal selesai, bukan break)
for i in range(3):
    print("loop else i =", i)
else:
    print("loop selesai tanpa break")


# 5. COMPREHENSION (optional, lebih ringkas)

# list comprehension dengan kondisi
numbers = [1, 2, 3, 4, 5]
even_numbers = [n for n in numbers if n % 2 == 0]
print("even_numbers =", even_numbers)


# Kesimpulan:
# - Conditional menggunakan if, elif, else
# - Looping menggunakan while dan for
# - break, continue, else dapat mengontrol jalannya loop
# - Nested loop dan comprehension mempermudah operasi kompleks