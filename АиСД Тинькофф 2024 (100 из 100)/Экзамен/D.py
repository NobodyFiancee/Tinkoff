MOD = 10 ** 9 + 9


def generate_three_digit_primes():
    sieve = [True] * 1000
    sieve[0] = sieve[1] = False
    for start in range(2, int(len(sieve) ** 0.5) + 1):
        if sieve[start]:
            for multiple in range(start * start, len(sieve), start):
                sieve[multiple] = False
    primes = [num for num in range(100, 1000) if sieve[num]]
    return primes


def count_triprime_numbers(N):
    primes = generate_three_digit_primes()
    prime_set = set(primes)

    dp = [0] * 1000
    for prime in primes:
        dp[prime] = 1

    for _ in range(3, N):
        new_dp = [0] * 1000
        for num in range(100, 1000):
            if dp[num] > 0:
                for digit in range(10):
                    new_num = (num % 100) * 10 + digit
                    if new_num in prime_set:
                        new_dp[new_num] = (new_dp[new_num] + dp[num]) % MOD
        dp = new_dp

    result = sum(dp) % MOD
    return result


N = int(input())
print(count_triprime_numbers(N))
