a = int(input())
b = int(input())
s = 0
arr = []


for i in range(a+1, b):
	for j in range(b, 0, -1):
		if i % j == 0:
			s += 1
	if s <= 2:
		arr.append(i)
	s = 0
print(arr)
