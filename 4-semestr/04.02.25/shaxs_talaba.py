class Shaxs:
	odamlar_soni = 0
	def __init__(self, ism, familiya):
		self.ism = ism
		self.familiya = familiya
		Shaxs.odamlar_soni += 1

class Talaba(Shaxs):
	__talabalar_soni = 0
	def __init__(self, ism, familiya, baho = 2):
		super().__init__(ism, familiya)
		self.__baho = baho
		Talaba.__talabalar_soni += 1

	def bahosi(self):
		return self.__baho
	def yangi(self, baho):
		self.__baho = baho

	@classmethod
	def soni(cls):
		return cls.__talabalar_soni

talaba1 = Talaba("Anvar", "Ashurov", 3)
print(talaba1.bahosi())
talaba1.yangi(5)
print(talaba1.bahosi())
print(talaba1.odamlar_soni)
talaba2 = Talaba("Anvar", "Ashurov", 3)
