"""
report_generator.py

Generates the complete traffic report
from an input video.
"""

import cv2

from modules.vehicle_detector import (
    detect_vehicles,
    get_vehicle_boxes
)

from modules.vehicle_counter import count_vehicles

from modules.traffic_density import get_traffic_density

from modules.signal_controller import get_signal_time

from modules.video_writer import draw_detections


def generate_report(
    model,
    cap,
    output_path,
    frame_skip=10
):
    """
    Analyze the video and generate a report.
    """

    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = cap.get(cv2.CAP_PROP_FPS)

    fourcc = cv2.VideoWriter_fourcc(*"avc1")

    out = cv2.VideoWriter(
        output_path,
        fourcc,
        fps,
        (width, height)
    )
    
    print("Output path:", output_path)
    print("VideoWriter opened:", out.isOpened())

    total_counts = {
        "Car": 0,
        "Motorcycle": 0,
        "Bus": 0,
        "Truck": 0
    }

    processed_frames = 0
    frame_number = 0

    # Store last detections
    last_vehicle_boxes = []

    while True:

        success, frame = cap.read()

        if not success:
            break

        frame_number += 1

        # Run YOLO every Nth frame
        if frame_number % frame_skip == 0:

            processed_frames += 1

            results = detect_vehicles(model, frame)

            last_vehicle_boxes = get_vehicle_boxes(results)

            counts = count_vehicles(last_vehicle_boxes)

            for vehicle in total_counts:
                total_counts[vehicle] += counts[vehicle]

            if processed_frames % 20 == 0:
                print(f"Processed {processed_frames} frames")

        # Draw previous detections on every frame
        frame = draw_detections(
            frame,
            last_vehicle_boxes
        )

        # Write every frame
        out.write(frame)

    cap.release()
    out.release()

    if processed_frames == 0:
        processed_frames = 1

    average_counts = {}

    for vehicle in total_counts:

        average_counts[vehicle] = round(
            total_counts[vehicle] / processed_frames,
            2
        )

    average_total = round(
        sum(average_counts.values()),
        2
    )

    final_density = get_traffic_density(
        round(average_total)
    )

    final_signal = get_signal_time(
        final_density
    )

    report = {
        "location": "Uploaded Video",

        "counts": average_counts,

        "total": average_total,

        "density": final_density,

        "signal_time": final_signal

    }

    return report