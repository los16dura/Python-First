__author__ = 'student'

a = list(map(int, input().split()))
n = a[0]
m = a[1]
a = a[2:]

def reading(n, m):
    g = [[] for i in range(n)]
    for j in range(m):
        d, b, c = [int(x) for x in input().split()]
        g[d][b] = c
    return g

def dij(g, start):
    used = set()
    d = [float('+INF') for v in g]
    while len(used) != len(g):
        min_d = float('+inf')
        for i in d:
            if d[i] < min_d and i not in used:
                cur = i
                min_d = d[i]
                used.add(cur)
        for n in g[cur]:
            L = d[cur] + g[cur][n]
            if L < d[n]:
                d[n] = L
        used.add(n)
    return(d)

g = reading(n,m)
for k in range(len(g)):
    dij(g, k)
