import sys
from collections import defaultdict


def dfs(v, visited, recursion_stack, graph):
    visited[v] = True
    recursion_stack[v] = True

    for neighbour in graph[v]:
        if not visited[neighbour]:
            if dfs(neighbour, visited, recursion_stack, graph):
                return True
        elif recursion_stack[neighbour]:
            return True

    recursion_stack[v] = False
    return False


def is_cyclic(n, graph):
    visited = defaultdict(bool)
    recursion_stack = defaultdict(bool)

    for i in range(1, n+1):
        if not visited[i]:
            if dfs(i, visited, recursion_stack, graph):
                return True
    return False


sys.setrecursionlimit(10**7)
n, m = map(int, input().split())
graph = defaultdict(list)
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)

print(1 if is_cyclic(n, graph) else 0)