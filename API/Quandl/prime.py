from math import sqrt

def jennyPrime():
	primes = []
	base = "8675309"
	for z in range(1, 1000):
		n = int(str(z)+base)
		if isPrime(n):
			primes.append(n)
	return primes
	

def isPrime(x):
	if x & 1 == 0:
		return False
	lim = int(sqrt(x))
	for i in range(3, lim, 2):
		if (x % i) == 0:
			return False
	return True

if __name__ == "__main__":
	data = jennyPrime()
	#print(isPrime(18675309))