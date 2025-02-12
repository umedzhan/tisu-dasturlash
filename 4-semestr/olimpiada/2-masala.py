fin = int(input())

if (fin > 0):
	print(str(fin)[::-1])
elif (fin < 0):
	print("-"+str(abs(fin))[::-1])