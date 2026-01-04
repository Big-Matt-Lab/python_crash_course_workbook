""" Creating a simple car class """
class Car:
    """ Working with classes and methods"""

    def __init__(self, make, model, year):
        """Initialize car attributes"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """ Return a neatly formatted, descriptive name"""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """Mileage statement"""
        return self.odometer_reading

    def update_odometer(self, mileage):
        """
        Set the odometer reading to the given value.
        Reject the change if it attempts to roll back the odometer.
        """
        if not isinstance(mileage, (int, float)):
            raise TypeError("Mileage must be a number.")
        if mileage < 0:
            raise ValueError("Mileage cannot be negative.")
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            raise ValueError("You can't roll back the odometer!")

    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading."""
        if not isinstance(miles, (int, float)):
            raise TypeError("Miles to increment must be a number.")
        if miles >= 0:
            self.odometer_reading += miles
        else:
            raise ValueError("You can't increment the odometer with negative miles!")

my_new_car = Car('audi', 'a4', 2024)
print(my_new_car.get_descriptive_name())

# Demonstrate setting the odometer
try:
    current_mileage_str = input("What is the current mileage?: ")
    current_mileage = int(current_mileage_str)
    my_new_car.update_odometer(current_mileage)
    print(f"This car has {my_new_car.read_odometer()} miles on it.")
except ValueError as e:
    print(f"Error updating odometer: {e}")
except TypeError as e:
    print(f"Error updating odometer: {e}")


# Demonstrate incrementing the odometer
my_new_car.increment_odometer(100)
my_new_car.read_odometer()

