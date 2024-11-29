N = int(input("N="))
x = []
y = []
xy = []
for i in range(1,N+1):
	x.append(int(input(f"xy{i}=")))
	y.append(int(input(f"x{i}=")))
	xy.append(x+y)
	x = []
	y = []
print(sorted(xy,reverse=True))