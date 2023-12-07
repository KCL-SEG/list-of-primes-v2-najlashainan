"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    if number_of_primes < 1:
        raise ValueError("number_of_primes has to be greater than 0")
    list = []
    n = 2
    while(len(list) < number_of_primes):
        if is_prime(n):
            list.append(n)
        n += 1
    return list

def is_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

