
def mod(n):
    total = (n // 1000) % n

    return total


def publik(angka_awal):
    return  angka_awal


def privasi(angka_pilihan):
    return angka_pilihan

privasi_key = privasi(4)

def total1(privasi):
    publik_key = publik(5)
    modulus = mod(43)
    hasil = publik_key ** privasi + modulus
    return hasil


enkripsi_pertama = total1(privasi_key)

print("Kode Pertama: ",enkripsi_pertama)

enkripsi_dua = total1(enkripsi_pertama)
print("Kode Dua: ",enkripsi_dua)


dekripsi = total1(enkripsi_dua)
print("kode tiga: ",dekripsi)



