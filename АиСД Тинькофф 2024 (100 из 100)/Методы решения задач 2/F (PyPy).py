def count_set_bits(x):
    return bin(x).count('1')

total_amount, num_coins = map(int, input().split())
coin_values = list(map(int, input().split()))
total_sum = sum(coin_values) * 2
sum_frequency = [0] * (1 << num_coins)
sum_occurrences = {}

if total_sum < total_amount:
    print(-1)
    exit()

for i in range(1 << num_coins):
    if i:
        sum_frequency[i] = sum_frequency[i ^ (1 << (i.bit_length() - 1))] + coin_values[i.bit_length() - 1]
    if sum_frequency[i] not in sum_occurrences:
        sum_occurrences[sum_frequency[i]] = (count_set_bits(i), i)
    else:
        sum_occurrences[sum_frequency[i]] = min(sum_occurrences[sum_frequency[i]], (count_set_bits(i), i))

min_coins_needed = 60
best_coin_selection = -1

for i in range(1 << num_coins):
    if total_amount - sum_frequency[i] in sum_occurrences:
        if count_set_bits(i) + sum_occurrences[total_amount - sum_frequency[i]][0] < min_coins_needed:
            min_coins_needed = count_set_bits(i) + sum_occurrences[total_amount - sum_frequency[i]][0]
            best_coin_selection = i

if best_coin_selection < 0:
    print(0)
    exit()

payment_coins = []
for i in range(num_coins):
    if (1 << i) & best_coin_selection:
        payment_coins.append(coin_values[i])
    if (1 << i) & sum_occurrences[total_amount - sum_frequency[best_coin_selection]][1]:
        payment_coins.append(coin_values[i])

print(len(payment_coins))
print(*payment_coins)
