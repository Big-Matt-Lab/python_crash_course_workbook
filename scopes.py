"""
Scopes docstring
"""
# Imaginary File: main.py
import random

FIRST_NAME = "Jaya"
LAST_NAME = "Bodegard"


def print_variables():
    """
    Docstring for print_variables
    """
    random_number = random.randint(0, 9)
    print(FIRST_NAME)
    print(LAST_NAME)
    print(random_number)

print(globals())
