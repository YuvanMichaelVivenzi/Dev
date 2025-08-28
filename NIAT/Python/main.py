a = int(input())
b = int(input())
c = a ** b
d = b ** a
if c > d:
    print("a to the power of b is greater")
    print(c)
else:
    print("b to the power of a is greater")
    print(d)