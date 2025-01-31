a = int(input('a='))
b = int(input('b='))
c = int(input('c='))
if a<b and a<c:
    kichigi = a
elif b<a and b<c:
    kichigi = b
else:
    kichigi = c
    
if a>b and a>c:
    kattasi = a
elif b>a and b>c:
    kattasi = b
else:
    kattasi = c
    
print(kichigi)
print(kattasi)

stop = input()