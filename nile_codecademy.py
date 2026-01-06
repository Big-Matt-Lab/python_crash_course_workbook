from nile import get_distance, format_price, SHIPPING_PRICES
from test import test_function

"""
This module contains core business logic for the Nile shipping application,
including functions to calculate shipping costs, driver costs, and total revenue.
"""


# 1. Calculate Shipping Cost (Updated with Docstrings, Type Hints, and Error Handling)
def calculate_shipping_cost(
    from_coords: tuple[float, float],
    to_coords: tuple[float, float],
    shipping_type: str = "Overnight"
) -> str:
    """
    Calculates the total shipping cost between two coordinates.

    Args:
        from_coords (tuple[float, float]): Latitude and longitude of the origin.
        to_coords (tuple[float, float]): Latitude and longitude of the destination.
        shipping_type (str, optional): The type of shipping (e.g., "Ground", "Priority", "Overnight").
                                       Defaults to "Overnight".

    Returns:
        str: The formatted shipping price (e.g., "$1.04").

    Raises:
        ValueError: If an invalid shipping_type is provided.
    """
    distance = get_distance(*from_coords, *to_coords) # Unpack tuples for get_distance
    shipping_rate = SHIPPING_PRICES.get(shipping_type)

    if shipping_rate is None:
        raise ValueError(f"Invalid shipping type: '{shipping_type}'. "
                         f"Available types are: {', '.join(SHIPPING_PRICES.keys())}")

    price = distance * shipping_rate
    return format_price(price)


test_function(calculate_shipping_cost)


# 2. Calculate Driver Cost (Updated with Docstrings, Type Hints, and Error Handling)
def calculate_driver_cost(distance: float, drivers_dict: dict) -> tuple[float | None, object | None]:
    """
    Finds the cheapest driver for a given distance from a dictionary of drivers.
    Drivers with zero or negative speed are ignored.
    Returns (None, None) if no suitable driver is found.
    """
    cheapest_driver = None
    cheapest_driver_price = None

    # Iterate through the dictionary items (name and driver object)
    for driver_name, driver in drivers_dict.items():
        # Calculate cost based on driver attributes
        if not hasattr(driver, 'speed') or not hasattr(driver, 'salary'):
            print(f"Warning: Driver '{driver_name}' is missing 'speed' or 'salary' attribute. Skipping.")
            continue
        if driver.speed <= 0:
            print(f"Warning: Driver '{driver_name}' has non-positive speed ({driver.speed}). Skipping.")
            continue

        driver_time = distance / driver.speed
        price_for_driver = driver_time * driver.salary

        # Logic to find the cheapest
        if cheapest_driver is None or price_for_driver < cheapest_driver_price:
            cheapest_driver = driver  # Keep the driver object
            cheapest_driver_price = price_for_driver

    return cheapest_driver_price, cheapest_driver


test_function(calculate_driver_cost)


# 3. Calculate Money Made (Updated with Docstrings and Type Hints)
def calculate_money_made(**trips: dict[str, object]) -> float:
    """
    Calculates the total money made from a collection of trips.

    Args:
        **trips: Keyword arguments where each key is a trip ID (str)
                 and each value is a Trip object with a 'cost' attribute.

    Returns:
        float: The total money made from all trips.
    """
    total_money_made = 0
    # trips is a dictionary where the value is the Trip object
    for trip_id, trip in trips.items():
        # Add the cost property of each trip to the total
        if not hasattr(trip, 'cost'):
            print(f"Warning: Trip '{trip_id}' is missing 'cost' attribute. Skipping.")
            continue
        total_money_made += trip.cost
    return total_money_made


# test_function(calculate_money_made)
