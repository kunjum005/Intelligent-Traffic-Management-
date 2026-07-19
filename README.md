# 🚦 Intelligent Traffic Management System Using AI

An AI-powered Intelligent Traffic Management System that analyzes traffic videos using **YOLOv8**, calculates traffic density, recommends optimal traffic signal timing, and generates AI-based traffic analysis using **Google Gemini AI**. The application is built with **Streamlit** for an interactive dashboard and **MySQL** for storing traffic reports.

---

## 📌 Project Overview

Traffic congestion is one of the major challenges in urban transportation. Conventional traffic signals operate on fixed timings and cannot adapt to real-time traffic conditions.

This project provides an intelligent solution by:

- Detecting vehicles from uploaded traffic videos.
- Calculating traffic density.
- Recommending optimal green signal duration.
- Generating AI-powered traffic analysis reports.
- Storing historical reports in a MySQL database.
- Displaying results through an interactive Streamlit dashboard.

---

## 🚀 Features

- 🚗 Real-time Vehicle Detection using YOLOv8
- 🎥 Traffic Video Processing using OpenCV
- 📊 Traffic Density Analysis
- 🚦 Intelligent Signal Time Recommendation
- 🤖 AI Traffic Analysis using Google Gemini
- 📈 Interactive Charts and Analytics
- 💾 MySQL Database Integration
- 🖥️ Streamlit Dashboard
- 📋 Historical Report Storage

---

## 🛠️ Technology Stack

| Technology | Purpose |
|------------|---------|
| Python | Programming Language |
| YOLOv8 | Vehicle Detection |
| OpenCV | Video Processing |
| Streamlit | Web Dashboard |
| Google Gemini AI | AI Traffic Report Generation |
| MySQL | Database |
| Plotly | Data Visualization |
| Pandas | Data Processing |
| Ultralytics | YOLO Framework |

---

## 📂 Project Structure

```text
intelligent-traffic-management/
│
├── dashboard.py
├── requirements.txt
├── README.md
├── .env
│
├── dataset/
│
├── models/
│   └── yolov8n.pt
│
├── modules/
│   ├── database.py
│   ├── detector.py
│   ├── video_processor.py
│   ├── vehicle_detector.py
│   ├── vehicle_counter.py
│   ├── report_generator.py
│   ├── dashboard_utils.py
│   ├── llm_service.py
│   ├── prompt_builder.py
│   ├── signal_controller.py
│   ├── traffic_density.py
│   └── video_writer.py
│
├── output/
│
└── temp/
```

---

# ⚙️ Installation

## 1. Clone the Repository

```bash
git clone https://github.com/kunjum005/intelligent-traffic-management.git

cd intelligent-traffic-management
```

---

## 2. Create Virtual Environment

### Windows

```bash
python -m venv venv
```

Activate the virtual environment:

```bash
venv\Scripts\activate
```

### macOS / Linux

```bash
python3 -m venv venv

source venv/bin/activate
```

---

## 3. Install Required Libraries

```bash
pip install -r requirements.txt
```

---

## 4. Install and Configure XAMPP

Install **XAMPP** and start:

- Apache
- MySQL

Create a MySQL database named:

```text
traffic_management
```

Import the required SQL table if provided.

---

## 5. Configure Google Gemini API

Create a file named:

```text
.env
```

Add your Gemini API key:

```env
GEMINI_API_KEY=YOUR_GEMINI_API_KEY
```

You can generate an API key from:

https://aistudio.google.com/app/apikey

---

## 6. Download YOLOv8 Model

Download the YOLOv8 Nano model:

```
yolov8n.pt
```

Place it inside:

```text
models/
```

---

## 7. Run the Application

```bash
streamlit run dashboard.py
```

The dashboard will open at:

```text
http://localhost:8501
```

---

# 📊 Workflow

```text
Upload Traffic Video
        │
        ▼
OpenCV Video Processing
        │
        ▼
Frame Extraction
        │
        ▼
YOLOv8 Vehicle Detection
        │
        ▼
Vehicle Counting
        │
        ▼
Traffic Density Analysis
        │
        ▼
Signal Time Recommendation
        │
        ▼
Generate AI Traffic Report
        │
        ▼
Store Report in MySQL
        │
        ▼
Display Results in Streamlit Dashboard
```

---

# 📸 Application Modules

### Vehicle Detection

Detects:

- Car
- Bus
- Truck
- Motorcycle

using the pre-trained YOLOv8 model.

---

### Video Processing

Uses OpenCV to:

- Read uploaded videos
- Extract frames
- Draw vehicle bounding boxes
- Generate processed videos

---

### Traffic Analysis

Calculates:

- Vehicle Count
- Average Vehicles
- Traffic Density
- Signal Timing

---

### AI Traffic Analysis

Google Gemini AI generates:

- Executive Summary
- Congestion Analysis
- Possible Causes
- Risk Assessment
- Signal Optimization
- Traffic Recommendations
- Expected Outcome

---

### Database

Stores:

- Video Name
- Vehicle Counts
- Traffic Density
- Signal Time
- Report History

---

# 📈 Dashboard

The Streamlit dashboard provides:

- Upload Traffic Video
- Original Video
- Processed Video
- Vehicle Statistics
- Traffic Analytics Charts
- AI Traffic Analysis
- Previous Traffic Reports

---

# Future Scope

- Live CCTV Integration
- Emergency Vehicle Detection
- Smart City Integration
- Traffic Prediction using Historical Data
- GPS-Based Traffic Analysis
- Mobile Application
- Cloud Deployment
- Multi-Camera Traffic Monitoring

---

# Dataset

Traffic videos used for testing can be downloaded from Kaggle:

https://www.kaggle.com/datasets/arshadrahmanziban/traffic-video-dataset

---

# Output

The system generates:

- Processed Traffic Video
- Vehicle Statistics
- Traffic Density
- Recommended Green Signal Time
- AI Traffic Report
- Historical Reports in MySQL

---

# Note

- This project uses a **pre-trained YOLOv8 model** for vehicle detection.
- The project performs **inference** on uploaded traffic videos and does **not train** the YOLO model.
- Google Gemini API is required for AI-generated traffic analysis.
- MySQL (XAMPP) must be running before starting the application.

---

# Author

**Kunjum Mittal**

B.Tech – Computer Science & Engineering (AI & ML)

---

# License

This project is developed for academic and educational purposes.
