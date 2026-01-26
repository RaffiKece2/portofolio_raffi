# Nama : Muhammad Raffi Putra Umaryono
# Kelas : XI
# No.Basen : 25

from numpy.array_api import trunc

data = {
    "Nasi Goreng": 10000,
    "Nasi Bakar": 20000,
    "Nasi Kuning": 12000,
    "Nasi Bungkus": 6000

}


def pembelian():

    isi = []
    sama = "=" * 30
    print(sama, "Raffi Store", sama)

    for kunci, nilai in data.items():
        print(f"{kunci}: {nilai}")

    print(sama,"Proses Pembelian",sama)

    jumlah = int(input("Jumlah Porsi: "))

    for mulai in range(jumlah):
        user = input(f"Nama Porsi ke-{mulai+1}: ")
        isi.append(data[user])

    harga = sum(isi)
    total_harga = harga * jumlah

    print(f"Harga Total: {harga} x {jumlah} : {total_harga} Rp")

    if jumlah > 3:
        total_harga_ahkir = total_harga - 5000
        print("Selamat Anda Menapatkan Potongan Harga Sebesar 5000!")
        print(f"Harga Asli: {total_harga} Rp => Potongan Harga {total_harga} - 5000: {total_harga_ahkir} Rp ")
    else:
        print("Maaf Anda tidak bisa mendapatkan potongan harga!")
        print(f"Harga Asli: {total_harga} Rp")

    while True:
        print("[1] : kembali")

        pilih = int(input("Pilih: "))

        match pilih:
            case 1:
                tampilan()
            case _:
                print("Maaf saya tidak melayani!!")
        return  pilih


def tampilan():
    while True:
        sama = "=" * 30
        print(sama,"Raffi Store",sama)


        menu = ["Beli","Keluar"]

        for kunci,nilai in data.items():
            print(f"{kunci}: {nilai}")

        print(sama + sama + sama)

        for nomor,isi in enumerate(menu,start=1):
            print(f"[{nomor}]: {isi}")

        user = int(input("Pilih: "))

        match user:
            case 1:
                pembelian()
            case 2:
                 break
            case _:
                print("Maaf Saya tidak melayani tersebut")



if __name__ == "__main__":
    tampilan()
