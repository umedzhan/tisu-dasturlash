A = int(input('A='))
B = int(input('B='))
C = int(input('C='))

n = (A>0 and B<0 and C<0) or (A<0 and B>0 and C<0) or (A<0 and B<0 and C>0)

print(n)
stop = input()
