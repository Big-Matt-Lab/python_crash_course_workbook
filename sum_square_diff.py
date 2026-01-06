"""
An exercise to solve euler #6
The difference between sums and squares

This script calculates the difference between the sum of the squares of the first N natural numbers
and the square of the sum of the first N natural numbers.
"""
NUM = 100

def sum_of_squares(n: int) -> int:
    """
    Calculates the sum of the squares of a range up to a given positive integer.
    Uses the formula: n * (n + 1) * (2n + 1) / 6

    Args:
        n (int): The max number in the range

    Returns:
        int: The sum.
    """
    # Using the mathematical formula for sum of squares
    return n * (n + 1) * (2 * n + 1) // 6

def square_of_sums(n: int) -> int:
    """
    Calculates the square of the sums of a range up to a given positive integer.
    First calculates the sum using the formula: n * (n + 1) / 2, then squares the result.

    Args:
        n (int): The max number in a range

    Returns:
        int: The square.
    """
    # Using the mathematical formula for sum of first n natural numbers
    sum_natural_numbers = n * (n + 1) // 2
    return sum_natural_numbers ** 2

def calculate_sum_square_difference(n: int) -> int:
    """
    Calculates the difference between the sum of the squares of the first n natural numbers
    and the square of the sum of the first n natural numbers.

    Args:
        n (int): The upper limit of the natural numbers.

    Returns:
        int: The calculated difference.
    """
    sum_sq = sum_of_squares(n)
    sq_sum = square_of_sums(n)
    return sq_sum - sum_sq

def main():
    difference = calculate_sum_square_difference(NUM)
    print(f"The difference between the sum of the squares and the square of the sums "
          f"of the first {NUM} natural numbers is {difference:,}.")

if __name__ == "__main__":
    main()
    
# EOF
