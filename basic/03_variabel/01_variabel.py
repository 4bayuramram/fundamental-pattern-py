"""
File ini berisi ringkasan tentang VARIABEL di Python
python basic/01_variabel/01_variabel.py (for run)
Ringkasan berdasarkan dokumentasi resmi Python.
'''
Variabel pada Python bersifat sangat sederhana karena 
menggunakan dynamic typing, sehingga tidak perlu 
mendeklarasikan tipe dan nilainya dapat berubah kapan saja,
 berbeda dengan Java yang menggunakan static typing sehingga 
 setiap variabel wajib memiliki tipe dan tidak dapat berganti tipe.
  JavaScript juga bersifat dinamis tetapi tetap membutuhkan keyword 
  seperti var, let, atau const serta memiliki mekanisme hoisting yang 
  tidak dimiliki Python, sementara PHP mirip dengan Python dalam 
  fleksibilitas tipe namun memakai tanda $ pada setiap variabel. 
  Secara umum Python adalah yang paling ringkas dan bersih dalam 
  penulisan variabel, Java yang paling ketat, dan JavaScript serta 
  PHP berada di tengah dengan aturan tambahan tertentu.
'''
"""
# jalankan file : python basic/03_variabel/01_variabel.py

# 1. PENGENALAN VARIABEL

# Variabel adalah nama yang menyimpan nilai.
# Python tidak membutuhkan deklarasi tipe.

x = 10
name = "Alice"
is_active = True

print("x =", x)
print("name =", name)
print("is_active =", is_active)


# 2. ATURAN PENAMAAN VARIABEL
"""
- Harus dimulai huruf atau underscore
- Tidak boleh diawali angka
- Menggunakan huruf, angka, underscore
- Case-sensitive (age, Age, AGE adalah variabel berbeda)
"""

_valid = 1
age2 = 20
Age = 30

print("_valid =", _valid)
print("age2 =", age2)
print("Age =", Age)


# 3. TIPE DATA OTOMATIS (DYNAMIC TYPING)
"""
Python menentukan tipe berdasarkan nilai.
Variabel bisa berubah tipe kapan saja.
"""

n = 5
print("n awal =", n, "(int)")

n = "lima"  # berubah jadi string
eprint = print  # alias untuk fungsi bawaan
print("n berubah =", n, "(str)")


# 4. ASSIGNMENT MULTIPLE (MENETAPKAN BEBERAPA NILAI SEKALIGUS)

a, b, c = 1, 2, 3
print("a, b, c =", a, b, c)

# swap nilai
x, y = 10, 20
x, y = y, x
print("swap -> x =", x, "y =", y)


# 5. ASSIGNMENT KE NILAI YANG SAMA

p = q = r = 100
print("p, q, r =", p, q, r)


# 6. TIPE IMMUTABLE DAN MUTABLE
"""
Immutable: int, float, str, tuple
Mutable: list, dict, set
"""

# contoh immutable
num = 10
print("num id awal =", id(num))
num += 1
print("num id setelah += 1 =", id(num))

# contoh mutable
items = [1, 2, 3]
print("items id awal =", id(items))
items.append(4)
print("items id setelah append =", id(items))


# 7. TYPE HINT (OPSIONAL)
"""
Type hint tidak mengubah perilaku tetapi membantu dokumentasi.
"""

age: int = 25
name: str = "Bob"

print("age =", age)
print("name =", name)


# 8. UNPACKING VARIABEL

data = [10, 20, 30]
x1, x2, x3 = data

print("unpacking:", x1, x2, x3)


# Kesimpulan:
# - Variabel menyimpan nilai tanpa deklarasi tipe
# - Nama variabel mengikuti aturan tertentu
# - Tipe data fleksibel (dinamis)
# - Bisa multiple assignment dan unpacking
# - Mutable vs immutable memengaruhi perubahan nilai