def mod_exp(base, exp, mod):
    result = 1
    while exp > 0:
        if exp % 2 == 1:
            result = (result * base) % mod
        base = (base * base) % mod
        exp //= 2
    return result


def mod_inverse(a, mod):
    return mod_exp(a, mod - 2, mod)


def solve(N, M, K, MOD):
    M_pow_N_mod = mod_exp(M, N, MOD)
    K_inv_mod = mod_inverse(K, MOD)
    result = (M_pow_N_mod * K_inv_mod) % MOD
    return result


N, M, K, MOD = map(int, input().split())
result = solve(N, M, K, MOD)
print(result)