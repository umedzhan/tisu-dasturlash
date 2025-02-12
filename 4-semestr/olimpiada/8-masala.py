a = [1, 2, 3]
b = [2, 3, 4]
arr = []

for i in a:
	for j in b:
		if i == j:
			arr.append(i)

print(sorted(arr))
