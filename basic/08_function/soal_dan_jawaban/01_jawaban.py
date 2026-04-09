"""
File: jawaban.py
Jawaban lengkap 10 soal Function Python untuk pemula
File ini berisi penjelasan detil setiap soal, syntax, pola penyelesaian, dan contoh output terminal.
Komentar panjang menggunakan triple quotes (docstring) untuk menjelaskan secara rinci.
"""

# jalankan file : python basic/08_function/soal_dan_jawaban/01_jawaban.py

# =========================================
# Soal 1
# =========================================
"""
Soal 1: Membuat fungsi greet() yang mencetak "Hello, World!"
Penjelasan:
- Fungsi dibuat dengan kata kunci 'def' diikuti nama fungsi dan tanda kurung ().
- Blok kode fungsi diindentasi di bawah definisi fungsi.
- Untuk menampilkan teks ke terminal digunakan print().
- Cara memanggil fungsi cukup dengan menulis nama_fungsi().
Output yang diharapkan:
Hello, World!
"""
def greet():
    print("Hello, World!")

greet()  # memanggil fungsi
print("-"*30)

# =========================================
# Soal 2
# =========================================
"""
Soal 2: Fungsi greet_name(name) yang menerima parameter.
Penjelasan:
- Parameter adalah variabel yang diterima fungsi saat dipanggil.
- Gunakan f-string untuk menampilkan nilai parameter di string.
- Syntax: def nama_fungsi(param): ...
Output contoh:
Hello, Alice!
Hello, Bob!
"""
def greet_name(name):
    print(f"Hello, {name}!")

greet_name("Alice")
greet_name("Bob")
print("-"*30)

# =========================================
# Soal 3
# =========================================
"""
Soal 3: Fungsi add(a,b) yang mengembalikan hasil penjumlahan.
Penjelasan:
- Fungsi bisa mengembalikan nilai dengan kata kunci 'return'.
- Return memungkinkan kita menyimpan hasil fungsi di variabel.
- Output contoh: 5 + 7 = 12
"""
def add(a, b):
    return a + b

result = add(5, 7)
print("5 + 7 =", result)
print("-"*30)

# =========================================
# Soal 4
# =========================================
"""
Soal 4: Fungsi power(base, exponent=2) dengan parameter default.
Penjelasan:
- Parameter default digunakan jika argumen tidak diberikan.
- Operator pangkat di Python menggunakan '**'.
- Output contoh:
3^2 = 9
2^3 = 8
"""
def power(base, exponent=2):
    return base ** exponent

print("3^2 =", power(3))
print("2^3 =", power(2, 3))
print("-"*30)

# =========================================
# Soal 5
# =========================================
"""
Soal 5: Fungsi sum_all(*numbers) menerima jumlah argumen variabel.
Penjelasan:
- *args memungkinkan menerima 0 atau lebih argumen posisional.
- Gunakan loop untuk menjumlahkan semua nilai.
- Output contoh: sum_all(1,2,3,4,5) = 15
"""
def sum_all(*numbers):
    total = 0
    for n in numbers:
        total += n
    return total

print("sum_all(1,2,3,4,5) =", sum_all(1,2,3,4,5))
print("-"*30)

# =========================================
# Soal 6
# =========================================
"""
Soal 6: Fungsi describe_person(name, **info)
Penjelasan:
- **kwargs menerima argumen keyword dalam bentuk dictionary.
- Gunakan items() untuk iterasi key dan value.
- Output contoh:
Name: Alice
age: 25
city: Jakarta
"""
def describe_person(name, **info):
    print(f"Name: {name}")
    for key, value in info.items():
        print(f"{key}: {value}")

describe_person("Alice", age=25, city="Jakarta")
print("-"*30)

# =========================================
# Soal 7
# =========================================
"""
Soal 7: Lambda function untuk menghitung kuadrat.
Penjelasan:
- Lambda adalah fungsi anonim (tanpa nama) untuk ekspresi sederhana.
- Syntax: lambda parameter: ekspresi
- Bisa dipanggil langsung atau disimpan di variabel.
- Output contoh: square(6) = 36
"""
square = lambda x: x ** 2
print("square(6) =", square(6))
print("-"*30)

# =========================================
# Soal 8
# =========================================
"""
Soal 8: Nested function / inner function
Penjelasan:
- Fungsi bisa didefinisikan di dalam fungsi lain.
- Inner function hanya bisa diakses di dalam outer function.
- Berguna untuk enkapsulasi atau closure.
- Output contoh: Inner says: Hello
"""
def outer(msg):
    def inner():
        print("Inner says:", msg)
    inner()

outer("Hello")
print("-"*30)

# =========================================
# Soal 9
# =========================================
"""
Soal 9: Fungsi greet_typed(name: str) -> str dengan type hint
Penjelasan:
- Type hint memberi info tipe parameter dan return, tidak memaksa tipe.
- Syntax: def fungsi(param: tipe) -> tipe: ...
- Output contoh: Hello, Bob!
"""
def greet_typed(name: str) -> str:
    return f"Hello, {name}!"

print(greet_typed("Bob"))
print("-"*30)

# =========================================
# Soal 10
# =========================================
"""
Soal 10: Fungsi multiply(a:int, b:int) -> int dengan docstring
Penjelasan:
- Docstring adalah string di awal fungsi untuk dokumentasi.
- Bisa diakses dengan __doc__.
- Output contoh:
Mengalikan dua bilangan dan mengembalikan hasilnya.
4 * 5 = 20
"""
def multiply(a: int, b: int) -> int:
    """Mengalikan dua bilangan dan mengembalikan hasilnya."""
    return a * b

print(multiply.__doc__)
print("4 * 5 =", multiply(4, 5))
print("-"*30)

# =========================================
# Kesimpulan
# =========================================
"""
Kesimpulan dari 10 soal:
1. Fungsi dibuat dengan 'def', bisa dipanggil berkali-kali.
2. Parameter dan return value membantu fungsi fleksibel dan modular.
3. Parameter default, *args, **kwargs meningkatkan fleksibilitas pemanggilan.
4. Lambda digunakan untuk fungsi sederhana, nested function untuk enkapsulasi.
5. Type hint dan docstring membantu dokumentasi dan pembelajaran.
6. Pemula belajar pola membuat fungsi, memanggil, mengembalikan nilai, dan membaca komentar penjelasan.
"""