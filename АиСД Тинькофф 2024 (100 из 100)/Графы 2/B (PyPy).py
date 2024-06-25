import heapq

def prim(graph):
    n = len(graph)
    visited = [False] * n
    min_heap = [(0, 0)]  # (w, n)
    total_weight = 0

    while min_heap:
        weight, node = heapq.heappop(min_heap)
        if not visited[node]:
            visited[node] = True
            total_weight += weight
            for neighbor, neighbor_weight in graph[node]:
                if not visited[neighbor]:
                    heapq.heappush(min_heap, (neighbor_weight, neighbor))

    return total_weight

def main():
    n, m = map(int, input().split())
    graph = [[] for _ in range(n)]
    for _ in range(m):
        u, v, w = map(int, input().split())
        graph[u-1].append((v-1, w))
        graph[v-1].append((u-1, w))

    min_weight = prim(graph)
    print(min_weight)

if __name__ == "__main__":
    main()
