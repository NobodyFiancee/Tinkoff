def calculate_hash(current_hash, number):
    mod1 = 2 ** 64
    mod2 = 10 ** 9 + 9

    return ((current_hash[0] + (number * 7 * 17) % mod1) % mod1,
            (current_hash[1] * (number + 19 * 31) % mod2) % mod2)


n = int(input())
first_arr = list(map(int, input().split()))
m = int(input())
second_arr = list(map(int, input().split()))

hashes_first = [[] for _ in range(n)]
hashes_second = [[] for _ in range(m)]

for i in range(n):
    h = (0, 1)
    for j in range(n - i):
        if j == 0:
            h = calculate_hash(h, first_arr[i])
        else:
            h = calculate_hash(h, first_arr[i + j])
        hashes_first[j].append(h)

for i in range(m):
    h = (0, 1)
    for j in range(m - i):
        if j == 0:
            h = calculate_hash(h, second_arr[i])
        else:
            h = calculate_hash(h, second_arr[i + j])
        hashes_second[j].append(h)

hash_set = set()
max_length = 0

for i in range(n):
    for j in range(len(hashes_first[i])):
        hash_set.add(hashes_first[i][j])

for i in range(m):
    for j in range(len(hashes_second[i])):
        if hashes_second[i][j] in hash_set:
            max_length = max(max_length, i + 1)

print(max_length)