# Perulangan dengan While adalah perulangan yang tidak diketahui akan berapa kali dilakukan perulangan nya

jumlah_buku = 10
print(f'jumlah buku yang ada adalah {jumlah_buku} buku')
jumlah_buku_yang_dibaca = 0

while jumlah_buku_yang_dibaca < jumlah_buku:
    print('baca 1 buku yang belum dibaca')
    jumlah_buku_yang_dibaca = jumlah_buku_yang_dibaca + 1
    print(f'buku ke {jumlah_buku_yang_dibaca} sudah dibaca')

print(f'jumlah buku yang sudah dibaca {jumlah_buku_yang_dibaca}')
