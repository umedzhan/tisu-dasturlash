# array 64
a = [1,2,3,4,5]
b = [4,3,5,2,1]
c = [8,7,4,6,3]

n = sorted(a + b + c)
with open('natija.txt', 'w') as natija:
	natija.write(', '.join(map(str, n)))