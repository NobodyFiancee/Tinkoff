def get_move(n, m):
    dp = [[0] * (m + 3) for _ in range(n + 3)]
    dp[2][2] = 1
    startx, starty = 2, 2
    while startx < n + 1 or starty < m + 1:
        if starty == m + 1:
            startx += 1
        else:
            starty += 1

        x, y = startx, starty
        while x <= n + 1 and y >= 2:
            dp[x][y] = dp[x + 1][y - 2] + dp[x - 1][y - 2] + dp[x - 2][y - 1] + dp[x - 2][y + 1]
            x += 1
            y -= 1

    return dp[n + 1][m + 1]


n, m = map(int, input().split())
print(get_move(n, m))