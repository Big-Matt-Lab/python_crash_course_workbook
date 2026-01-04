"""
Docstring for cars
Intro to if statements
"""
print()# new line for readibility in terminal

cars = ['audi', 'bmw', 'suburu', 'toyota']
for car in cars: # start loop
    if car == 'bmw': # if statement, conditional ==
        print(car.upper()) # print if condition is True
    else:
        print(car.title()) # if condion is False
# EOF
