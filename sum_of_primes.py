"""
A solution to Euler problem 10
Find the sum of the primes below 'n' (LIMIT)
Credit to reddit user Bitwise Gamgee for much of this
"""
def find_primes(limit: int) -> int:
    """
    Finds the sum of all prime numbers below a given limit using the
    Sieve of Eratosthenes algorithm.

    Args:
        limit (int): The upper bound (exclusive) for prime numbers to sum.

    Returns:
        int: The sum of all prime numbers below the limit.
    """
    is_prime = [True] * (limit + 1)
    is_prime[0] = is_prime[1] = False

    for number in range(2, int(limit**0.5) + 1):
        if is_prime[number]:
            for multiple in range(number * number, limit + 1, number):
                is_prime[multiple] = False

    # Sum all numbers that are still marked as prime after the sieving process
    sum_of_primes = sum(number for number, prime_status in enumerate(is_prime) if prime_status)

    return sum_of_primes


if __name__ == "__main__":
    LIMIT = 2000000
    result = find_primes(LIMIT)
    print(f"The sum of all the prime numbers less than {LIMIT} is {result:,}")
# EOF
