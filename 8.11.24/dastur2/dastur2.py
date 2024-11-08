# array 78
a = [1,2,3,4,5]
b = []
for i in range(len(a)-1):
	b.append((a[i]+(a[i]+1)) / 2)
	print(a[i] + (a[i]+1))

with open('natija.txt', 'w') as natija:
	natija.write(', '.join(map(str, b)))