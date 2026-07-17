"""
traffic_density.py

Determines traffic density based on
the total number of detected vehicles.
"""


def get_traffic_density(total_vehicles):
    """
    Determine traffic density.

    Args:
        total_vehicles (int)

    Returns:
        str
    """

    if total_vehicles <= 5:
        return "LOW"

    elif total_vehicles <= 15:
        return "MEDIUM"

    else:
        return "HIGH"