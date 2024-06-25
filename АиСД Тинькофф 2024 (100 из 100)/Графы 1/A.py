import sys
from collections import defaultdict


def dfs(graph, node, visited):
    visited[node] = True
    component = [node]
    for neighbour in graph[node]:
        if not visited[neighbour]:
            component += dfs(graph, neighbour, visited)
    return component


def connected_components(graph, n):
    visited = defaultdict(bool)
    components = []
    for i in range(1, n + 1):
        if not visited[i]:
            component = dfs(graph, i, visited)
            components.append(sorted(component))
    return components


sys.setrecursionlimit(10**7)
n, m = map(int, input().split())
graph = defaultdict(list)
for _ in range(m):
    i, j = map(int, input().split())
    graph[i].append(j)
    graph[j].append(i)

components = connected_components(graph, n)
print(len(components))
for component in components:
    print(len(component))
    print(*component)