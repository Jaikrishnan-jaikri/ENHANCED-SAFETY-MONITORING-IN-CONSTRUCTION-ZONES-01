# ENHANCED-SAFETY-MONITORING-IN-CONSTRUCTION-ZONES-01


This project provides an AI-powered solution for real-time safety monitoring in construction zones. It detects safety gear violations (PPE compliance), danger zone breaches, and notifies supervisors through visual dashboards and SMS alerts.

📊 Features

Real-time detection of:

No Hardhat

No Mask

No Safety Vest

Danger Zone Intrusion

DeepSORT-based person tracking

CLAHE-enhanced video processing for better accuracy

SMS alert system via Twilio

Web dashboard for detection log viewing

Violation summary with tracked counts per frame

🚀 Getting Started

Prerequisites

Python 3.8+

Django

OpenCV

Ultralytics YOLO

DeepSORT (deep_sort_realtime)

Twilio

Installation

Clone the repository:

git clone https://github.com/your-username/construction-safety-monitoring.git
cd construction-safety-monitoring

Create virtual environment and install dependencies:

python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate
pip install -r requirements.txt

Run migrations:

python manage.py makemigrations
python manage.py migrate

Start the development server:

python manage.py runserver

🚧 Model Weights

Due to file size, the YOLOv11s model (best.pt) is not included.
Download it from Google Drive and place it inside the APP/ folder.

🔧 How It Works

Web camera feed is processed in real-time.

CLAHE enhances frame contrast.

YOLO detects objects; DeepSORT assigns consistent IDs.

If a person is detected in the danger zone or violates PPE rules, a log is saved with:

Frame number

Track ID

Violation type

Timestamp

Person count

SMS is sent via Twilio if alerts are enabled.

🌟 Violation Summary Fields

Total persons tracked

No Mask

No Hardhat

No Safety Vest

Danger Zone Intrusions


Collaborators (if any)

🔧 Future Enhancements

Crowd density monitoring

Posture-based fatigue detection

Tool and material misuse detection

Attendance with PPE compliance

Centralized cloud dashboard

🌟 Accuracy

Model accuracy: 87.2% (YOLOv11s variant chosen after testing multiple models)
