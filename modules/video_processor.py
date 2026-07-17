"""
video_processor.py

This module reads a traffic video using OpenCV.
"""

from pathlib import Path
import cv2


def open_video(video_path):
    """
    Opens a video file.

    Args:
        video_path (str or Path): Path of the video

    Returns:
        cv2.VideoCapture object
    """

    video_path = Path(video_path)

    if not video_path.exists():
        raise FileNotFoundError(f"Video not found:\n{video_path}")

    cap = cv2.VideoCapture(str(video_path))

    if not cap.isOpened():
        raise ValueError("Unable to open the video.")

    return cap