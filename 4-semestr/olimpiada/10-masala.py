fin = input()
x = fin.split()
a = []

while True:
	a.append(int(x[-1]) - int(x[-2]))
	x.pop()
	if len(x) <2:
		break

if len(set(a)) == 1:
	print("Yes")
else:
	print("No")
