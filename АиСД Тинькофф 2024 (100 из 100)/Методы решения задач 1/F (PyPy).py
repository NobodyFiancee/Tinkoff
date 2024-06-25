n = int(input())
mas = []

for i in range(n):
    start, end = map(int, input().split())
    mas.append((start, 1))
    mas.append((end, -1))

mas.sort()
c = 1
res = 0
for i in range(1, len(mas)):
    if c != 0:
        res += (mas[i][0] - mas[i-1][0])
    c += mas[i][1]


print(res)