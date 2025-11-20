import math


def prime_factors(n):
    prime_factors = []
    while n % 2 == 0:
        prime_factors.append(2)
        n //= 2
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        while n % i == 0:
            prime_factors.append(i)
            n //= i
    if n != 1:
        prime_factors.append(n)
    return prime_factors
