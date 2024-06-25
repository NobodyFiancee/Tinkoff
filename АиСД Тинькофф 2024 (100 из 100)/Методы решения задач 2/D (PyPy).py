def min_cut_cost(L, N, cuts):
    N += 2
    d = [[0] * N for _ in range(N)]

    for j in range(1, N):
        for i in range(j - 2, -1, -1):
            d[i][j] = float('inf')
            for k in range(i + 1, j):
                d[i][j] = min(d[i][j], d[i][k] + d[k][j])
            d[i][j] += cuts[j] - cuts[i]

    return d[0][N - 1]


L, N = map(int, input().split())
inpt = list(map(int, input().split()))
cuts = [0] + inpt + [L]

result = min_cut_cost(L, N, cuts)
print(result)