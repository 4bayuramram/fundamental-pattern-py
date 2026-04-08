"""
05_CONTROL_FLOW_IF.py
=====================

Materi: Control Flow di Python
Topik: if, elif, else

File ini dirancang agar:
- Pemula mudah memahami (penjelasan dengan komentar)
- Berisi contoh penggunaan if, elif, else
- Bisa dijalankan tanpa error
- Mengacu pada dokumentasi resmi Python:
  https://docs.python.org/3/tutorial/controlflow.html

------------------------------------------------
Apa itu Control Flow?
------------------------------------------------
Control Flow adalah cara program mengambil keputusan
berdasarkan kondisi tertentu.

Digunakan untuk:
• Percabangan logika
• Menentukan aksi berdasarkan kondisi

Di Python digunakan dengan:
if, elif, else
"""

# jalankan file:
# python basic/05_control_flow/01_control_flow.py

# ---------------------------------------------------------
# 1. Struktur Dasar if
# ---------------------------------------------------------
"""
SINTAX DASAR:
-------------
if kondisi:
    aksi

CATATAN:
• kondisi harus bernilai True atau False
• gunakan indentasi (spasi) untuk blok kode
"""

# Contoh 1 — if sederhana
umur = 18

if umur >= 18:
    print("Anda sudah dewasa")


# ---------------------------------------------------------
# 2. if - else
# ---------------------------------------------------------
"""
Digunakan jika ada dua kemungkinan kondisi

SINTAX:
-------
if kondisi:
    aksi jika True
else:
    aksi jika False
"""

# Contoh 2
nilai = 70

if nilai >= 75:
    print("Lulus")
else:
    print("Tidak lulus")


# ---------------------------------------------------------
# 3. if - elif - else
# ---------------------------------------------------------
"""
Digunakan untuk banyak kondisi

SINTAX:
-------
if kondisi1:
    aksi1
elif kondisi2:
    aksi2
else:
    aksi default
"""

# Contoh 3
nilai = 85

if nilai >= 90:
    print("Grade A")
elif nilai >= 75:
    print("Grade B")
elif nilai >= 60:
    print("Grade C")
else:
    print("Grade D")


# ---------------------------------------------------------
# 4. Perbandingan & Operator Logika
# ---------------------------------------------------------
"""
Operator Perbandingan:
>   lebih besar
<   lebih kecil
>=  lebih besar sama dengan
<=  lebih kecil sama dengan
==  sama dengan
!=  tidak sama

Operator Logika:
and, or, not
"""

# Contoh 4
umur = 20
punya_ktp = True

if umur >= 17 and punya_ktp:
    print("Boleh membuat SIM")


# ---------------------------------------------------------
# 5. if bersarang (nested if)
# ---------------------------------------------------------
"""
if di dalam if
"""

# Contoh 5
umur = 20
punya_uang = True

if umur >= 18:
    if punya_uang:
        print("Boleh masuk bioskop")
    else:
        print("Tidak punya uang")
else:
    print("Masih di bawah umur")


# ---------------------------------------------------------
# 6. Penulisan singkat (ternary)
# ---------------------------------------------------------
"""
SINTAX:
-------
nilai_if_true if kondisi else nilai_if_false
"""

# Contoh 6
umur = 16
status = "Dewasa" if umur >= 18 else "Anak-anak"
print(status)


# ---------------------------------------------------------
# 7. Mini latihan
# ---------------------------------------------------------
"""
Buat program:
• input nilai
• tampilkan kategori:
  A (>=90), B (>=75), C (>=60), D (<60)
"""

print("\n=== LATIHAN MINI ===")
nilai = int(input("Masukkan nilai: "))

if nilai >= 90:
    print("Grade A")
elif nilai >= 75:
    print("Grade B")
elif nilai >= 60:
    print("Grade C")
else:
    print("Grade D")


# ---------------------------------------------------------
# 8. Kesimpulan
# ---------------------------------------------------------
"""
• if → untuk satu kondisi
• if-else → dua kemungkinan
• if-elif-else → banyak kondisi
• Gunakan indentasi dengan benar
• Bisa menggunakan operator logika untuk kondisi kompleks

Selamat belajar Control Flow di Python!
"""