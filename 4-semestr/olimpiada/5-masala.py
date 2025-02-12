fin = input()
x = fin.split()
toq = 0
juft = 0

for i in x:
	if int(i) % 2 == 0:
		juft += 1
	else:
		toq += 1

print("Toq:",toq)
print("Juft:",juft)
