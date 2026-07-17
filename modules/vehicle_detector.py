"""
vehicle_detector.py

Detects and filters only vehicles.
"""

VEHICLE_CLASSES = {
    2: "Car",
    3: "Motorcycle",
    5: "Bus",
    7: "Truck"
}


def detect_vehicles(model, frame):
    """
    Run YOLO detection on a single frame.
    """

    # verbose=False stops YOLO from printing
    # detection details for every frame.
    results = model(frame, verbose=False)

    return results


def get_vehicle_boxes(results):
    """
    Return only vehicle detections.
    """

    vehicle_boxes = []

    for box in results[0].boxes:

        class_id = int(box.cls[0])

        if class_id in VEHICLE_CLASSES:

            vehicle_boxes.append(box)

    return vehicle_boxes


def get_vehicle_name(class_id):
    """
    Convert class ID to vehicle name.
    """

    return VEHICLE_CLASSES.get(class_id, "Unknown")