import sys
import  time


lirik = [
    "halo,nama saya raffi",
    "saya kelas XI RPL",
    "alamat saya adalah tukum",
    "jancok"
]

waktu = [
    0.1,
    0.02,
    0.3,
    0.05
]

for sem in range(len(lirik)):
    for liryc in lirik[sem]:
        sys.stdout.write(liryc)
        sys.stdout.flush()
        time.sleep(waktu[sem])
        print(end="")
    print()