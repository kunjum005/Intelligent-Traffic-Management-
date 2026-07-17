"""
detector.py

This module loads the YOLOv8 Nano model.
If the model is not already downloaded, Ultralytics will download it automatically.
"""

from ultralytics import YOLO


def load_model():
    """
    Load the YOLOv8 Nano model.

    Returns:
        YOLO: Loaded YOLO model
    """
    model = YOLO("yolov8n.pt")
    return model