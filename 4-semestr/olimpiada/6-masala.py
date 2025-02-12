fin = int(input())
f1 = 1
f2 = 1
n = 0

while True:
	n = f1 + f2
	f1 = f2
	f2 = n
	if n >= fin:
		break

if n == fin:
	print("Yes")
else:
	print("No")
