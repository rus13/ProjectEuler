__author__ = 'Ruslan'
import random
import sys
import fractions


def is_probable_prime(n, k=7):
    """use Rabin-Miller algorithm to return True (n is probably prime)
       or False (n is definitely composite)"""
    if n < 6:  # assuming n >= 0 in all cases... shortcut small cases here
        return [False, False, True, True, False, True][n]
    elif n & 1 == 0:  # should be faster than n % 2
        return False
    else:
        s, d = 0, n - 1
        while d & 1 == 0:
            s, d = s + 1, d >> 1
        # Use random.randint(2, n-2) for very large numbers
        for a in random.sample(range(2, min(n - 2, sys.maxsize)), min(n - 4, k)):
            x = pow(a, d, n)
            if x != 1 and x + 1 != n:
                for r in range(1, s):
                    x = pow(x, 2, n)
                    if x == 1:
                        return False  # composite for sure
                    elif x == n - 1:
                        a = 0  # so we know loop didn't continue to end
                        break  # could be strong liar, try another a
                if a:
                    return False  # composite if we reached end of this loop
        return True  # probably prime if reached end of outer loop


def egcd(a, b):
    x, y, u, v = 0, 1, 1, 0
    while a != 0:
        q, r = b // a, b % a
        m, n = x - u * q, y - v * q
        b, a, x, y, u, v = a, r, u, v, m, n
    gcd = b
    return gcd, x, y


def modinv(a, m):
    gcd, x, y = egcd(a, m)
    if gcd != 1:
        return None  # modular inverse does not exist
    else:
        return x % m


def rsa_create_keys(length):
    p = (random.random()+1)*(2**length)
    q = (random.random()+1)*(2**length)
    while not is_probable_prime(p):
            p = (random.random()+1)*(2**length)
    while not is_probable_prime(q):
            q = (random.random()+1)*(2**length)
    n = p*q
    phi = n - (p + q - 1)
    e = random.random()*phi + 1
    while fractions.gcd(e, phi) != 1:
        e = random.random()*phi + 1
    d = modinv(e, phi)
    return e, d


def rsa_encode(text, public, n):
    plain = int(text)
    return (plain**public)%n


def rsa_decode(encrypted, private, n):
    return str((encrypted**private)%n)