import math

"""
This is an attempt at solving Project Euler #3
Prime Factorization
"""

TARGET_NUMBER = 600851475143 # Edit this number

def get_largest_prime_factor(n: int) -> int:
    """
    Calculates the largest prime factor of a given positive integer.

    Args:
        n (int): The number for which to find the largest prime factor.

    Returns:
        int: The largest prime factor of n.
    """
    largest_prime_factor = 1

    # Handle factor 2
    while n % 2 == 0:
        largest_prime_factor = 2
        n //= 2

    # Handle odd factors from 3 up to sqrt(n)
    # We only need to check up to sqrt(n) because if n has a prime factor
    # greater than sqrt(n), it must also have one smaller than sqrt(n) (which would have been found).
    # If n remains > 1 after this loop, then the remaining n is prime and the largest factor.
    f = 3
    while f * f <= n: # Optimized loop condition
        if n % f == 0:
            largest_prime_factor = f
            n //= f # Divide out the factor
        else:
            f += 2 # Move to the next odd potential factor

    # If n is still greater than 2, it means the remaining n is a prime factor itself (and the largest one)
    if n > 2:
        largest_prime_factor = n

    return largest_prime_factor

largest_factor = get_largest_prime_factor(TARGET_NUMBER)
print(f"The largest prime factor of {TARGET_NUMBER:,} is: {largest_factor:,}")
# EOF
