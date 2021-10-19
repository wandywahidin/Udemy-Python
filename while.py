# Perulangan dengan While adalah perulangan yang tidak diketahui akan berapa kali dilakukan perulangan nya

"""
jumlah_buku = 10
print(f'jumlah buku yang ada adalah {jumlah_buku} buku')
jumlah_buku_yang_dibaca = 0

while jumlah_buku_yang_dibaca < jumlah_buku:
    print('baca 1 buku yang belum dibaca')
    jumlah_buku_yang_dibaca = jumlah_buku_yang_dibaca + 1
    print(f'buku ke {jumlah_buku_yang_dibaca} sudah dibaca')

print(f'jumlah buku yang sudah dibaca {jumlah_buku_yang_dibaca}')
"""

jumlah_buku = 10
print(f'jumlah buku yang ada adalah {jumlah_buku} buku')
total_baca = 0
jumlah_buku_yang_dibaca_dan_dipahami = 0

while total_baca < jumlah_buku * 2:
    total_baca = total_baca + 1
    if jumlah_buku_yang_dibaca_dan_dipahami == jumlah_buku - 1:
        print(f'buku ke {jumlah_buku_yang_dibaca_dan_dipahami + 1} belum paham')
    else:
        jumlah_buku_yang_dibaca_dan_dipahami = jumlah_buku_yang_dibaca_dan_dipahami + 1
        print(f'buku ke {jumlah_buku_yang_dibaca_dan_dipahami} sudah dibaca dan dipahami')
