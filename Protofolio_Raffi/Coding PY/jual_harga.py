from rich.console import Console
from rich.text import Text
from rich.panel import Panel
from rich.table import Table
from rich.prompt import Prompt
import datetime




class Tokoh:
    def __init__(self):
        self.console = Console()
        self.saldo = 0
        self.pesan = ""
        self.akun = {}
        self.keranjang = []
        self.harga_keranjang = []
        self.isi_keranjang = {}
        self.saldo_c = [10000,25000,50000,81000]
        self.saldo_r = [150000,290000,570000,950000]
        self.isi_menu = ["Lihat Dompet","Tambahkan Dompet","Shop","Keranjang"]
        self.cetak_pesan = None
        self.im = []
        self.isi_shop = ["Sepatu","Baju","Topi"]
        self.sepatu = ["Sepatu jordan","Sepatu nike v12","Sepatu adidas","Sepatu wakai","Sepatu converse"]
        self.sepatu_harga = [250000,130000,350000,95000,700000]
        self.baju = ["T-shirt blue","T-shirt Light blue","T-shirt gambar logo spiderman","Polo shirt red","Baju kemeja"]
        self.baju_harga = [450000,200000,150000,650000,270000]
        self.topi = ["Topi trucker","Flat cap","Topi jerami","Topi boater","Topi rimba"]
        self.topi_harga = [260000,60000,36000,150000,56000]



    def daftar(self):
        judul = Text( "Daftar RaffiShop",style = "bold cyan")
        self.console.print(" " * 50,judul," " * 50)

        while True:
            try:
                username = Prompt.ask("[bold green] Username:[/bold green] ")
                password = int(Prompt.ask("[bold green] Password:[/bold green] "))

                self.akun[username] = password


                self.pesan = "Daftar Berhasil"
                self.cetak_pesan = Text(f"Pesan: {self.pesan}", style="blue")

                if self.cetak_pesan is not None:
                    self.console.print(self.cetak_pesan)
                    tokoh_raffi.menu()

                return

            except ValueError:

                self.pesan = "Anda Harus Menggunakan Angka bukan Huruf"
                self.cetak_pesan = Text(f"Pesan: {self.pesan}", style="blue")
                if self.cetak_pesan is not None:
                    self.console.print(self.cetak_pesan)

    def menu(self):

        teks = ""
        teks2 = "[5].Keluar"

        for nomor,nama in enumerate(self.isi_menu,start=1):
            teks += f" [{nomor}].{nama}\n"

        panel = Panel(f"{teks}",title="RaffiShop",border_style="cyan",style="bold green",title_align="center")
        panel2 = Panel(f"{teks2}",style="bold red",)
        self.console.print(panel,panel2)


        for kunci,nilai in self.akun.items():
            self.im.append(kunci)

        while True:
            try:
                pilih_a = int(Prompt.ask(f"[blue]{self.im[0]}:[/blue] "))

                if pilih_a == 1:
                    isi_s = Text(f"Dompet: {self.saldo}",style="bold green")
                    self.console.print(isi_s)
                elif pilih_a == 2:
                    tokoh_raffi.tambah_saldo()

                elif pilih_a == 3:
                    tokoh_raffi.shop()
                elif pilih_a == 4:

                    tokoh_raffi.c_keranjang()

                elif pilih_a == 5:
                    self.pesan = "Terimakasih Kembali Jangan Lupa Semoga Hari mu Indah !!"
                    self.cetak_pesan = Text(f"Pesan: {self.pesan}", style="blue")
                    if self.cetak_pesan is not None:
                        self.console.print(self.cetak_pesan)

                    return

                else:
                    self.pesan = "Maaf pilihan itu tidak ada coba lagi!!"
                    self.cetak_pesan = Text(f"Pesan: {self.pesan}", style="blue")
                    if self.cetak_pesan is not None:
                        self.console.print(self.cetak_pesan)
            except ValueError:
                self.pesan = "Maaf Anda Harus Menggunakan Angka ya!!"
                self.cetak_pesan = Text(f"Pesan: {self.pesan}", style="blue")

                if self.cetak_pesan is not None:
                    self.console.print(self.cetak_pesan)

    def tambah_saldo(self):


        teks2 = "[5].Kembali"



        titel = Table(title="Tambah Saldo",border_style="cyan")

        titel.add_column("No",style="cyan")
        titel.add_column("Saldo Classic",style="bold cyan")
        titel.add_column("Saldo Rare",style="bold cyan")
        for isi in range(len(self.saldo_c)):
            titel.add_row(f"{isi + 1}.",f"{self.saldo_c[isi]}",f"{self.saldo_r[isi]}",style="bold green")



        self.console.print(titel)

        panel3 = Panel(f"{teks2}",style="bold red")
        self.console.print(panel3)

        while True:
            try:
                pilih = int(Prompt.ask(f"[blue]{self.im[0]}:[/blue] "))

                if pilih in [1,2,3,4,6,7,8,9,10]:
                    self.pesan = "Anda Langsung pilih berapa saldo yang anda inginkan"
                    self.cetak_pesan = Text(f"Pesan: {self.pesan}", style="blue")

                    if self.cetak_pesan is not None:
                        self.console.print(self.cetak_pesan)
                elif pilih > 1000000 or pilih < 0:
                    self.pesan = "Maaf Saldo tersebut Belum Tersedia!!"
                    self.cetak_pesan = Text(f"Pesan: {self.pesan}", style="blue")

                    if self.cetak_pesan is not None:
                        self.console.print(self.cetak_pesan)
                elif pilih == 5:
                    return

                else:
                    self.saldo += pilih
                    pesan = "Penambahan Dompet Berhasil!!"
                    self.cetak_pesan = Text(f"Pesan: {pesan}", style="blue")
                    if self.cetak_pesan is not None:
                        self.console.print(self.cetak_pesan)
                    a = Prompt.ask(f"[blue]Apakah Anda Ingin Mengisi Lagi? (y/n):[/blue] ")
                    if a == "y":
                        continue
                    else:
                        tokoh_raffi.menu()
            except ValueError:
                self.pesan = "Sudah Berapa Kali saya Mengatakan!!"
                self.cetak_pesan = Text(f"Pesan: {self.pesan}", style="blue")

                if self.cetak_pesan is not None:
                    self.console.print(self.cetak_pesan)

    def shop(self):
        while True:

            titel3 = Table(title="Isi Tokoh",border_style="blue",style="bold cyan")

            titel3.add_column("No",style="cyan")
            titel3.add_column("KeyWord",style="cyan")

            for isi2 in range(len(self.isi_shop)):
                titel3.add_row(f"{isi2 + 1}",f"{self.isi_shop[isi2]}",style="green")


            self.console.print(titel3)
            panel3 = Panel("[9].Kembali", style="bold red")
            self.console.print(panel3)


            try:
                user = Prompt.ask(f"[blue]Pilih KeyWord:[/blue] ")

                if user == "9":
                    self.menu()
                    return

                else:
                    self.isishop(user.lower())

            except ValueError:
                self.pesan = "Maaf Anda tidak bisa memilih angka harus huruf!"
                self.cetak_pesan = Text(f"Pesan: {self.pesan}", style="blue")

                if self.cetak_pesan is not None:
                    self.console.print(self.cetak_pesan)


    def isishop(self,user):

        if user == "sepatu":
            titel5 = Table(title=f"{user}",border_style="blue",style="bold green")

            titel5.add_column("No",style="cyan")
            titel5.add_column(f"Jenis {user}",style="cyan")
            titel5.add_column("Harga",style="cyan")

            for isi7 in range(len(self.sepatu)):
                titel5.add_row(f"{isi7 + 1}",f"{self.sepatu[isi7]}",f"{self.sepatu_harga[isi7]}",style="green")

            self.console.print(titel5)

            kembali = Panel("[6].Kembali", style="bold red")
            self.console.print(kembali)

            while True:
                try:
                    choi = int(Prompt.ask("[blue]Pilih Nomor:[/blue] "))


                    if choi in [1,2,3,4,5]:
                        k = Prompt.ask("[bold green]Masukan Keranjang (y/n):[/bold green] ").lower()

                        if k == "y":
                            self.keranjang.append(self.sepatu[choi - 1])
                            self.harga_keranjang.append(self.sepatu_harga[choi - 1])
                            self.pesan = "Pesanan berhasil disimpan ke keranjang!"
                            self.cetak_pesan = Text(f"Pesan: {self.pesan}", style="blue")
                            if self.cetak_pesan is not None:
                                self.console.print(self.cetak_pesan)
                        elif k == "n":

                            if self.saldo < self.sepatu_harga[choi - 1]:
                                self.pesan = "Maaf Dompet Anda Tidak Cukup, Silahkan Isi Dulu!"
                                self.cetak_pesan = Text(f"Pesan: {self.pesan}", style="blue")
                                if self.cetak_pesan is not None:
                                    self.console.print(self.cetak_pesan)
                            else:
                                self.saldo -= self.sepatu_harga[choi - 1]
                                self.pesan = "Pembayaran Anda Berhasil!"
                                self.cetak_pesan = Text(f"Pesan: {self.pesan}", style="blue")
                                if self.cetak_pesan is not None:
                                    self.console.print(self.cetak_pesan)
                        else:
                            self.pesan = "Maaf Tidak ada pilihan bisa coba lagi"
                            self.cetak_pesan = Text(f"Pesan: {self.pesan}", style="blue")
                            if self.cetak_pesan is not None:
                                self.console.print(self.cetak_pesan)


                    elif choi == 6:
                        return

                    else:
                        self.pesan = "Segera Datang"
                        self.cetak_pesan = Text(f"Pesan: {self.pesan}", style="blue")
                        if self.cetak_pesan is not None:
                            self.console.print(self.cetak_pesan)
                        break

                except ValueError:
                    self.pesan = "Maaf Tidak bisa coba lagi"
                    self.cetak_pesan = Text(f"Pesan: {self.pesan}", style="blue")

                    if self.cetak_pesan is not None:
                        self.console.print(self.cetak_pesan)

        elif user == "baju":

            judul = Table(title=f"{user}",border_style="blue",style="bold green")

            judul.add_column("No",style="cyan")
            judul.add_column(f"Jenis {user}",style="cyan")
            judul.add_column(f"Harga {user}",style="cyan")

            for isi6 in range(len(self.baju)):
                judul.add_row(f"{isi6 + 1}",f"{self.baju[isi6]}",f"{self.baju_harga[isi6]}",style="green")

            self.console.print(judul)

            kembali2 = Panel("[6].Kembali", style="bold red")
            self.console.print(kembali2)

            while True:
                try:
                    choi2 = int(Prompt.ask("[blue]Pilih Nomor:[/blue] "))



                    if choi2 in [1, 2, 3, 4,5]:
                        k2 = Prompt.ask("[bold green]Masukan Keranjang (y/n):[/bold green] ").lower()

                        if k2 == "y":
                            self.keranjang.append(self.baju[choi2 - 1])
                            self.harga_keranjang.append(self.baju_harga[choi2 - 1])
                            self.pesan = "Pesanan berhasil disimpan ke keranjang!"
                            self.cetak_pesan = Text(f"Pesan: {self.pesan}", style="blue")
                            if self.cetak_pesan is not None:
                                self.console.print(self.cetak_pesan)
                        elif k2 == "n":

                            if self.saldo < self.baju_harga[choi2 - 1]:
                                self.pesan = "Maaf Dompet Anda Tidak Cukup, Silahkan Isi Dulu!"
                                self.cetak_pesan = Text(f"Pesan: {self.pesan}", style="blue")
                                if self.cetak_pesan is not None:
                                    self.console.print(self.cetak_pesan)
                            else:
                                self.saldo -= self.baju_harga[choi2 - 1]
                                self.pesan = "Pembayaran Anda Berhasil!"
                                self.cetak_pesan = Text(f"Pesan: {self.pesan}", style="blue")
                                if self.cetak_pesan is not None:
                                    self.console.print(self.cetak_pesan)
                        else:
                            self.pesan = "Maaf Tidak ada pilihan bisa coba lagi"
                            self.cetak_pesan = Text(f"Pesan: {self.pesan}", style="blue")
                            if self.cetak_pesan is not None:
                                self.console.print(self.cetak_pesan)

                    elif choi2 == 6:
                        return

                    else:
                        self.pesan = "Segera Datang"
                        self.cetak_pesan = Text(f"Pesan: {self.pesan}", style="blue")
                        if self.cetak_pesan is not None:
                            self.console.print(self.cetak_pesan)
                        break

                except ValueError:
                    self.pesan = "Maaf Tidak bisa coba lagi"
                    self.cetak_pesan = Text(f"Pesan: {self.pesan}", style="blue")

                    if self.cetak_pesan is not None:
                        self.console.print(self.cetak_pesan)

        elif user == "topi":
            titel6 = Table(title=f"{user}", border_style="blue", style="bold green")

            titel6.add_column("No", style="cyan")
            titel6.add_column(f"Jenis {user}", style="cyan")
            titel6.add_column("Harga", style="cyan")

            for isi8 in range(len(self.topi)):
                titel6.add_row(f"{isi8 + 1}", f"{self.topi[isi8]}", f"{self.topi_harga[isi8]}", style="green")

            self.console.print(titel6)

            kembali = Panel("[6].Kembali", style="bold red")
            self.console.print(kembali)

            while True:
                try:
                    choi3 = int(Prompt.ask("[blue]Pilih Nomor:[/blue] "))
                    if choi3 in [1, 2, 3, 4,5]:

                        k3 = Prompt.ask("[bold green]Masukan Keranjang (y/n)[/bold green] ").lower()

                        if k3 == "y":
                            self.keranjang.append(self.topi[choi3 - 1])
                            self.harga_keranjang.append(self.topi_harga[choi3 - 1])
                            self.pesan = "Pesanan berhasil disimpan ke keranjang!"
                            self.cetak_pesan = Text(f"Pesan: {self.pesan}", style="blue")
                            if self.cetak_pesan is not None:
                                self.console.print(self.cetak_pesan)
                        elif k3 == "n":
                            if self.saldo < self.topi_harga[choi3 - 1]:
                                self.pesan = "Maaf Dompet Anda Tidak Cukup, Silahkan Isi Dulu!"
                                self.cetak_pesan = Text(f"Pesan: {self.pesan}", style="blue")
                                if self.cetak_pesan is not None:
                                    self.console.print(self.cetak_pesan)

                            else:
                                self.saldo -= self.topi_harga[choi3 - 1]
                                self.pesan = "Pembayaran Anda Berhasil!"
                                self.cetak_pesan = Text(f"Pesan: {self.pesan}", style="blue")
                                if self.cetak_pesan is not None:
                                    self.console.print(self.cetak_pesan)
                        else:
                            self.pesan = "Maaf Tidak ada pilihan bisa coba lagi"
                            self.cetak_pesan = Text(f"Pesan: {self.pesan}", style="blue")
                            if self.cetak_pesan is not None:
                                self.console.print(self.cetak_pesan)



                    elif choi3 == 6:
                            return

                    else:
                        self.pesan = "Segera Datang"
                        self.cetak_pesan = Text(f"Pesan: {self.pesan}", style="blue")
                        if self.cetak_pesan is not None:
                            self.console.print(self.cetak_pesan)
                        break

                except ValueError:
                    self.pesan = "Maaf Tidak bisa coba lagi"
                    self.cetak_pesan = Text(f"Pesan: {self.pesan}", style="blue")

                    if self.cetak_pesan is not None:
                        self.console.print(self.cetak_pesan)


    def c_keranjang(self):

        while True:

            judul3 = Table(title="Keranjang Barang", border_style="blue", style="bold blue")


            judul3.add_column("No",style="bold green")
            judul3.add_column("Nama Barang",style="bold green")
            judul3.add_column("Harga",style="bold green")

            for isi9 in range(len(self.keranjang)):
                judul3.add_row(f"{isi9 + 1}",f"{self.keranjang[isi9]}", f"{self.harga_keranjang[isi9]}")

            self.console.print(judul3)


            for barang in range(len(self.keranjang)):
                self.isi_keranjang[self.keranjang[barang]] = self.harga_keranjang[barang]

            ahkir = len(self.keranjang)

            kembali = Panel(f"{ahkir + 1}.Kembali",style="bold red")
            self.console.print(kembali)

            i = Prompt.ask(f"[blue]Masukan Nama Barang:[/blue] ").capitalize()




            if i == str(ahkir + 1) or i.lower() == "kembali":
                self.menu()
                return


            if i in self.isi_keranjang:
                m = Prompt.ask("[bold blue]Bayar Nanti (y/n):[/bold blue] ").lower()

                if m == "y":
                    try:
                        masuk_tanggal = Prompt.ask("[bold red]Masukan Tanggal format (DD/MM/YY):[/bold red] ")
                        tanggal = datetime.datetime.strptime(masuk_tanggal, "%d/%m/%y")

                        self.pesan = f"Anda harus membayar pada tanggal: {tanggal.date()}"

                        self.cetak_pesan = Text(f"Pesan: {self.pesan}", style="blue")
                        if self.cetak_pesan is not None:
                            self.console.print(self.cetak_pesan)
                    except ValueError:
                        self.pesan = "Maaf format anda salah tolong ulangi"
                        self.cetak_pesan = Text(f"Pesan: {self.pesan}", style="blue")
                        if self.cetak_pesan is not None:
                            self.console.print(self.cetak_pesan)

                elif m == "n":
                    if self.saldo < self.isi_keranjang[i]:
                        self.pesan = "Maaf Dompet Anda Tidak Cukup, Silahkan Isi Dulu!"
                        self.cetak_pesan = Text(f"Pesan: {self.pesan}", style="blue")
                        if self.cetak_pesan is not None:
                            self.console.print(self.cetak_pesan)

                    else:
                        self.saldo -= self.isi_keranjang[i]
                        self.pesan = "Pembayaran Anda Berhasil!"
                        self.cetak_pesan = Text(f"Pesan: {self.pesan}", style="blue")
                        if self.cetak_pesan is not None:
                            self.console.print(self.cetak_pesan)

                        self.isi_keranjang.clear()


                else:
                    self.pesan = "Maaf tidak ada pilihan coba lagi"
                    self.cetak_pesan = Text(f"Pesan: {self.pesan}", style="blue")
                    if self.cetak_pesan is not None:
                        self.console.print(self.cetak_pesan)


tokoh_raffi = Tokoh()
tokoh_raffi.daftar()

