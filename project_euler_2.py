"""
Calculates the sum of even-valued terms in the Fibonacci sequence
whose values do not exceed a specified maximum.
"""
MAX_NUMBER = 4000000 # Edit to the maximum allowed number in the sequenceexit()
total = 0
a, b = 1, 2

# The loop processes 'a' as the current Fibonacci term.
while a <= MAX_NUMBER: # Loop as long as the current term 'a' is within the max
    if a % 2 == 0: # Test if the current term 'a' is even
        total += a # Sum all even numbers whose value does not exceed MAX_NUMBER
    # Generate the next Fibonacci term
    a, b = b, a + b
print(f"The sum of the even Fibonacci numbers whose values do not exceed {MAX_NUMBER:,} is: {total:,}")
# EOF
