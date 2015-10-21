def sieve(n):
    is_prime = [True for i in range(n+1)]
    is_prime[0] = is_prime[1] = False
    primes = []
    for i in range(2, int(n**0.5)+1):
        if is_prime[i]:
            primes.append(i)
            for j in range(2*i, n+1, i):
                is_prime[j] = False
	return primes, is_prime	

primes = sieve(10**5)

def prime_decomposition(n):
    decomp = []
    i = 0
    while n > 1:
        p = primes[i]
        if n%p == 0:
            decomp.append(p)
            while n%p == 0:
                n //= p
        i += 1

def f(x):
    return (x*x + c)%n


def ggt(a, b):
    if a == 0:
        return b
    return ggt(b, a%b)


def rho_factorize(n):
    x, y, d = 2, 2, 1
    while d == 1:
        x = f(x)
        y = f(f(y))
        d = ggt(abs(x-y),n)
        
for i in range(2, 10**5):
    i_1 = set(prime decompositon(i))
    i_2 = set(prime decompositon(i+2)) 
    i_3 = set(prime decompositon(i+3))   
    i_4 = set(prime decompositon(i+4))
