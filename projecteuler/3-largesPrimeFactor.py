# Largest prime factor
# Problem 3

# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?

# Get all factors, see which ones are primes, get greatest one

def factors(n):
    return [x for x in range(1,(n//2) +1) if (n % x == 0)]

def is_prime(num):
    return(len(factors(num)) == 1)

def prime_factors(num):
    return [f for f in factors(num) if is_prime(f)]

def lpf(num):
    return max(prime_factors(num))

