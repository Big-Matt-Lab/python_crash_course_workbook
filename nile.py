"""
Utility functions for the Nile shipping project, including distance calculation
and price formatting.
"""
from math import sin, cos, atan2, sqrt, radians

# Earth's radius in kilometers (mean radius)
EARTH_RADIUS_KM = 6371

def get_distance(from_lat: float, from_long: float, to_lat: float, to_long: float) -> float:
    """
    Calculates the distance between two points on Earth using the Haversine formula.
    Assumes input latitudes and longitudes are in degrees and converts them to radians.

    Args:
        from_lat (float): Latitude of the starting point in degrees.
        from_long (float): Longitude of the starting point in degrees.
        to_lat (float): Latitude of the destination point in degrees.
        to_long (float): Longitude of the destination point in degrees.

    Returns:
        float: The distance between the two points in kilometers.
    """
    # Convert latitudes and longitudes from degrees to radians
    from_lat_rad, from_long_rad, to_lat_rad, to_long_rad = map(radians,
    [from_lat, from_long, to_lat, to_long])

    dlon = to_long_rad - from_long_rad
    dlat = from_lat_rad - to_lat_rad
    a = sin(dlat / 2)**2 + cos(from_lat_rad) * cos(to_lat_rad) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    distance = EARTH_RADIUS_KM * c  # Correct Haversine formula
    return round(distance, 2) # Round to 2 decimal places for practical use


SHIPPING_PRICES = {
    "Ground": 1,
    "Priority": 1.6,
    "Overnight": 2.3,
}


def format_price(price: float) -> str:
    """
    Formats a numeric price into a string with a dollar sign and two decimal places.

    Args:
        price (float): The numeric price to format.

    Returns:
        str: The formatted price string (e.g., "$1.04").
    """
    return f"${price:.2f}"
