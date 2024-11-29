x1 = int(input("x1="))
y1 = int(input("y1="))
x2 = int(input("x2="))
y2 = int(input("y2="))

if (y2 == y1+2) and (x2 == x1-1 or x2 == x1+1):
	result = True
elif (y2 == y1-2) and (x2 == x1-1 or x2 == x1+1):
	result = True
elif (x2 == x1 + 2) and (y2 == y1+1 or y2 == y1-1):
	result = True
elif (x2 == x1 - 2) and (y2 == y1+1 or y2 == y1-1):
	result = True
else:
	result = False

if (y2 == y1):
	farzin = True
elif (x2 == x1):
	farzin = True
elif (x1-y1 == x2-y2):
	farzin = True
else:
	farzin = False

print(result)
print(farzin)