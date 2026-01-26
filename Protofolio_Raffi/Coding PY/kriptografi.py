from cryptography.exceptions import InvalidSignature
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import utils
from cryptography.hazmat.primitives import serialization



pesan = ["halo","saya","raffi"]

kunci = Fernet.generate_key()

fernet = Fernet(kunci)

data_AES = []

for e in range(len(pesan)):
    pesan_byte = pesan[e].encode()
    AES_key = fernet.encrypt(pesan_byte)

    data_AES.append(AES_key)


private_kunci = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048,
)

publik_kunci = private_kunci.public_key()


data_enkripsi = []

for a in range(len(data_AES)):
    t = publik_kunci.encrypt(
        data_AES[a],
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None,
        )

    )

    data_enkripsi.append(t)

add_hash = hashes.SHA256()

view_hash = hashes.Hash(add_hash)

for g in range(len(data_enkripsi)):
    view_hash.update(data_enkripsi[g])

digest = view_hash.finalize()

tanda_tangan = private_kunci.sign(
    digest,
    padding.PSS(
        mgf=padding.MGF1(add_hash),
        salt_length=padding.PSS.MAX_LENGTH,
    ),
    utils.Prehashed(add_hash)

)


notif = ""

try:
    publik_kunci.verify(
        tanda_tangan,
        digest,
        padding.PSS(
            mgf=padding.MGF1(add_hash),
            salt_length=padding.PSS.MAX_LENGTH,
        ),
        utils.Prehashed(add_hash)
    )
    notif += "cocok"
    print(notif)
except InvalidSignature:
    print("Tidak cocok")
    notif += "tidak cocok"
    print(notif)

data_dekripsi = []

data_private = []
data_publik = []

database = {}

if notif == "cocok":
    for k in range(len(data_enkripsi)):
        rs = private_kunci.decrypt(
            data_enkripsi[k],
            padding.OAEP(
                mgf=padding.MGF1(algorithm=add_hash),
                algorithm=add_hash,
                label=None,
            )

        )
        data_dekripsi.append(rs)

    for enk in range(len(data_enkripsi)):

        serial = private_kunci.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.PKCS8,
            encryption_algorithm=serialization.BestAvailableEncryption(data_enkripsi[enk]),
        )

        data_private.append(serial)

    for enk2 in range(len(data_enkripsi)):
        serial2 = publik_kunci.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo,

        )
        data_publik.append(serial2)

    judul1 = "Serial Private Key"
    judul2 = "Serial Public Key"
    for comp in range(len(data_private)):
        database[judul1] = data_private[comp]

    for comp2 in range(len(data_publik)):
        database[judul2] = data_publik[comp2]

    dekripsi_pesan1 = fernet.decrypt(data_dekripsi[0])
    dekripsi_pesan2 = fernet.decrypt(data_dekripsi[1])
    dekripsi_pesan3 = fernet.decrypt(data_dekripsi[2])

    print("Data Enkripsi AES: ",data_AES[0])
    print("Data Enkripsi AES: ",data_AES[1])
    print("Data Enkripsi AES: ",data_AES[2])
    print("Serial Private Key: ",database[judul1])
    print("Serial Public Key: ",database[judul2])
    print("Dekripsi Pesan: ",dekripsi_pesan1)
    print("Dekripsi Pesan: ",dekripsi_pesan2)
    print("Dekripsi Pesan: ",dekripsi_pesan3)
    print("Data Enkripsi RSA: ",data_enkripsi[0])
    print("Data Enkripsi RSA: ",data_enkripsi[1])
    print("Data Enkripsi RSA: ",data_enkripsi[2])

else:
    print("Bacot")


