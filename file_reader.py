"""
Reading files and saving data
PCC 3rd Ed chapter 10
"""
from pathlib import Path

path = Path('pi_million_digits.txt')
contents = path.read_text(encoding="utf-8")

pi_string = ""
for line in contents.splitlines():
    pi_string += line.lstrip()

birthday = input("Enter your birthday, in the form mmddyy: ")
if birthday in pi_string:
    print("Your birthday appears in the first million digits of pi!")
else:
    print("Your birthday does not appear in the first million digits of pi.")

# EOF
