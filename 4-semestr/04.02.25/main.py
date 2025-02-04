from uuid import uuid4
class Avto:
	__num_avto = 0
	def __init__(self, make, model, rang, yil, narx, km = 0):
		self.make = make
		self.model = model
		self.rang = rang
		self.yil = yil
		self.narx = narx
		self.__km = km
		self.__id = uuid4()
		Avto.__num_avto += 1
	@classmethod
	def get_num_avto(cls):
		return cls.__num_avto
	def get_km(self):
		return self.__km
	def get_id(self):
		return self.__id
	def add_km(self, km):
		if km >= 0:
			self.__km += km
		else:
			return "Mashina km kamaytirib bo'lmaydi"
avto1 = Avto("GM", "Malibu", "Qora", 2025, 40000, 100000)
avto2 = Avto("GM", "Lacetti", "Oq", 2025, 20000)
print(f"ID: {avto1.get_id()}")
avto1.add_km(1500)
print(avto1.get_km())
print(avto1.get_num_avto())
avto3 = Avto("Tayota", "Carmy", "Silver", 2023, 45000)
print(avto1.get_num_avto())