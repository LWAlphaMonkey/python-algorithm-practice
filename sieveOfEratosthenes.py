def sieveOfEratosthenes(num):
    """
    return all prime numbers up
    to `num` in an array
    stop looping through at the square root of `num`
    """

    if num < 2:
        return False

    #initialize all num as True
    primes = [True] * (num + 1)
    primes[0] = False
    primes[1] = False

    for idx_i in range(2, int(num ** (1 / 2)) + 1):
        idx_j = 2

        while (idx_j * idx_i) <= num:
            primes[(idx_i * idx_j)] = False
            idx_j += 1

    result = []
    for idx_i in range(1, num + 1):
        if primes[idx_i] == True:
            result.append(idx_i)

    return result

print(sieveOfEratosthenes(10))
print(sieveOfEratosthenes(20))
print(sieveOfEratosthenes(200))
