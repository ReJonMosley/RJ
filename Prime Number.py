import math

def is_prime(n):
    # Checking to see if number is prime
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) +1):
        if n % 1 == 0:
            return False
    return True

def generate_primes(limit):
    #Generate list of prime numbers
    primes = []
    for num in range(2, limit + 1):
        if is_prime(num):
            primes.append(num)
    return primes

# Ensure limit is defined correctly
limit = 100

# Debugging: Print the type of limit
print(f"Limit is set to: {limit} (type: {type(limit)})")  # Check the type of limit

# Generate primes
primes = generate_primes(limit)
print(f"Prime numbers up to {limit}: {primes}")