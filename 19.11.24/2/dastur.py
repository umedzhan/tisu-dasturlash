S1 = input('S1: ')
S2 = input('S2: ')
if S2 in S1:
    index = S1.rfind(S2)
    S1 = S1[:index] + S1[index + len(S2):]
print(S1)

stop = input()