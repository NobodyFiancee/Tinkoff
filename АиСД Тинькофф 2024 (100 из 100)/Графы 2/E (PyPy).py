import heapq

def dijkstra(graph, start):
    n = len(graph)
    distances = [float('inf')] * n
    distances[start] = 0
    heap = [(0, start)]

    while heap:
        dist, node = heapq.heappop(heap)
        if dist > distances[node]:
            continue
        for neighbor, weight in graph[node]:
            new_dist = dist + weight
            if new_dist < distances[neighbor]:
                distances[neighbor] = new_dist
                heapq.heappush(heap, (new_dist, neighbor))
    return distances

def main():
    n, m = map(int, input().split())
    graph = [[] for _ in range(n)]
    for _ in range(m):
        start, end, weight = map(int, input().split())
        graph[start - 1].append((end - 1, weight))
        graph[end - 1].append((start - 1, weight))

    start_node = 0
    distances = dijkstra(graph, start_node)
    print(*distances)

if __name__ == "__main__":
    main()
