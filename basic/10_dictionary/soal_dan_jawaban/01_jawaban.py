"""
File ini berisi jawaban untuk 10 soal Python Dictionary.
Setiap soal disertai penjelasan syntax, cara menjawab, dan output terminal.
Penjelasan ditujukan agar pemula memahami konsep dictionary di Python.
"""

# jalankan file : python basic/10_dictionary/soal_dan_jawaban/01_jawaban.py

# -------------------------------
# SOAL 1
# -------------------------------
# Tugas: Buat dictionary student dengan key "name" dan "age"
# Penjelasan:
# - Dictionary dibuat dengan tanda kurung kurawal {}
# - Format: key: value
# - key adalah string, value bisa int, str, bool, dll.
student = {"name": "Alice", "age": 20}

# Print dictionary untuk melihat isinya
print("SOAL 1 Output:", student)
"""
Output:
SOAL 1 Output: {'name': 'Alice', 'age': 20}
"""

# -------------------------------
# SOAL 2
# -------------------------------
# Tugas: Tambahkan key "major" = "Physics"
# Penjelasan:
# - Menambahkan key baru cukup dengan assignment: dict[key] = value
student["major"] = "Physics"
print("SOAL 2 Output:", student)
"""
Output:
SOAL 2 Output: {'name': 'Alice', 'age': 20, 'major': 'Physics'}
"""

# -------------------------------
# SOAL 3
# -------------------------------
# Tugas: Ubah value key "age" menjadi 21
# Penjelasan:
# - Update value dictionary sama seperti menambahkan key baru
student["age"] = 21
print("SOAL 3 Output:", student)
"""
Output:
SOAL 3 Output: {'name': 'Alice', 'age': 21, 'major': 'Physics'}
"""

# -------------------------------
# SOAL 4
# -------------------------------
# Tugas: Hapus key "major"
# Penjelasan:
# - Gunakan del dict[key] untuk menghapus key tertentu
del student["major"]
print("SOAL 4 Output:", student)
"""
Output:
SOAL 4 Output: {'name': 'Alice', 'age': 21}
"""

# -------------------------------
# SOAL 5
# -------------------------------
# Tugas: Gunakan .get() untuk mengambil "name" dan "city" (default "Unknown")
# Penjelasan:
# - dict.get(key, default) mengembalikan default jika key tidak ada
name_value = student.get("name")
city_value = student.get("city", "Unknown")
print("SOAL 5 Output: Name =", name_value, "City =", city_value)
"""
Output:
SOAL 5 Output: Name = Alice City = Unknown
"""

# -------------------------------
# SOAL 6
# -------------------------------
# Tugas: Dictionary comprehension untuk squares 0-4
# Penjelasan:
# - Pola: {key_expression: value_expression for variable in iterable}
# - Membuat dictionary dari iterable lebih ringkas
squares = {x: x**2 for x in range(5)}
print("SOAL 6 Output:", squares)
"""
Output:
SOAL 6 Output: {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
"""

# -------------------------------
# SOAL 7
# -------------------------------
# Tugas: Looping dictionary student print key dan value
# Penjelasan:
# - Bisa loop langsung pada dictionary (iterasi key)
# - Bisa loop items() untuk iterasi key & value bersamaan
print("SOAL 7 Output:")
for key, value in student.items():
    print("Key:", key, "Value:", value)
"""
Output:
SOAL 7 Output:
Key: name Value: Alice
Key: age Value: 21
"""

# -------------------------------
# SOAL 8
# -------------------------------
# Tugas: Nested dictionary classroom
# Penjelasan:
# - Dictionary bisa berisi dictionary lain (nested)
# - Akses nested dictionary dengan dict[key1][key2]
classroom = {
    "student1": {"name": "Alice", "age": 20},
    "student2": {"name": "Bob", "age": 22}
}
print("SOAL 8 Output: student2 age =", classroom["student2"]["age"])
"""
Output:
SOAL 8 Output: student2 age = 22
"""

# -------------------------------
# SOAL 9
# -------------------------------
# Tugas: Copy dictionary student dan ubah nama di salinan
# Penjelasan:
# - .copy() membuat shallow copy dictionary
# - Perubahan di salinan tidak memengaruhi original
student_copy = student.copy()
student_copy["name"] = "Charlie"
print("SOAL 9 Output: Original =", student, "Copy =", student_copy)
"""
Output:
SOAL 9 Output: Original = {'name': 'Alice', 'age': 21} Copy = {'name': 'Charlie', 'age': 21}
"""

# -------------------------------
# SOAL 10
# -------------------------------
# Tugas: Looping dictionary student print semua pasangan key-value
# Penjelasan:
# - .items() mengembalikan iterable tuple (key, value)
print("SOAL 10 Output:")
for key, value in student.items():
    print(key, ":", value)
"""
Output:
SOAL 10 Output:
name : Alice
age : 21
"""

# -------------------------------
# KESIMPULAN
# -------------------------------
"""
Dari 10 soal di atas, pemahaman yang dipelajari:
1. Cara membuat dictionary dan menambahkan key-value
2. Mengubah dan menghapus item
3. Mengakses item dengan [] dan .get()
4. Looping dictionary dengan key, value, atau items()
5. Dictionary comprehension
6. Nested dictionary dan cara mengaksesnya
7. Copy dictionary dan perbedaan original vs salinan

Pemula bisa mempelajari pola:
- Assignment key-value untuk membuat dan update
- del dan pop untuk menghapus
- items() untuk iterasi key-value
- Dictionary comprehension untuk membuat dictionary cepat
- Nested dictionary untuk struktur data kompleks
"""
