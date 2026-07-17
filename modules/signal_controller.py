"""
signal_controller.py

Recommend green signal timing
based on traffic density.
"""


def get_signal_time(traffic_density):
    """
    Recommend signal time.

    Args:
        traffic_density (str)

    Returns:
        int
    """

    signal_time = {
        "LOW": 20,
        "MEDIUM": 40,
        "HIGH": 60
    }

    return signal_time.get(traffic_density, 20)