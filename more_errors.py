"""
catching errors with input and missing files
"""
def add_em_up(num_1: int, num_2: int) -> int:
    """
    Calculates the sum of two integers.

    Args:
        num_1 (int): The first integer.
        num_2 (int): The second integer.

    Returns:
        int: The sum of num_1 and num_2.
    """
    total = num_1 + num_2
    return total

def get_integer_input(prompt: str) -> int:
    """
    Prompts the user for an integer and retries until valid input is received.

    Args:
        prompt (str): The message displayed to the user.

    Returns:
        int: The valid integer entered by the user.
    """
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

def main():
    """Main execution loop for the adding machine."""
    while True:
        print("Please input two(2) numbers.")

        num_1 = get_integer_input("First number: ")
        num_2 = get_integer_input("Second number: ")

        result = add_em_up(num_1, num_2)
        print(f"The sum of {num_1} and {num_2} is {result}.")

        play_again = input("Would you like to try again? (y/n): ").strip().lower()
        if play_again != 'y':
            print("Thanks for trying our adding machine.")
            break

if __name__ == "__main__":
    main()

# EOF
