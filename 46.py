def sieve(n):
	is_prime = [True for i in range(n+1)]
	is_prime[0] = is_prime[1] = False
	for i in range(2, int(n**0.5)+1):
		if is_prime[i]:
			for j in range(2*i, n+1, i):
				is_prime[j] = False
	return is_prime		

is_prime = sieve(10**5)
#print(is_prime)
found = False
sol = 0
x = 9
while not found:
	if not is_prime[x]:
		q = 1
		found = True
		for q in range(1, int((x/2)**0.5)+1):
			p = x - 2*q**2
			print("x: " + str(x) + " p: "+ str(p) + " q: " + str(q))
			if p > 0 and is_prime[p]:	
				found = False
		sol = x
	x += 2
print(sol)
