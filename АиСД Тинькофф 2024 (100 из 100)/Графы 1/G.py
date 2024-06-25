def floyd_warshall(N, roads):
    dist = [[float('inf')] * (N + 1) for _ in range(N + 1)]

    # Заполнение расстояний для прямых путей
    for i in range(1, N + 1):
        dist[i][i] = 0

    for u, v, w in roads:
        dist[u][v] = w
        dist[v][u] = w

    # Алгоритм Флойда-Уоршелла
    for k in range(1, N + 1):
        for i in range(1, N + 1):
            for j in range(1, N + 1):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

    return dist

def find_optimal_city(N, dist):
    min_total_distance = float('inf')
    optimal_city = -1

    for i in range(1, N + 1):
        total_distance = max(dist[i][j] for j in range(1, N + 1) if i != j)
        if total_distance < min_total_distance:
            min_total_distance = total_distance
            optimal_city = i

    return optimal_city

# Считываем входные данные
N, M = map(int, input().split())
roads = [tuple(map(int, input().split())) for _ in range(M)]

# Вызываем функции для нахождения решения
distances = floyd_warshall(N, roads)
optimal_city = find_optimal_city(N, distances)

# Выводим результат
print(optimal_city)