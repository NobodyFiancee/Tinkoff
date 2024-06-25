def damerau_levenshtein_distance(str1, str2):
    len_1 = len(str1)
    len_2 = len(str2)
    dp = [[0] * (len_2 + 1) for _ in range(len_1 + 1)]

    for i in range(len_1 + 1):
        for j in range(len_2 + 1):
            if i == 0:
                dp[i][j] = j
            elif j == 0:
                dp[i][j] = i
            elif str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])
                if i > 1 and j > 1 and str1[i - 1] == str2[j - 2] and str1[i - 2] == str2[j - 1]:
                    dp[i][j] = min(dp[i][j], dp[i - 2][j - 2] + 1)

    return dp[len_1][len_2]


a = input()
b = input()

print(damerau_levenshtein_distance(a, b))
