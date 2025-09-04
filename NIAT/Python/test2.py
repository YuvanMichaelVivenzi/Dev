a = int(input())
a = str(a)
b = a[0]
c = a[1]
d = a[2]
e = a[3]
f = (str(b) + str(c))
g = (str(d) + str(e))
if (int(f) == 19) and (int(g) > 30 and int(g) < 60):
    print(True)
else:
    print(False) 