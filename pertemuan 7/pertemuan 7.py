```python
# Parent Class
class AlatPembayaran:
    def proses_bayar(self):
        print("Memproses pembayaran...")


# Child Class 1
class KartuKredit(AlatPembayaran):
    def proses_bayar(self):
        print("Pembayaran menggunakan Kartu Kredit berhasil.")


# Child Class 2
class EWallet(AlatPembayaran):
    def proses_bayar(self):
        print("Pembayaran menggunakan E-Wallet berhasil.")


# Child Class 3 (opsional tambahan)
class TransferBank(AlatPembayaran):
    def proses_bayar(self):
        print("Pembayaran menggunakan Transfer Bank berhasil.")


# Fungsi Duck Typing
def jalankan_transaksi(objek):
    objek.proses_bayar()


# Membuat objek
kartu = KartuKredit()
ewallet = EWallet()
transfer = TransferBank()


# Menjalankan transaksi
jalankan_transaksi(kartu)
jalankan_transaksi(ewallet)
jalankan_transaksi(transfer)
```
