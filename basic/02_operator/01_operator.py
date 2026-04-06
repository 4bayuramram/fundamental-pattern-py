
# Import module operator
import operator

#  File ini berisi ringkasan operator Python untuk pemula
# python basic/02_operator/01_operator.py (for run)

# in place operator 

# 1. OPERATOR ARITMATIKA

a = 10
b = 3

# penjumlahan
print("a + b =", a + b)

# pengurangan
print("a - b =", a - b)

# perkalian
print("a * b =", a * b)

# pembagian
print("a / b =", a / b)

# pembagian bulat
print("a // b =", a // b)

# sisa bagi
print("a % b =", a % b)

# pangkat
print("a ** b =", a ** b)


# 2. OPERATOR PERBANDINGAN

print("a > b =", a > b)
print("a < b =", a < b)
print("a == b =", a == b)
print("a != b =", a != b)
print("a >= b =", a >= b)
print("a <= b =", a <= b)


# 3. OPERATOR LOGIKA

x = True
y = False

print("x AND y =", x and y)
print("x OR y =", x or y)
print("NOT x =", not x)


# 4. OPERATOR MEMBERSHIP

data = [1, 2, 3]

print("2 in data =", 2 in data)
print("5 not in data =", 5 not in data)


# 5. OPERATOR IDENTITY

n = None

print("n is None =", n is None)
print("n is not None =", n is not None)


# 6. MODULE OPERATOR (VERSI FUNGSI)

import operator

'''
Module operator adalah versi fungsi dari operator biasa.
Contoh:
a + b  sama dengan operator.add(a,b)
'''

print("operator.add(a,b) =", operator.add(a, b))
print("operator.sub(a,b) =", operator.sub(a, b))
print("operator.mul(a,b) =", operator.mul(a, b))
print("operator.truediv(a,b) =", operator.truediv(a, b))


# contoh in-place operator

value = 10

value = operator.iadd(value, 5)

print("hasil operator.iadd =", value)


# module operator

'''
Module operator memungkinkan kita memakai operator seperti +, -, ==, dll
dalam bentuk fungsi. Contoh:
operator.add(a,b) sama dengan a + b
Tujuan file ini: membantu memahami konsep operator dasar Python
'''

print("=== CONTOH OPERATOR PYTHON ===")



# 1. OPERATOR PERBANDINGAN


a = 5
b = 3

# operator.lt artinya kurang dari (<)
print("a < b:", operator.lt(a, b))

# operator.eq artinya sama dengan (==)
print("a == b:", operator.eq(a, b))

# operator.gt artinya lebih besar (>)
print("a > b:", operator.gt(a, b))



# 2. OPERATOR LOGIKA


# operator.not_ artinya NOT
print("not True:", operator.not_(True))

# operator.truth mengecek apakah bernilai True
print("truth(1):", operator.truth(1))

# operator.is_ mengecek apakah objek sama
x = None
print("x is None:", operator.is_(x, None))



# 3. OPERATOR MATEMATIKA


x = 10
y = 2

# penjumlahan
print("x + y:", operator.add(x, y))

# pengurangan
print("x - y:", operator.sub(x, y))

# perkalian
print("x * y:", operator.mul(x, y))

# pembagian
print("x / y:", operator.truediv(x, y))

# pangkat
print("x ** y:", operator.pow(x, y))


# 4. OPERATOR BITWISE (LANJUTAN)


'''
Bitwise bekerja pada angka biner.
Biasanya dipakai di level lanjutan seperti manipulasi data low-level.
Untuk pemula cukup kenal saja dulu.
'''

print("5 & 3:", operator.and_(5, 3))
print("5 | 3:", operator.or_(5, 3))
print("5 ^ 3:", operator.xor(5, 3))



# 5. OPERATOR SEQUENCE (LIST / STRING)


data = [1,2,3]

# mengambil index
print("index ke-1:", operator.getitem(data, 1))

# cek apakah ada nilai
print("2 in data:", operator.contains(data, 2))

# gabung list
print("gabung list:", operator.concat(data, [4,5]))


# 6. OPERATOR IN-PLACE (+= dll)
'''
Operator in-place seperti += *= dll
mengubah nilai variabel langsung.
'''

n = 10

operator.iadd(n, 5)
print("contoh iadd:", n)


#  Kesimpulan:
#  operator module = versi fungsi dari operator Python biasa
#  dipakai saat butuh operator sebagai fungsi
