N,M = [int(x) for x in input().split()]
edges = []
for i in range(M):
    v1,v2= list(map(int,input().split()))
    edges.append((v1,v2))
comp = list(range(N))
tree = []
tree_weight = 0
for v1,v2 in edges:
    if comp[v1]!=comp[v2]:
        tree.append((v1,v2))
        tree_weight += 1
        a = comp[v1]
        b = comp[v2]
        for i in range(N):
            if comp[i] == b:
                comp[i] = a
print(tree_weight)
