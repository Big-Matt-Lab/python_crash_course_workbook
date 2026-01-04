"""
Docstring for first_numbers
"""
# using range for numerical lists
for value in range(1, 5):
    print(value)
numbers = list(range(1, 6))
print(numbers)
# using range step argument
even_numbers = list(range(2, 11, 2))
print(even_numbers)

squares = [] # create empty list
for value in range(1, 11): # loop
    square = value ** 2 # square the value
    squares.append(square) # append squared value to list squares
print(squares)

# cleaner code
squares = []
for value in range(1, 11):
    squares.append(value ** 2) # eliminates the 'square variable, directly appends value to squares
print(squares)
#
#cleanest
squares = [value ** 2 for value in range(1, 11)] 
print(squares)

# counting
for number in range(1, 21):
    print(number)
# list comprehension cube formula
cubes = [value ** 3 for value in range (1, 21)]
print(cubes)
#
# looping numbers
numbers = (list(range(1,10)))
for number in numbers:
    if number == 1:
        print(f"{number}st")
    elif number == 2:
        print(f"{number}nd")
    elif number == 3:
        print(f"{number}rd")
    else:
        print(f"{number}th")
# EOF
