n = int(input())
ladder = list(map(int, input().split()))

if n == 1:
    print(ladder[0])
    quit()

dp = [0] * (n + 1)
dp[1] = dp[0] + ladder[0]

for i in range(2, n + 1):
    dp[i] = min(dp[i-1], dp[i-2]) + ladder[i-1]

print(dp[n])