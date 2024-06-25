from math import log2


def build_sparse_table(graph, n):
    log_n = int(log2(n)) + 1
    table = [[-1] * log_n for _ in range(n)]

    for i in range(n):
        table[i][0] = graph[i]

    j = 1
    while (1 << j) < n:
        for i in range(n):
            if table[i][j - 1] != -1:
                table[i][j] = table[table[i][j - 1]][j - 1]
        j += 1

    return table


def lca(u, v, depth, parent, sparse_table):
    if depth[u] < depth[v]:
        u, v = v, u

    log_n = len(sparse_table[0])

    for i in range(log_n - 1, -1, -1):
        if depth[u] - (1 << i) >= depth[v]:
            u = sparse_table[u][i]

    if u == v:
        return u

    for i in range(log_n - 1, -1, -1):
        if sparse_table[u][i] != sparse_table[v][i]:
            u = sparse_table[u][i]
            v = sparse_table[v][i]

    return parent[u]


def dfs(graph, u, depth, parent):
    for v in graph[u]:
        if v != parent[u]:
            parent[v] = u
            depth[v] = depth[u] + 1
            dfs(graph, v, depth, parent)


n = int(input())
parents = list(map(int, input().split()))
parent = [0] + parents

graph = [[] for _ in range(n)]
for i in range(1, n):
    graph[parent[i]].append(i)

root = 0
depth = [0] * n
parent[root] = -1
dfs(graph, root, depth, parent)

sparse_table = build_sparse_table(parent, n)

m = int(input())
for _ in range(m):
    u, v = map(int, input().split())
    print(lca(u, v, depth, parent, sparse_table))

