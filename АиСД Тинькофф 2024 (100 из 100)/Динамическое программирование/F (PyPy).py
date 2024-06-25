def find_largest_square(n, m, grid):
    dp = [[0] * m for _ in range(n)]
    max_side = 0
    max_x = max_y = 0
    for x in range(n):
        for y in range(m):
            if grid[x][y] == 1:
                if x == 0 or y == 0:
                    dp[x][y] = 1
                else:
                    dp[x][y] = min(dp[x-1][y], dp[x][y-1], dp[x-1][y-1]) + 1

                if dp[x][y] >= max_side:
                    max_side = dp[x][y]
                    max_x = x
                    max_y = y

    return max_side, max_x - max_side + 1, max_y - max_side + 1


n, m = map(int, input().split())
field = [list(map(int, input().split())) for _ in range(n)]

max_side, top_left_x, top_left_y = find_largest_square(n, m, field)
print(max_side)
print(top_left_x + 1, top_left_y + 1)
