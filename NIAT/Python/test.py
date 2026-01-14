a = input()
b = a[-1]
c = int(a[:-1])
if b == "T":
    print(c * 10)
elif b == "H":
    print(c * 100)
elif b == "K":
    print(c * 1000)