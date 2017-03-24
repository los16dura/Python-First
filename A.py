__author__ = 'student'

N = int(input())
g = [[]*N for i in range(N)]
for j in range(N):
    a = list(map(int, input().split()))
    for k in range(N):
        if a[k] != 0:
            g[j].append(k)

b = input()
b = 0

C = list(map(int, input().split()))
for i in range(N):
    for j in g[i]:
        if C[i] != C[j]:
            b +=1

print(b//2)
