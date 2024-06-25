n = int(input())
general_cash = n
mas = []
current_cash = 0

for i in range(n):
    hs, ms, ss, he, me, se = map(int, input().split())
    start = hs * 60 * 60 + ms * 60 + ss
    end = he * 60 * 60 + me * 60 + se
    if start == end:
        general_cash -= 1
    else:
        mas.append((start, 1))
        mas.append((end, -1))
        if start > end:
            current_cash += 1

res = 0
mas.sort()
if current_cash == general_cash:
    res += mas[0][0]

for i in range(len(mas)):
    current_cash += mas[i][1]
    if current_cash == general_cash:
        if i != len(mas) - 1:
            res += mas[i + 1][0]
            res -= mas[i][0]
        else:
            res += 24*60*60
            res -= mas[i][0]

print(res)