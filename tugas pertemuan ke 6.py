# inheritance_lab.py

# Parent Class
class Kendaraan:
    def __init__(self):
        print("Kendaraan dibuat")

    def info(self):
        print("Ini adalah kendaraan")


# Child Class pertama
class Mobil(Kendaraan):
    def __init__(self):
        super().__init__()
        print("Mobil dibuat")

    def jalan(self):
        print("Mobil sedang berjalan")


# Child Class kedua
class Motor(Kendaraan):
    def __init__(self):
        super().__init__()
        print("Motor dibuat")

    def klakson(self):
        print("Motor membunyikan klakson")


# Multiple Inheritance (Diamond Problem)
class KendaraanListrik(Mobil, Motor):
    def __init__(self):
        super().__init__()
        print("Kendaraan listrik dibuat")

    def baterai(self):
        print("Menggunakan baterai listrik")


# Program utama
print("=== Program Inheritance & Diamond Problem ===")

# Membuat objek
tesla = KendaraanListrik()

print("\n=== Menjalankan Method ===")
tesla.info()
tesla.jalan()
tesla.klakson()
tesla.baterai()

print("\n=== Method Resolution Order (MRO) ===")
print(KendaraanListrik.__mro__)