def factoriall(a):
	if a == 0 or a == 1:
		return 1
	else:
		javob = a * factoriall(a - 1)
		return javob
a = int(input('1 son:'))
print(factoriall(a))
b = int(input('2 son:'))
print(factoriall(b))
c = int(input('3 son:'))
print(factoriall(c))

stop = input()