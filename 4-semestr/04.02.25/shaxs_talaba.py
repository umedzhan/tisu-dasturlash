class Shaxs:
	def __init__(self, ism, familiya):
		self.ism = ism
		self.familiya = familiya

class Talaba(Shaxs):
	def __init__(self, ism, familiya, baho = 2):
		super().__init__(ism, familiya)
		self.__baho = baho

	def bahosi(self):
		return self.__baho
	def yangi(self, baho):
		self.__baho = baho

talaba1 = Talaba("Anvar", "Ashurov")
print(talaba1.bahosi())
talaba1.yangi(5)
print(talaba1.bahosi())
