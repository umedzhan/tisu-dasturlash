# 1. Asosiy "Savdo" klassi
class Savdo:
    def __init__(self, mahsulot, narx, miqdor, mijoz, sana):
        self.__mahsulot = mahsulot  # inkapsulyatsiya (private)
        self.__narx = narx  # inkapsulyatsiya (private)
        self.__miqdor = miqdor  # inkapsulyatsiya (private)
        self.mijoz = mijoz
        self.sana = sana

    # get_info metodi - ma'lumotlarni chiroyli qilib ekranga chiqarish
    def get_info(self):
        print(f"Mahsulot: {self.__mahsulot}")
        print(f"Narx: {self.__narx} so'm")
        print(f"Miqdor: {self.__miqdor} ta")
        print(f"Mijoz: {self.mijoz}")
        print(f"Sana: {self.sana}")
        print("-" * 30)

    # umumiy savdo qiymatini hisoblash (polimorfizm)
    def savdo_qiymati(self):
        return self.__narx * self.__miqdor

    # Narxni yangilash
    def narxni_yangilash(self, yangi_narx):
        self.__narx = yangi_narx

    # Miqdorni yangilash
    def miqdorni_yangilash(self, yangi_miqdor):
        self.__miqdor = yangi_miqdor

    # Mijozni yangilash
    def mijozni_yangilash(self, yangi_mijoz):
        self.mijoz = yangi_mijoz

# 2. Savdo klassidan 5 ta obyekt yaratish
savdo1 = Savdo("Nokia telefon", 1500000, 10, "Ali", "2025-02-11")
savdo2 = Savdo("Samsung telefon", 2500000, 5, "Ona", "2025-02-11")
savdo3 = Savdo("iPhone telefon", 5000000, 2, "Vali", "2025-02-10")
savdo4 = Savdo("Xiaomi telefon", 1200000, 15, "Shahnoza", "2025-02-09")
savdo5 = Savdo("Huawei telefon", 2000000, 8, "Dilorom", "2025-02-08")

# Obyektlarning metodlariga murojaat qilish
savdo1.get_info()
savdo2.get_info()
savdo3.get_info()
savdo4.get_info()
savdo5.get_info()

# Polimorfizmni ko'rsatish
print(f"Savdo qiymati (savdo1): {savdo1.savdo_qiymati()} so'm")
print(f"Savdo qiymati (savdo2): {savdo2.savdo_qiymati()} so'm")

# 3. Savdo klassidan voris bo'lgan "ChegirmaSavdo" klassi
class ChegirmaSavdo(Savdo):
    def __init__(self, mahsulot, narx, miqdor, mijoz, sana, chegirma=0):
        super().__init__(mahsulot, narx, miqdor, mijoz, sana)  # asosiy klassni chaqirish
        self.chegirma = chegirma

    # Chegirmali savdo qiymatini hisoblash (polimorfizm)
    def savdo_qiymati(self):
        original_qiymat = super().savdo_qiymati()
        chegirma_qiymati = original_qiymat * (self.chegirma / 100)
        return original_qiymat - chegirma_qiymati

    # Chegirma qo'shish
    def chegirma_qoshish(self, chegirma):
        self.chegirma = chegirma

    # get_info metodini o'zgartirish (polimorfizm)
    def get_info(self):
        super().get_info()
        print(f"Chegirma: {self.chegirma}%")
        print("-" * 30)

# 4. ChegirmaSavdo klassidan 5 ta obyekt yaratish
savdo6 = ChegirmaSavdo("iPhone telefon", 5000000, 2, "Xurshid", "2025-02-11", 10)
savdo7 = ChegirmaSavdo("Xiaomi telefon", 1200000, 15, "Nodir", "2025-02-10", 15)
savdo8 = ChegirmaSavdo("Samsung telefon", 2500000, 5, "Zarina", "2025-02-09", 20)
savdo9 = ChegirmaSavdo("Huawei telefon", 2000000, 8, "Ravshan", "2025-02-08", 5)
savdo10 = ChegirmaSavdo("Nokia telefon", 1500000, 10, "Samar", "2025-02-07", 12)

# ChegirmaSavdo obyektlarining metodlariga murojaat qilish
savdo6.get_info()
savdo7.get_info()
savdo8.get_info()
savdo9.get_info()
savdo10.get_info()

# Polimorfizmni ko'rsatish
print(f"Chegirmali savdo qiymati (savdo6): {savdo6.savdo_qiymati()} so'm")
print(f"Chegirmali savdo qiymati (savdo7): {savdo7.savdo_qiymati()} so'm")
