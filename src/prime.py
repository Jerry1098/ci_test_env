def get_first_100_primes():
    primes = []
    num = 2
    while len(primes) < 100:
        if all(num % p != 0 for p in primes):
            primes.append(num)
        num += 1
    return primes
