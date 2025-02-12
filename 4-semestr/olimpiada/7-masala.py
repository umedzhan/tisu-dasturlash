a = [1, 2, 3, 4]
surish = 2
arr = []

for i in a:
	arr.insert(surish, i)
	surish+=1
	if surish >= len(a):
		surish = 0

print(arr)
