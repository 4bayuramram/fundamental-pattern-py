"""
KUNCI JAWABAN LATIHAN INPUT / OUTPUT
====================================
File ini berisi jawaban soal 1–10 dengan:
- Penjelasan menggunakan komentar
- Kode yang bisa dijalankan tanpa error
- Contoh output sesuai hasil ketika dijalankan

Catatan:
Untuk menjalankan file ini, silakan isi input sesuai instruksi.
"""
#jalankan file : python basic/04_input_dan_output/soal_dan_jawaban/01_jawaban.py 

print("\n==============================")
print("SOAL 1")
print("==============================")
# Soal: meminta nama lalu menampilkan "Halo, <nama>!"
nama = input("Masukkan nama Anda: ")
print(f"Halo, {nama}!")

# Contoh Output (jika input: Budi)
# Masukkan nama Anda: Budi
# Halo, Budi!


print("\n==============================")
print("SOAL 2")
print("==============================")
# Soal: meminta usia (integer), lalu tampilkan
usia = int(input("Masukkan usia Anda: "))
print(f"Usia kamu adalah {usia} tahun.")

# Contoh Output:
# Masukkan usia Anda: 20
# Usia kamu adalah 20 tahun.


print("\n==============================")
print("SOAL 3")
print("==============================")
# Soal: meminta dua angka, tampilkan penjumlahan
angka1 = float(input("Masukkan angka pertama: "))
angka2 = float(input("Masukkan angka kedua: "))
print(f"Hasil penjumlahan: {angka1 + angka2}")

# Contoh Output:
# Masukkan angka pertama: 5
# Masukkan angka kedua: 7
# Hasil penjumlahan: 12.0


print("\n==============================")
print("SOAL 4")
print("==============================")
# Soal: input float lalu tampilkan kembali
desimal = float(input("Masukkan angka desimal: "))
print(f"Angka desimal yang kamu masukkan adalah {desimal}")

# Contoh Output:
# Masukkan angka desimal: 3.14
# Angka desimal yang kamu masukkan adalah 3.14


print("\n==============================")
print("SOAL 5")
print("==============================")
# Soal: tampilkan 3 kata dipisahkan tanda "-"
print("Python", "itu", "mudah", sep="-")

# Contoh Output:
# Python-itu-mudah


print("\n==============================")
print("SOAL 6")
print("==============================")
# Soal: tampilkan 2 kalimat dalam satu baris dengan end
print("Ini kalimat pertama", end=" | ")
print("Ini kalimat kedua")

# Contoh Output:
# Ini kalimat pertama | Ini kalimat kedua


print("\n==============================")
print("SOAL 7")
print("==============================")
# Soal: input nama depan & belakang, tampilkan pakai f-string
nama_depan = input("Nama depan: ")
nama_belakang = input("Nama belakang: ")
print(f"Nama lengkap Anda adalah {nama_depan} {nama_belakang}")

# Contoh Output:
# Nama depan: Andi
# Nama belakang: Wijaya
# Nama lengkap Anda adalah Andi Wijaya


print("\n==============================")
print("SOAL 8")
print("==============================")
# Soal: input bilangan, tampilkan *2 dan /2
bil = float(input("Masukkan bilangan: "))
print(f"Dikali 2 = {bil * 2}")
print(f"Dibagi 2 = {bil / 2}")

# Contoh Output:
# Masukkan bilangan: 10
# Dikali 2 = 20.0
# Dibagi 2 = 5.0


print("\n==============================")
print("SOAL 9")
print("==============================")
# Soal: hitung luas persegi panjang
panjang = float(input("Masukkan panjang: "))
lebar = float(input("Masukkan lebar: "))
luas = panjang * lebar
print(f"Luas persegi panjang = {luas}")

# Contoh Output:
# Masukkan panjang: 5
# Masukkan lebar: 4
# Luas persegi panjang = 20.0


print("\n==============================")
print("SOAL 10")
print("==============================")
# Soal: kalkulator sederhana (+, -, *, /)
x = float(input("Masukkan angka pertama: "))
y = float(input("Masukkan angka kedua: "))

print(f"Hasil penjumlahan : {x + y}")
print(f"Hasil pengurangan : {x - y}")
print(f"Hasil perkalian   : {x * y}")
print(f"Hasil pembagian   : {x / y if y != 0 else 'Tidak bisa membagi dengan 0'}")

# Contoh Output:
# Masukkan angka pertama: 10
# Masukkan angka kedua: 2
# Hasil penjumlahan : 12
# Hasil pengurangan : 8
# Hasil perkalian   : 20
# Hasil pembagian   : 5.0