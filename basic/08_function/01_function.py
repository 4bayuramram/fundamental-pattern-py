"""

File ini berisi ringkasan tentang FUNCTION di Python
python basic/02_function/01_function.py (for run)
Ringkasan berdasarkan dokumentasi resmi Python.
'''
Fungsi di Python adalah blok kode yang dapat dipanggil berulang kali untuk melakukan tugas tertentu.
Python menggunakan kata kunci `def` untuk mendefinisikan fungsi. 
Fungsi dapat memiliki parameter, nilai default, *args, **kwargs, dan bisa mengembalikan nilai menggunakan `return`.
Python juga mendukung nested function, anonymous function (lambda), dan type hint.
Fungsi di Python fleksibel karena Python menggunakan dynamic typing.
'''
"""

# jalankan file : python basic/08_function/01_function.py

# 1. PENGENALAN FUNCTION
"""
Function adalah blok kode yang dapat dipanggil berulang kali.
Membantu modularisasi, mengurangi pengulangan, dan meningkatkan keterbacaan kode.
"""
def greet():
    print("Hello, World!")

greet()  # memanggil fungsi


# 2. FUNCTION DENGAN PARAMETER
def greet_name(name):
    print(f"Hello, {name}!")

greet_name("Alice")
greet_name("Bob")


# 3. RETURN VALUE
def add(a, b):
    return a + b

result = add(5, 3)
print("5 + 3 =", result)


# 4. PARAMETER DEFAULT
def power(base, exponent=2):
    return base ** exponent

print("3^2 =", power(3))
print("2^3 =", power(2, 3))


# 5. ARGUMENTS VARIABEL (*args)
def sum_all(*numbers):
    total = 0
    for n in numbers:
        total += n
    return total

print("sum_all(1,2,3,4) =", sum_all(1,2,3,4))


# 6. KEYWORD ARGUMENTS DAN **kwargs
def describe_person(name, **info):
    print(f"Name: {name}")
    for key, value in info.items():
        print(f"{key}: {value}")

describe_person("Alice", age=25, city="Jakarta")


# 7. ANONYMOUS FUNCTION (LAMBDA)
square = lambda x: x ** 2
print("square(5) =", square(5))

# bisa langsung dipakai
print("lambda 3^3 =", (lambda x: x**3)(3))


# 8. NESTED FUNCTION / INNER FUNCTION
def outer(msg):
    def inner():
        print("Inner says:", msg)
    inner()

outer("Hello from outer")


# 9. TYPE HINT (OPSIONAL)
def greet_typed(name: str) -> str:
    return f"Hello, {name}!"

print(greet_typed("Bob"))


# 10. DOCSTRING
def multiply(a: int, b: int) -> int:
    """Mengalikan dua bilangan dan mengembalikan hasilnya."""
    return a * b

print(multiply.__doc__)
print("4 * 5 =", multiply(4, 5))


# Kesimpulan:
# - Fungsi dibuat dengan def dan bisa dipanggil berkali-kali
# - Mendukung parameter, default, *args, **kwargs
# - Bisa mengembalikan nilai dengan return
# - Mendukung nested function dan lambda
# - Type hint opsional, docstring membantu dokumentasi