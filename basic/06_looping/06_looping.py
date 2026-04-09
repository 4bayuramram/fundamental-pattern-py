"""
File ini berisi ringkasan tentang LOOPING di Python
python basic/02_looping/01_looping.py (for run)
Ringkasan berdasarkan dokumentasi resmi Python.
'''
Looping digunakan untuk mengeksekusi blok kode berulang kali.
Python memiliki dua jenis loop utama: for dan while. 
Berbeda dengan Java yang menggunakan for, while, dan do-while, 
Python tidak memiliki do-while. For Python iterates langsung 
pada item iterable (list, tuple, string, dict, set) bukan menggunakan 
indeks secara default. While loop mirip dengan bahasa lain: dieksekusi 
selama kondisi True. Break, continue, dan else juga dapat digunakan 
untuk mengatur alur loop.
'''
"""

# jalankan file: python basic/06_looping/06_looping.py

# 1. PENGENALAN LOOPING
"""
Looping digunakan untuk mengeksekusi blok kode berulang kali.
- for loop: untuk iterasi pada iterable
- while loop: selama kondisi True
"""

# contoh for loop sederhana
for i in range(5):  # range(5) menghasilkan 0,1,2,3,4
    print("for loop i =", i)

# contoh while loop sederhana
count = 0
while count < 5:
    print("while loop count =", count)
    count += 1


# 2. FOR LOOP PADA ITERABLE
"""
For loop dapat langsung iterasi pada list, tuple, string, dict, set.
"""

# list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print("fruit:", fruit)

# string
for char in "Python":
    print("char:", char)

# dictionary
person = {"name": "Alice", "age": 25}
for key in person:
    print("key:", key, "value:", person[key])

# set
colors = {"red", "green", "blue"}
for color in colors:
    print("color:", color)


# 3. WHILE LOOP
"""
While loop mengeksekusi selama kondisi True.
- Bisa digunakan untuk loop yang tidak pasti jumlahnya
- Perlu berhati-hati agar tidak infinite loop
"""

n = 0
while n < 3:
    print("n =", n)
    n += 1


# 4. BREAK, CONTINUE, DAN ELSE PADA LOOP
"""
- break: keluar dari loop
- continue: lompat ke iterasi berikutnya
- else: dieksekusi jika loop selesai normal (tanpa break)
"""

# break
for i in range(5):
    if i == 3:
        break
    print("break loop i =", i)

# continue
for i in range(5):
    if i % 2 == 0:
        continue
    print("continue loop i =", i)

# else pada loop
for i in range(3):
    print("loop i =", i)
else:
    print("loop selesai tanpa break")


# 5. NESTED LOOP
"""
Loop di dalam loop (nested loop) untuk struktur data multi-dimensi
"""

for i in range(3):
    for j in range(2):
        print(f"i={i}, j={j}")


# 6. LIST COMPREHENSION DENGAN LOOP
"""
Kombinasi for loop dan ekspresi untuk membuat list baru
"""

squares = [x**2 for x in range(5)]
print("squares:", squares)

# dengan if condition
even_squares = [x**2 for x in range(6) if x % 2 == 0]
print("even_squares:", even_squares)


# Kesimpulan:
# - For loop untuk iterasi pada iterable
# - While loop untuk kondisi True
# - Break, continue, else untuk kontrol alur
# - Bisa nested loop dan list comprehension