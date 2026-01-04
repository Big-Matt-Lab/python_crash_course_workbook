"""
This module contains a custom testing framework and test cases for the functions
defined in `nile_codecademy.py`. It includes helper classes `Driver` and `Trip`
for simulating real-world entities in the tests.
"""

def test_function(fn):
    """Dispatches the appropriate test function based on the name of the function being tested."""
    test_map = {
        "calculate_shipping_cost": test_shipping,
        "calculate_driver_cost": test_driver,
        "calculate_money_made": test_money,
    }
    test_func = test_map.get(fn.__name__)
    if test_func:
        test_func(fn)
    else:
        print(f"No test found for function: {fn.__name__}")



def test_shipping(f):
    """Tests the calculate_shipping_cost function."""
    try:
        costs = f((0, 0), (1, 1))
    except TypeError:
        print(
            "calculate_shipping_cost() did not provide default argument for shipping_type"
        )
        return
    if not type(costs) is str:
        print("calculate_shipping_cost() did not format the result in a string")
        return
    if costs != "$1.04":
        print(
            "calculate_shipping_cost((0, 0), (1, 1)) returned {}. Expected result is {}".format(
                costs, "$1.04"
            )
        )
        return
    print("OK! calculate_shipping_cost() passes tests")


class Driver:
    """Represents a driver with a specific speed and salary."""
    def __init__(self, speed, salary):
        """
        Initializes a Driver object.
        Args:
            speed (float): The driver's speed.
            salary (float): The driver's hourly salary.
        """
        self.speed = speed
        self.salary = salary

    def __repr__(self):
        """Returns a string representation of the Driver object."""
        return "Nile Driver speed {} salary {}".format(self.speed, self.salary)


driver1 = Driver(4, 10)
driver2 = Driver(7, 20)

def test_driver(f):
    """Tests the calculate_driver_cost function."""
    try:
        price, driver = f(80, {'driver1': driver1, 'driver2': driver2})
    except TypeError:
        print("calculate_driver_cost() doesn't expect multiple driver arguments")
        return
    if type(driver) is not Driver:
        print("calculate_driver_cost() did not return driver")
        return
    if price != 200:
        print(
            f"calculate_driver_cost() did not provide correct final price
            expected {}, received {})".format(200, price)
            )
        return
    if driver is not driver1:
        print("calculate_driver_cost() did not provide least expensive driver")
        return
    print("OK! calculate_driver_cost() passes tests")


class Trip:
    def __init__(self, cost, driver, driver_cost):
        self.cost = cost
        driver.cost = driver_cost
        self.driver = driver


trip1 = Trip(200, driver1, 15)
trip2 = Trip(300, driver2, 40)


def test_money(f):
    try:
        money = f(UEXODI=trip1, DEFZXIE=trip2)
    except TypeError:
        print("calculate_money_made() doesn't expect multiple trip keyword arguments")
        return
    if type(money) not in (int, float):
        print("calculate_driver_cost() did not return a number")
        return
    if money != 445:
        print(
            "calculate_driver_cost() did not provide correct final price (expected {}, received {})".format(
                445, money
            )
        )
        return
    print("OK! calculate_money_made() passes tests")
# End of file
