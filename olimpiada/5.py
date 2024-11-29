def Polidrom(s):
    s = s.lower()
    l = len(s)

    if l < 2:
        return True
    elif s[0] == s[l - 1]:
        return Polidrom(s[1: l - 1])
    else:
        return False

s = input("S=")
ans = Polidrom(s)

if ans:
    print(True)

else:
    print(False)