def longest_palindromic_subsequence(s):
    n = len(s)
    dp = [[0] * n for _ in range(n)]

    for i in range(n):
        dp[i][i] = 1

    for l in range(2, n + 1):
        for i in range(n - l + 1):
            j = i + l - 1
            if s[i] == s[j] and l == 2:
                dp[i][j] = 2
            elif s[i] == s[j]:
                dp[i][j] = dp[i + 1][j - 1] + 2
            else:
                dp[i][j] = max(dp[i][j - 1], dp[i + 1][j])

    subseq = ""
    i, j = 0, n - 1
    while i <= j:
        if s[i] == s[j]:
            subseq += s[i]
            i += 1
            j -= 1
        elif dp[i][j - 1] > dp[i + 1][j]:
            j -= 1
        else:
            i += 1

    if dp[0][n - 1] % 2 == 0:
        return dp[0][n - 1], subseq + subseq[::-1]
    else:
        return dp[0][n - 1], subseq + subseq[:-1][::-1]


input_string = input().strip()
length, palindrome = longest_palindromic_subsequence(input_string)
print(length)
print(palindrome)
