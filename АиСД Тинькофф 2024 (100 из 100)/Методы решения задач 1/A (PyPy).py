import sys

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
prefix_sum = [0] * (n + 1)
prefix_xor = [0] * (n + 1)
for i in range(1, n + 1):
    prefix_sum[i] = prefix_sum[i - 1] + arr[i - 1]
    prefix_xor[i] = prefix_xor[i - 1] ^ arr[i - 1]

m = int(sys.stdin.readline())

for _ in range(m):
    q, l, r = map(int, sys.stdin.readline().split())
    if q == 1:
        sys.stdout.write(str(prefix_sum[r] - prefix_sum[l-1]) + '\n')
    else:
        sys.stdout.write(str(prefix_xor[r] ^ prefix_xor[l-1]) + '\n')