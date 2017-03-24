__author__ = 'student'

n = input()
m = input()
a = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
b = [int(x) for x in range(1, 9)]

c = n[0]
d = int(n[1])
cd = c+str(d)
print(cd)

while cd != m:
    c = a[a.index(c)+1]
    if d + 2 <= 8:
        d = b[b.index(d)+2]
    elif d + 2 > 8:
        d = b[b.index(d)-2]
    cd = c+str(d)
    print(cd)
