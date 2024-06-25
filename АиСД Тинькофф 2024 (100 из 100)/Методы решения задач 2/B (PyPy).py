from collections import defaultdict

def dfs(node, parent, cost, graph, min_cost, depth):
    min_cost[node][0] = parent
    min_cost[node][1] = cost
    depth[node] = depth[parent] + 1

    for child, edge_cost in graph[node]:
        if child != parent:
            dfs(child, node, edge_cost, graph, min_cost, depth)

def preprocess_tree(n, edges):
    graph = defaultdict(list)
    min_cost = [[-1, float('inf')] for _ in range(n)]
    depth = [-1] * n

    for i, (parent, cost) in enumerate(edges):
        graph[parent].append((i + 1, cost))

    dfs(0, 0, 0, graph, min_cost, depth)

    return graph, min_cost, depth

def find_min_cost_path(x, y, min_cost, depth):
    if depth[x] < depth[y]:
        x, y = y, x

    min_cost_edge = float('inf')

    while depth[x] != depth[y]:
        min_cost_edge = min(min_cost_edge, min_cost[x][1])
        x = min_cost[x][0]

    while x != y:
        min_cost_edge = min(min_cost_edge, min(min_cost[x][1], min_cost[y][1]))
        x = min_cost[x][0]
        y = min_cost[y][0]

    return min_cost_edge


n = int(input())
edges = [tuple(map(int, input().split())) for _ in range(n - 1)]
m = int(input())
queries = [tuple(map(int, input().split())) for _ in range(m)]

graph, min_cost, depth = preprocess_tree(n, edges)

for query in queries:
    x, y = query
    min_cost_path = find_min_cost_path(x, y, min_cost, depth)
    print(min_cost_path)
