# write a program to accept a number n 
# a. check if n is prime 
# b. Generate all prime numbers till n
# c. Generate first n prime numbers

import math

def is_prime(num):
    """a. Helper function to check if a number is prime"""
    if num <= 1:
        return False
    # Check for factors up to the square root of the number
    for i in range(2, math.isqrt(num) + 1):
        if num % i == 0:
            return False
    return True

def generate_primes_till_n(n):
    """b. Function to generate all prime numbers till n"""
    primes = []
    for num in range(2, n + 1):
        if is_prime(num):
            primes.append(num)
    return primes

def generate_first_n_primes(n):
    """c. Function to generate the first n prime numbers"""
    primes = []
    num = 2
    while len(primes) < n:
        if is_prime(num):
            primes.append(num)
        num += 1
    return primes

try:
    # Accept a number 'n' from the user
    n = int(input("Enter a positive integer (n): "))

    if n < 0:
        print("Please enter a positive integer.")
    else:
        print("\n--- RESULTS ---")
        
        # a. Check if n is prime
        if is_prime(n):
            print(f"a. {n} is a prime number.")
        else:
            print(f"a. {n} is NOT a prime number.")
            
        # b. Generate all prime numbers till n
        primes_till_n = generate_primes_till_n(n)
        print(f"b. Prime numbers up to {n}: {primes_till_n}")
        
        # c. Generate first n prime numbers
        first_n_primes = generate_first_n_primes(n)
        print(f"c. The first {n} prime numbers: {first_n_primes}")

except ValueError:
    print("Invalid input! Please enter a valid integer.")