from collections import defaultdict


def is_topological_sort(permutation, graph, n):
    position = {v: i for i, v in enumerate(permutation)}

    for u in range(1, n + 1):
        for v in graph[u]:
            if position[u] > position[v]:
                return "NO"
    return "YES"


n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]
permutation = list(map(int, input().split()))

graph = defaultdict(list)
for u, v in edges:
    graph[u].append(v)

print(is_topological_sort(permutation, graph, n))