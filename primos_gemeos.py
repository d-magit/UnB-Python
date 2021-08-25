def primos_gemeos(n):
    primes = [2, 3]
    result = []
    i = 0
    while len(result) < n:
        prime = primes[-1]
        while True:
            prime += 2
            isPrime = True
            for x in range(2, int(prime**(1/2)) + 1):
                if prime % x == 0:
                    isPrime = False
                    break
            if isPrime:
                primes.append(prime)
                break
        if (primes[i] + 2) == primes[i + 1]:
            result.append((primes[i], (primes[i] + 2)))
        i += 1
    return result