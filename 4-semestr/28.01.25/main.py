class Talaba:
	def __init__(self, ism, familiya, tyil):
		self.ism = ism
		self.familiya = familiya
		self.tyil = tyil
	def tanishtir(self):
		return f"Ismim {self.ism} {self.familiya}. {self.tyil} yilda tug'ilganman"

	def get_age(self, yil):
		return yil - self.tyil

var = Talaba("Alijon", "Valiyev", 2000)
print(var.tanishtir())
print(f"Men {var.get_age(2025)} yoshdaman.")