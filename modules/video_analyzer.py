"""
video_analyzer.py

Analyze an entire traffic video.
"""

from modules.vehicle_detector import detect_vehicles, get_vehicle_boxes
from modules.vehicle_counter import count_vehicles


def analyze_video(model, cap, frame_skip=100, max_frames=300):
    """
    Analyze a traffic video.

    Args:
        model : Loaded YOLO model
        cap : OpenCV VideoCapture object
        frame_skip : Process every Nth frame
        max_frames : Maximum frames to read

    Returns:
        Dictionary containing average vehicle counts.
    """

    total_counts = {
        "Car": 0,
        "Motorcycle": 0,
        "Bus": 0,
        "Truck": 0
    }

    processed_frames = 0
    frame_number = 0

    while True:

        success, frame = cap.read()

        if not success:
            print("\nEnd of video reached.")
            break

        frame_number += 1

        # Stop after reading max_frames
        if frame_number > max_frames:
            print(f"\nStopped after {max_frames} frames.")
            break

        # Show progress every 50 frames
        if frame_number % 50 == 0:
            print(f"Reading Frame: {frame_number}")

        # Skip frames
        if frame_number % frame_skip != 0:
            continue

        processed_frames += 1

        results = detect_vehicles(model, frame)

        vehicle_boxes = get_vehicle_boxes(results)

        counts = count_vehicles(vehicle_boxes)
        print(f"\nFrame {frame_number}")

        for vehicle, count in counts.items():
            print(f"{vehicle:<12}: {count}")

        for vehicle in total_counts:
            total_counts[vehicle] += counts[vehicle]

    average_counts = {}

    for vehicle in total_counts:

        if processed_frames == 0:
            average_counts[vehicle] = 0

        else:
            average_counts[vehicle] = round(
                total_counts[vehicle] / processed_frames,
                2
            )

    return average_counts