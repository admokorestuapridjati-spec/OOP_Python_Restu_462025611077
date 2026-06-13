# Pertemuan 8 - Exception Handling Lab
# Skenario: Sistem Transaksi Bank (Penarikan Saldo)


class SaldoMinimalError(Exception):
    """Custom Exception: dipicu jika penarikan menyebabkan saldo
    di bawah batas minimal yang ditentukan."""

    def __init__(self, saldo, jumlah_tarik, minimal):
        self.saldo = saldo
        self.jumlah_tarik = jumlah_tarik
        self.minimal = minimal
        message = (
            f"Penarikan Rp{jumlah_tarik:,.2f} ditolak! "
            f"Saldo akan menjadi Rp{saldo - jumlah_tarik:,.2f}, "
            f"di bawah saldo minimal Rp{minimal:,.2f}."
        )
        super().__init__(message)


class JumlahTidakValidError(Exception):
    """Custom Exception: dipicu jika jumlah penarikan tidak valid
    (nol atau negatif)."""

    def __init__(self, jumlah):
        self.jumlah = jumlah
        message = f"Jumlah penarikan tidak valid: Rp{jumlah:,.2f}. Harus lebih dari 0."
        super().__init__(message)


class RekeningBank:
    """Class Utama untuk mengelola transaksi rekening bank."""

    SALDO_MINIMAL = 50000.0

    def __init__(self, nama_pemilik, saldo_awal):
        self.nama_pemilik = nama_pemilik
        self.saldo = saldo_awal

    def tarik_tunai(self, jumlah):
        """Melakukan validasi dan proses penarikan tunai."""
        if jumlah <= 0:
            raise JumlahTidakValidError(jumlah)

        sisa_saldo = self.saldo - jumlah

        if sisa_saldo < self.SALDO_MINIMAL:
            raise SaldoMinimalError(self.saldo, jumlah, self.SALDO_MINIMAL)

        self.saldo = sisa_saldo
        print(f"Penarikan berhasil! Sisa saldo: Rp{self.saldo:,.2f}")
        return self.saldo


def proses_transaksi(rekening, jumlah_penarikan):
    """Membungkus pemanggilan metode tarik_tunai dengan try-except-finally."""
    print(f"\n--- Mencoba menarik Rp{jumlah_penarikan:,.2f} ---")
    try:
        rekening.tarik_tunai(jumlah_penarikan)
    except SaldoMinimalError as e:
        print(f"[SaldoMinimalError] {e}")
    except JumlahTidakValidError as e:
        print(f"[JumlahTidakValidError] {e}")
    except Exception as e:
        print(f"[Error Tak Terduga] {e}")
    finally:
        print("Proses pemeriksaan transaksi telah selesai dilakukan.")


if __name__ == "__main__":
    rekening = RekeningBank("Budi Santoso", 200000.0)

    print(f"Pemilik: {rekening.nama_pemilik}")
    print(f"Saldo awal: Rp{rekening.saldo:,.2f}")

    # Skenario 1: Penarikan normal (berhasil)
    proses_transaksi(rekening, 50000.0)

    # Skenario 2: Penarikan melebihi batas saldo minimal (gagal)
    proses_transaksi(rekening, 150000.0)

    # Skenario 3: Penarikan dengan jumlah tidak valid (gagal)
    proses_transaksi(rekening, -1000.0)

    print(f"\nSaldo akhir: Rp{rekening.saldo:,.2f}")