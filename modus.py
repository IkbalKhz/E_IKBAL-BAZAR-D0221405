# membuat list
data = [0, 2, 2, 1, 4, 0, 5]

# membuat dictionary untuk menghitung frekuensi setiap bilangan
frekuensi = {}
for i in data:
    frekuensi[i] = frekuensi.get(i, 0) + 1

# mencari bilangan dengan frekuensi tertinggi
modus = max(frekuensi, key=frekuensi.get)

# menampilkan hasil modus
print("Modus dari bilangan yang diberikan adalah:", modus)
