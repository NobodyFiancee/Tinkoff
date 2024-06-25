import sys

n, m, k = map(int, sys.stdin.readline().split())

matrix = [[0] * m for _ in range(n)]
pref_sum_2d = [[0] * m for _ in range(n)]

for y in range(n):
    elements = list(map(int, sys.stdin.readline().split()))
    for x in range(m):
        matrix[y][x] = elements[x]

pref_sum_2d[0][0] = matrix[0][0]
for i in range(1, n):
    pref_sum_2d[i][0] = pref_sum_2d[i - 1][0] + matrix[i][0]

for i in range(1, m):
    pref_sum_2d[0][i] = pref_sum_2d[0][i - 1] + matrix[0][i]

for i in range(1, n):
    for j in range(1, m):
        pref_sum_2d[i][j] = pref_sum_2d[i - 1][j] + pref_sum_2d[i][j - 1] - pref_sum_2d[i - 1][j - 1] + matrix[i][j]

for i in range(k):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    y1, x1, y2, x2 = y1 - 1, x1 - 1, y2 - 1, x2 - 1
    sys.stdout.write(str(
        pref_sum_2d[x2][y2]
        - (pref_sum_2d[x1 - 1][y2] if x1 else 0)
        - (pref_sum_2d[x2][y1 - 1] if y1 else 0)
        + (pref_sum_2d[x1 - 1][y1 - 1] if (x1 and y1) else 0)
    ) + '\n')