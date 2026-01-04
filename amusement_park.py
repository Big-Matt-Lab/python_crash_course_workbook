"""
Docstring for amusement_park
Handles age-based pricing for an amusement park, with robust input validation.
"""

while True:
    print()
    age = input('What is your age? Please enter a number from 1 - 100: ')
    try:
        age = int(age)
        if 1 <= age <= 100:
            break
        
        print('Please enter a valid age.')
    except ValueError:
        print("Invalid response. Please enter a number.")

if age < 4:
    price = 0
elif age < 18:
    price = 25
else:
    price = 40
print()
print(f"The price of admission is ${price}.")
# EOF
