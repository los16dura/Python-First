start = input()
finish = input()
# вводим словарь
s = []
f = []
A = ['a','b','c','d','e','f','g','h']
b = [int(x) for x in range(1,9)]
#print(start[0])
for i in range(0,8):
    if start[0] == A[i]:
        s.append(i)
        s.append(int(start[1]))
    if finish[0] == A[i]:
        f.append(i)
        f.append(int(finish[1]))

s0 = int(s[0])
s1 = int(s[1]) - 1
f0 = int(f[0])
f1 = int(f[1]) - 1
print(s0,s1)

while s0 != f0 or s1 != f1:
    if abs(s0 - f0) < abs(s1 - f1):
        if f0 - s0 < 0:
            if s0 != 0:
                s0 -= 2
            else:
                s0 += 2
        else:
            if s0 != 7:
                s0+=2
            else:
                s0-=2
        if f1 - s1 < 0:
            if s1 != 0:
                s1 -= 1
            else:
                s1 += 1
        else:
            if s1 != 7:
                s1+=1
            else:
                s1-=1
        print(s0,s1)

    else:
        if f0 - s0 < 0:
            if s0 != 0:
                s0 -= 1
            else:
                s0 += 1
        else:
            if s0 != 7:
                s0+=1
            else:
                s0-=1
        if f1 - s1 < 0:
            if s1 != 0:
                s1 -= 2
            else:
                s1 += 2
        else:
            if s1 != 7:
                s1+=2
            else:
                s1-=2
        print(s0,s1)
print(f0,f1)
