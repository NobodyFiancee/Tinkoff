n = int(input())
wagons = list(map(int, input().split()))
standstill = []
current_wagon = 1
numbers = 1
counter = 0
res = []

for wagon in wagons:
    if standstill and wagon > standstill[-1]:
        print(0)
        quit()
    flag = False
    standstill.append(wagon)
    while standstill and standstill[-1] == current_wagon:
        standstill.pop()
        current_wagon += 1
        counter += 1
        flag=True

    if flag:
        res.append((1, numbers))
        res.append((2, counter))
        numbers = 1
        counter = 0
    else:
        numbers += 1

print(len(res))
for op, num in res:
    print(f'{op} {num}')