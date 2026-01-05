"""
Reading files and saving data
PCC 3rd Ed chapter 10
"""
from pathlib import Path

path = Path('pi_million_digits.txt')
try:
    contents = path.read_text(encoding="utf-8")
except FileNotFoundError:
    print(f"Sorry, the file {path} does not exist.")
else:
    pi_string = ""
    for line in contents.splitlines():
        pi_string += line.lstrip()

    while True:
        birthday = input("Enter your birthday, in the form mmddyy: ")

        # Validate length
        if len(birthday) != 6:
            print("Invalid format. Please enter your birthday as 6 digits (mmddyy).")
            continue # Ask for input again

        # Validate if all characters are digits
        if not birthday.isdigit():
            print("Invalid input. Birthday must contain only digits.")
            continue # Ask for input again

        # Validate month (mm)
        month = int(birthday[0:2])
        if not 1 <= month <= 12:
            print("Invalid month. Month must be between 01 and 12.")
            continue # Ask for input again

        # If all validations pass, check if birthday is in pi_string
        if birthday in pi_string:
            print("Your birthday appears in the first million digits of pi!")
        else:
            print("Your birthday does not appear in the first million digits of pi.")
        break # Exit loop only after valid input and search

# EOF
