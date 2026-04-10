"""
File ini berisi ringkasan tentang DICTIONARY di Python
python basic/02_dictionary/01_dictionary.py (for run)
Ringkasan berdasarkan dokumentasi resmi Python.
"""
# jalankan file : python basic/10_dictionary/01_dictionary.py

# 1. PENGENALAN DICTIONARY
"""
Dictionary adalah struktur data berbasis key-value.
Setiap key unik dan digunakan untuk mengakses nilainya.
Mirip dengan object di JavaScript atau map di Java.
"""

# membuat dictionary
person = {
    "name": "Alice",
    "age": 25,
    "is_active": True
}

print("person =", person)

# mengakses nilai
print("Nama:", person["name"])
print("Umur:", person["age"])
print("Status aktif:", person["is_active"])

# 2. MENAMBAH & MEMPERBARUI NILAI
"""
- Menambahkan key baru atau mengubah value key lama
"""

# menambahkan key baru
person["city"] = "Jakarta"
print("Tambah city:", person)

# mengubah value
person["age"] = 26
print("Update age:", person)

# 3. MENGHAPUS ITEM
"""
- del dictionary[key] -> menghapus key tertentu
- pop(key) -> menghapus dan mengembalikan nilai
- clear() -> menghapus semua isi dictionary
"""

# menggunakan del
del person["is_active"]
print("Setelah del is_active:", person)

# menggunakan pop
age = person.pop("age")
print("Pop age:", age)
print("Dictionary sekarang:", person)

# menggunakan clear
temp_dict = {"x": 1, "y": 2}
temp_dict.clear()
print("Clear temp_dict:", temp_dict)

# 4. METHOD POPULER
"""
- keys() -> semua key
- values() -> semua value
- items() -> semua pasangan (key, value)
- get(key, default) -> ambil value, default jika key tidak ada
"""

person = {"name": "Alice", "age": 25}

print("Keys:", person.keys())
print("Values:", person.values())
print("Items:", person.items())
print("Get city (default 'Unknown'):", person.get("city", "Unknown"))

# 5. ITERASI DICTIONARY
"""
Looping key, value, atau keduanya
"""

for key in person:
    print("Key:", key, "Value:", person[key])

for key, value in person.items():
    print("Key:", key, "Value:", value)

# 6. DICTIONARY COMPREHENSION
"""
Membuat dictionary dari iterable dengan satu baris
"""

squares = {x: x**2 for x in range(5)}
print("Squares:", squares)

# 7. COPY & SHALLOW VS DEEP COPY
import copy

dict1 = {"a": 1, "b": [1, 2]}
shallow = dict1.copy()  # salinan dangkal
deep = copy.deepcopy(dict1)  # salinan dalam

dict1["b"].append(3)
print("Original:", dict1)
print("Shallow copy:", shallow)
print("Deep copy:", deep)

# 8. NESTED DICTIONARY
"""
Dictionary bisa berisi dictionary lain
"""

data = {
    "person1": {"name": "Alice", "age": 25},
    "person2": {"name": "Bob", "age": 30}
}

print("Nested dict person1:", data["person1"])
print("Nested dict person2 age:", data["person2"]["age"])

# Kesimpulan:
# - Dictionary menyimpan pasangan key-value
# - Key harus unik dan immutable
# - Mutable dan fleksibel
# - Banyak method built-in untuk manipulasi
# - Bisa nested dan comprehension