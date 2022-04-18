import math

def isPrime(n):
    if n < 2:
        return False
    result = True
    r = math.floor(math.sqrt(n))
    for d in range(2, r+1):
        if d > 2 and d % 2 == 0: continue
        if n % d == 0:
            result = False
            break
    return result

def isPrimeII(n):
    # Eliminate negative numbers and 0, 1.
    if n <= 3:
        return n > 1
    if n % 2 == 0 or n % 3 == 0:
        return False
    result = True
    r = math.floor(math.sqrt(n))
    d, f, c = 4, -1, 1
    while d < r:
        d = 6 * c + f
        if n % d == 0:
            result = False
            break
        f *= -1
        if f < 0:
            c += 1
    return result

n = 2
print("Is it a prime ? : " + str(isPrimeII(n)))
