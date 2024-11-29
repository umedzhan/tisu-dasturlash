M = int(input("M="))
x = []
xy = []

for i in range(M):
    for i in range(M):
        x.append(input())
    xy.append(x)
    x = []
mat = xy
 
def rotate_matrix(a):
    b = []
    i = len(a)-1
    while i>=0:
        if len(a) == len(a[-1]):
            for j in range(0, len(a)):
                print(j)
                if (len(b) < (j+1)):
                    b.append([a[i][j]])
                    
                else:
                    b[j].append(a[i][j])
                    
            i -= 1
        else:
            for j in range(0, len(a)+1):
                print(j)
                if (len(b) < (j+1)):
                    b.append([a[i][j]])
                    
                else:
                    b[j].append(a[i][j])
                    
            i -= 1
    return b
    
print(rotate_matrix(mat))