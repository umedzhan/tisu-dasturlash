# 1. Asosiy "Restoran" klassi
class Restoran:
    def __init__(self, nomi, joylashuv, menyu, xizmatlar, yildan_tashkil_etilgan):
        self.__nomi = nomi  # inkapsulyatsiya (private)
        self.__joylashuv = joylashuv  # inkapsulyatsiya (private)
        self.menyu = menyu
        self.xizmatlar = xizmatlar
        self.__yildan_tashkil_etilgan = yildan_tashkil_etilgan  # inkapsulyatsiya (private)

    # get_info metodi - ma'lumotlarni chiroyli qilib ekranga chiqarish
    def get_info(self):
        print(f"Restoran Nomi: {self.__nomi}")
        print(f"Joylashuv: {self.__joylashuv}")
        print(f"Menyu: {', '.join(self.menyu)}")
        print(f"Xizmatlar: {', '.join(self.xizmatlar)}")
        print(f"Tashkil etilgan yil: {self.__yildan_tashkil_etilgan}")
        print("-" * 30)

    # Restoran yilini olish
    def yili(self):
        return 2025 - self.__yildan_tashkil_etilgan

    # Menyuni yangilash
    def menyuni_yangilash(self, yangi_menyu):
        self.menyu = yangi_menyu

    # Xizmatlarni yangilash
    def xizmatlarni_yangilash(self, yangi_xizmatlar):
        self.xizmatlar = yangi_xizmatlar

    # Restoran nomini yangilash
    def nomini_yangilash(self, yangi_nomi):
        self.__nomi = yangi_nomi

# 2. Restoran klassidan 5 ta obyekt yaratish
restoran1 = Restoran("Shirin Taomlar", "Toshkent, Amir Temur ko'chasi", ["Pilaf", "Shashlik", "Manti"], ["Ochilish soatlari", "Wi-Fi", "Taksilar"], 2000)
restoran2 = Restoran("Oshxona", "Buxoro, Bog'ishamol", ["Shurva", "Somsa", "Beshbarmoq"], ["Pishirish darslari", "Ochilish soatlari", "Kafedravi"], 2005)
restoran3 = Restoran("Zavod Taomlari", "Samarqand, Qo'qon ko'chasi", ["Kebab", "Shurva", "Laghmon"], ["Wi-Fi", "Taksilar", "Balkon"], 2010)
restoran4 = Restoran("Toshkent Taomlari", "Toshkent, Yunusobod", ["Palov", "Somsa", "Shashlik"], ["Pishirish darslari", "Ochilish soatlari", "Taksilar"], 2015)
restoran5 = Restoran("Ziyorat Taomlari", "Qarshi, Saryog'och", ["Shashlik", "Kebab", "Chuchvara"], ["Wi-Fi", "Kofe", "Ochilish soatlari"], 2012)

# Obyektlarning metodlariga murojaat qilish
restoran1.get_info()
restoran2.get_info()
restoran3.get_info()
restoran4.get_info()
restoran5.get_info()

# Polimorfizmni ko'rsatish
print(f"Restoran1 tashkil etilganiga {restoran1.yili()} yil bo'ldi.")
print(f"Restoran2 tashkil etilganiga {restoran2.yili()} yil bo'ldi.")

# 3. Restoran klassidan voris bo'lgan "RestoranVIP" klassi
class RestoranVIP(Restoran):
    def __init__(self, nomi, joylashuv, menyu, xizmatlar, yildan_tashkil_etilgan, maxsus_xizmat):
        super().__init__(nomi, joylashuv, menyu, xizmatlar, yildan_tashkil_etilgan)  # asosiy klassni chaqirish
        self.maxsus_xizmat = maxsus_xizmat

    # VIP xizmatlarini qo'shish
    def maxsus_xizmatni_qoshish(self, xizmat):
        self.maxsus_xizmat.append(xizmat)

    # RestoranVIP klassi uchun get_info metodini o'zgartirish (polimorfizm)
    def get_info(self):
        super().get_info()
        print(f"Maxsus xizmatlar: {', '.join(self.maxsus_xizmat)}")
        print("-" * 30)

    # VIP xizmatlarini yangilash
    def maxsus_xizmatlarni_yangilash(self, yangi_maxsus_xizmat):
        self.maxsus_xizmat = yangi_maxsus_xizmat

# 4. RestoranVIP klassidan 5 ta obyekt yaratish
restoranVIP1 = RestoranVIP("Zavod VIP Taomlari", "Toshkent, Temur Malik", ["Lazzatli Shashlik", "Lobster", "Stek"], ["Kuydirish", "Lounge", "Wi-Fi"], 2018, ["Xususiy xizmat", "Tez ovqatlanish"])
restoranVIP2 = RestoranVIP("Kuzatuv Taomlari", "Buxoro, Shahrisabz ko'chasi", ["Barbekyu", "Qovurilgan somsa"], ["Wi-Fi", "VIP joylar", "Kofe bar"], 2020, ["Maxfiylik", "Kuydirish", "Lounge"])
restoranVIP3 = RestoranVIP("Jazira Taomlari", "Samarqand, Ulughbek", ["Tandoor", "Somsa", "Kebab"], ["Kofe", "Wi-Fi", "Balkon"], 2017, ["Kuzatish kamerasi", "Kuydirish", "Maxsus menyu"])
restoranVIP4 = RestoranVIP("Baliq Taomlari", "Navoiy, Sirdaryo ko'chasi", ["Baliq", "Lobster", "Krevetka"], ["Kofe", "Kuydirish", "Wi-Fi"], 2019, ["Kuchli Wi-Fi", "Balkon", "Maxfiylik"])
restoranVIP5 = RestoranVIP("Karmona Taomlari", "Farg'ona, G'azalkent", ["Keksa somsa", "Shorva", "Manti"], ["Wi-Fi", "Taksilar", "Kuydirish"], 2016, ["Maxsus xizmat", "Kuydirish", "Jangovar xizmat"])

# RestoranVIP obyektlarining metodlariga murojaat qilish
restoranVIP1.get_info()
restoranVIP2.get_info()
restoranVIP3.get_info()
restoranVIP4.get_info()
restoranVIP5.get_info()

# Polimorfizmni ko'rsatish
print(f"VIP restoran1 tashkil etilganiga {restoranVIP1.yili()} yil bo'ldi.")
print(f"VIP restoran2 tashkil etilganiga {restoranVIP2.yili()} yil bo'ldi.")
