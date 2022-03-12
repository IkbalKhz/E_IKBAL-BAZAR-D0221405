print("Hello Kalian")
cam = "Apa Kabar Kalian"
print(cam)

# tipe bool adalah nilai true atau false
tipe_bool = False
print("data :",tipe_bool)
print("bertipe :", type(tipe_bool))

# tipe data stiring adalah sekumpulan karakter
tipe_str = "ucup"
print("data :", tipe_str, "bertipe :", type(tipe_str))

# tipe integer adalah angka satuan
tipe_int = 10
print("data :", tipe_int, "bertipe :", type(tipe_int))

# tipe data float adalah angka yang mempunyai koma
tipe_float = 1.9
print("data :", tipe_float, "bertipe :", type(tipe_float))

print("========================")
print("OPERATOR ARITMATIKA")
print("="*25)
x = 10
y = 5
# PERJUMLAHAN
print(x + y)
# PENGURANGAN
print(x - y)
# PERKALIAN
print(x * y)
# PEMBAGIAN
print(x / y)
# MODULO ATAU SISAH BAGI
print(x % y)
# PANGKAT
print(x ** y)
# PEMBAGIAN BULAT
print(x // y)

print("========================")
print("KALKULATOR SEDERHANA")
print("="*25)
nilai1 = int(input("Masukkan bilangan pertama :"))
nilai2 = int(input("Masukkan bilangan kedua :"))
print("""pilih operator aritmatika yang ingin digunakan
a. perjumlahan
b. pengurangan
c. perkalian
d. pembgaian
e. modulo
f. pangkat
g. pembagian bulat""")

operasi = input("masukkan pilihan anda yang ada di atas :")
if operasi == "a" :
    nilai = nilai1 + nilai2
    print("Hasil :",nilai)
elif operasi == "b" :
    nilai = nilai1 - nilai2
    print("Hasil :", nilai)
elif operasi == "c" :
    nilai = nilai1 * nilai2
    print("Hasil :", nilai)
elif operasi == "d" :
    nilai = nilai1 / nilai2
    print("Hasil :", nilai)
elif operasi == "e" :
    nilai = nilai1 % nilai2
    print("Hasil :", nilai)
elif operasi == "f" :
    nilai = nilai1 ** nilai2
    print("Hasil :", nilai)
elif operasi == "g" :
    nilai = nilai1 // nilai2
    print("Hasil :", nilai)
else :
    print("hasil tidak terdefenisi")

print("========================")
print("TANTANGAN")
print("="*25)

nim = "D0221405"
gaji_pokok = 1000000
print("gaji pokok :", gaji_pokok)
gaji_lembur_perjam = 5000
print("gaji lembur perjam :", gaji_lembur_perjam)
lama_lembur = int(input("masukkan lama lembur :"))
pajak = 10/100
# penyelesaian
gaji_lembur = gaji_lembur_perjam * lama_lembur
gaji_kotor = gaji_pokok + gaji_lembur
potongan_pajak = gaji_kotor * pajak
gaji_bersih = gaji_kotor - potongan_pajak
print("gaji anda sebelum potong pajak sebesar :", gaji_kotor)
print("gaji anda setelahh potong pajak sebesar :", gaji_bersih)
