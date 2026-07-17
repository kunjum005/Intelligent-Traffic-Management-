"""
app.py

Main application for Intelligent Traffic Management System.
"""

from modules.detector import load_model
from modules.video_processor import open_video
from modules.report_generator import generate_report
from modules.database import save_report


def main():

    print("=" * 50)
    print(" Intelligent Traffic Management System ")
    print("=" * 50)

    # -----------------------------
    # Load YOLO Model
    # -----------------------------
    print("\nLoading YOLO model...")
    model = load_model()

    # -----------------------------
    # Open Video
    # -----------------------------
    video_path = "dataset/Talaimari/east.mp4"

    print("Opening video...")
    cap = open_video(video_path)

    # -----------------------------
    # Analyze Video
    # -----------------------------
    print("Analyzing video...")

    report = generate_report(
        model=model,
        cap=cap,
        output_path="output/east_processed.mp4",
        frame_skip=10
    )

    # -----------------------------
    # Display Report
    # -----------------------------
    print("\n========== FINAL REPORT ==========\n")

    for vehicle, count in report["counts"].items():
        print(f"{vehicle:<15}: {count}")

    print("----------------------------------")
    print(f"Average Vehicles : {report['total']}")
    print(f"Traffic Density  : {report['density']}")
    print(f"Green Signal     : {report['signal_time']} sec")

    # -----------------------------
    # Save in Database
    # -----------------------------
    save_report(
        location="Talaimari East",
        video_name="east.mp4",
        counts=report["counts"],
        total=report["total"],
        density=report["density"],
        signal_time=report["signal_time"]
    )

    print("\nProcessed video saved in:")
    print("output/east_processed.mp4")

    print("\nDatabase updated successfully.")


if __name__ == "__main__":
    main()