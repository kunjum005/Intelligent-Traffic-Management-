"""
vehicle_counter.py

Counts detected vehicles.
"""

from modules.vehicle_detector import get_vehicle_name


def count_vehicles(vehicle_boxes):
    """
    Count each type of detected vehicle.

    Args:
        vehicle_boxes : List of vehicle detections

    Returns:
        Dictionary containing vehicle counts.
    """

    vehicle_count = {
        "Car": 0,
        "Motorcycle": 0,
        "Bus": 0,
        "Truck": 0
    }

    for box in vehicle_boxes:

        class_id = int(box.cls[0])

        vehicle_name = get_vehicle_name(class_id)

        vehicle_count[vehicle_name] += 1

    return vehicle_count