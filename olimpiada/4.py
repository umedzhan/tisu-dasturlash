def circular_subtraction(i):
    new_i = i 
    if(i==0):
        new_i = 2
    elif(i==1):
        new_i = 1
    elif(i==2):
        new_i = 0
    return new_i


def rotate_clock(matrix):
    new_matrix = matrix


M = int(input("M="))
x = []
xy = []

for i in range(M):
	for i in range(M):
		x.append(input())
	xy.append(x)
	x = []


matrix = xy
rotate_clock(matrix)

for i in range(len(matrix)):
    for j in range(len(matrix)):
        new_i = circular_subtraction(i)
        new_matrix[j][new_i] = matrix[i][j]
        print("New element added from {},{} to {},{} ::: {} to {}".format(i+1,j+1,j+1,new_i+1,matrix[i][j],new_matrix[j][new_i]))

for each_row in new_matrix:
    print(each_row)


print("Length of the matrix : ",len(matrix))
for each_row in matrix:
    print(each_row)
print()
