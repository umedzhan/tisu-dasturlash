class Users:
	def __init__(self, ism, username, mail):
		self.ism = ism
		self.username = username
		self.mail = mail

	def get_userinfo(self):
		return f"Ism: {self.ism}, Foydalanuvchi nomi: {self.username}, Pochta manzili: {self.mail}"

var = Users("Oral", "Oral1", "oral@gmail.com")
print(var.get_userinfo())
