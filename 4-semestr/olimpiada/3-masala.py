fin = input()
a = []
for i in fin:
	a.append(i)

if len(set(a)) == len(a):
	print("Yes")
else:
	print("No")

