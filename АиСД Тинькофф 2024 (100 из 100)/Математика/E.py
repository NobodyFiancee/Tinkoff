MOD = 10 ** 9 + 7


def mod_inverse(a, p):
    return pow(a, p - 2, p)


def precompute_factorials_and_inverses(n, p):
    fact = [1] * (n + 1)
    inv_fact = [1] * (n + 1)

    for i in range(2, n + 1):
        fact[i] = fact[i - 1] * i % p

    inv_fact[n] = mod_inverse(fact[n], p)
    for i in range(n - 1, 0, -1):
        inv_fact[i] = inv_fact[i + 1] * (i + 1) % p

    return fact, inv_fact


def binomial_coefficient(n, k, p):
    if k > n:
        return 0
    fact, inv_fact = precompute_factorials_and_inverses(n, p)
    return fact[n] * inv_fact[k] % p * inv_fact[n - k] % p


n, k = map(int, input().split())
result = binomial_coefficient(n, k, MOD)
print(result)
