"""
video_writer.py

Functions for drawing vehicle detections.
"""

import cv2

from modules.vehicle_detector import get_vehicle_name


def draw_detections(frame, vehicle_boxes):
    """
    Draw bounding boxes and labels.
    """

    for box in vehicle_boxes:

        x1, y1, x2, y2 = map(int, box.xyxy[0])

        class_id = int(box.cls[0])

        confidence = float(box.conf[0])

        vehicle_name = get_vehicle_name(class_id)

        label = f"{vehicle_name} {confidence:.2f}"

        cv2.rectangle(
            frame,
            (x1, y1),
            (x2, y2),
            (0, 255, 0),
            2
        )

        cv2.putText(
            frame,
            label,
            (x1, y1 - 10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.6,
            (0, 255, 0),
            2
        )

    return frame