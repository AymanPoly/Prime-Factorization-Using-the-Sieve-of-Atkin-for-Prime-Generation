import math

# ------------------------------
# 1. Sieve of Atkin (prime list)
# ------------------------------
def sieve_of_atkin(limit):
    if limit <= 2:
        return []

    is_prime = [False] * limit
    sqrt_lim = int(math.isqrt(limit)) + 1

    for x in range(1, sqrt_lim):
        for y in range(1, sqrt_lim):
            n = 4*x*x + y*y
            if n < limit and (n % 12 == 1 or n % 12 == 5):
                is_prime[n] = not is_prime[n]

            n = 3*x*x + y*y
            if n < limit and (n % 12 == 7):
                is_prime[n] = not is_prime[n]

            n = 3*x*x - y*y
            if x > y and n < limit and (n % 12 == 11):
                is_prime[n] = not is_prime[n]

    for r in range(5, sqrt_lim):
        if is_prime[r]:
            r2 = r*r
            for k in range(r2, limit, r2):
                is_prime[k] = False

    primes = []
    if limit > 2:
        primes.append(2)
    if limit > 3:
        primes.append(3)

    for i in range(5, limit):
        if is_prime[i]:
            primes.append(i)

    return primes

# -----------------------------------
# 2. Prime factorization with powers
# -----------------------------------
def prime_factors_with_powers(N):
    primes = sieve_of_atkin(int(math.isqrt(N)) + 1)
    factors = {}
    n = N

    for p in primes:
        if p*p > n:
            break
        count = 0
        while n % p == 0:
            n //= p
            count += 1
        if count > 0:
            factors[p] = count

    if n > 1:  # n is prime itself
        factors[n] = 1

    return factors

# Example usage
N = 120
factors = prime_factors_with_powers(N)
print(f"Prime factors of {N} with their powers:", factors)
