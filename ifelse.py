"""
Semua sintaksis dasar bahasa pemograman terdiri dari :
1. Sekuensial : Langkah berurutan
2. Percabangan : Langkah melompat jika kondisi terpenuhi
3. Perulangan : Mengulang langkah yang sama berkali-kali sampai kondisi terpenuhi
"""

# sekuensial
print('ibu berkata, "pergi ke toko"')
print('budi menjawab, "apa yang harus saya lakukan di toko?"')
print('ibu menjawab, "beli satu botol susu, dan jika ada telur beli 6"')
print('maka budi berangkat ke toko')

# Percabangan
susu_yang_dibeli = 2
telur_yang_dibeli = 10
uang = 20000
jumlah_susu_tersedia = 3
jumlah_telur_tersedia = 8
harga_susu = 5000
harga_telur = 1000
bayar_susu = susu_yang_dibeli * harga_susu
bayar_telur = telur_yang_dibeli * harga_telur

if jumlah_susu_tersedia >= susu_yang_dibeli and uang >= bayar_susu :
    if jumlah_telur_tersedia >= telur_yang_dibeli and uang >= bayar_susu + bayar_telur :
        print(f'Membeli {susu_yang_dibeli} botol susu dan {telur_yang_dibeli} telur')
    else:
        print(f'membeli {susu_yang_dibeli} botol susu')
else:
    print('tidak jadi membeli susu')



