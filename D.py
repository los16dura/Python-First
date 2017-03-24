__author__ = 'student'

N, M = [int(x) for x in input().split()]

def read(N, M):
    g = [[] for i in range(N)]
    for j in range(M):
        a, b = [int(x) for x in input(). split()]
        g[a].append(b)
    return g


def schet(g):
    k = []
    p = []
    if M % 2 == 0:
        for i in range(N):
            if len(g[i]) % 2 == 0:
                k.append(g[i])
        for i in range(len(k)):
            if k[i] != []:
                k[i] = i
                p.append(k[i])
        print(' '.join(map(str, p)))
    else:
        print('NO')

g = read(N, M)
schet(g)
