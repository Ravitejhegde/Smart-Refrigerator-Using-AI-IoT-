# 🧊 Smart Refrigerator Monitoring System

> An AI & IoT-based Smart Refrigerator system that automatically detects milk packets, monitors inventory, and alerts when stock is running low.

![Python](https://img.shields.io/badge/Python-3.x-blue)
![YOLOv8](https://img.shields.io/badge/YOLOv8-Ultralytics-red)
![OpenCV](https://img.shields.io/badge/OpenCV-Computer%20Vision-green)
![License](https://img.shields.io/badge/License-MIT-yellow)

---

# 📖 Overview

The Smart Refrigerator Monitoring System is an AI-powered inventory management solution that uses computer vision to detect and count milk packets inside a refrigerator.

The system continuously analyzes images from a camera, tracks the available stock, and automatically generates alerts whenever the inventory falls below a predefined threshold.

This project demonstrates the integration of Artificial Intelligence, Computer Vision, and IoT concepts for smart home and smart retail applications.

---

# ✨ Features

- 🥛 Automatic Milk Packet Detection
- 🤖 YOLOv8 Object Detection
- 📷 Camera/Image Processing
- 🔢 Real-Time Packet Counting
- ⚠ Low Stock Alert System
- 📊 Inventory Monitoring
- 📈 Detection Confidence Display
- 🧠 AI-Based Recognition
- 🖥 User-Friendly Interface
- 🔄 Continuous Monitoring

---

# 🎯 Objectives

- Automate refrigerator inventory monitoring.
- Reduce manual stock checking.
- Detect milk packets using AI.
- Count available packets accurately.
- Notify users when stock is low.
- Demonstrate AI + IoT integration.

---

# 🛠 Tech Stack

## Programming Language

- Python

## AI & Machine Learning

- YOLOv8 (Ultralytics)

## Computer Vision

- OpenCV
- Pillow

## Deep Learning

- PyTorch

## Supporting Libraries

- NumPy
- Matplotlib
- EasyOCR *(Optional for text recognition)*

---

# 🏗 System Architecture

```
                Camera

                  │
                  ▼

        Capture Refrigerator Image

                  │
                  ▼

           YOLOv8 Detection

                  │
                  ▼

        Detect Milk Packets

                  │
                  ▼

          Count Total Packets

                  │
        ┌─────────┴─────────┐
        │                   │
        ▼                   ▼

   Stock Available      Low Stock

        │                   │
        ▼                   ▼

 Display Count       Send Alert
```

---

# 📂 Project Structure

```
Smart-Refrigerator/

│

├── dataset/
│   ├── train/
│   ├── valid/
│   └── data.yaml
│
├── models/
│
├── runs/
│
├── images/
│
├── train.py
├── predict.py
├── milk_counter.py
├── requirements.txt
└── README.md
```

---

# 🚀 Installation

## Clone Repository

```bash
git clone https://github.com/yourusername/smart-refrigerator.git

cd smart-refrigerator
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# ▶ Train YOLO Model

```bash
python train.py
```

---

# 🔍 Run Detection

```bash
python predict.py
```

---

# 📦 Required Libraries

```text
ultralytics
opencv-python
torch
numpy
matplotlib
Pillow
easyocr
```

Install manually:

```bash
pip install ultralytics opencv-python torch numpy matplotlib Pillow easyocr
```

---

# 📊 Workflow

```
Capture Image
      │
      ▼
Preprocessing
      │
      ▼
YOLOv8 Detection
      │
      ▼
Milk Packet Count
      │
      ▼
Inventory Check
      │
      ▼
Generate Alert
```

---

# 📈 Future Enhancements

- 📹 Live Camera Monitoring
- 🌐 IoT Cloud Integration
- 📱 Mobile Application
- 🔔 SMS / Email Notifications
- 📊 Dashboard Analytics
- 🛒 Automatic Grocery Ordering
- 🥚 Detection of Multiple Grocery Items
- ☁ Cloud Deployment
- 📡 Remote Monitoring

---

# 🎯 Applications

- Smart Homes
- Dairy Management
- Grocery Stores
- Supermarkets
- Cold Storage Monitoring
- Retail Inventory Management
- Smart Kitchens

---

# 📸 Sample Output

```
Milk Packets Detected : 5

Confidence Scores

Milk : 98%
Milk : 97%
Milk : 96%
Milk : 95%
Milk : 93%

Inventory Status

✅ Stock Available
```

If the number of packets falls below the threshold:

```
Milk Packets Detected : 1

⚠ LOW STOCK ALERT

Please refill the refrigerator.
```

---

# 📚 Learning Outcomes

- Object Detection using YOLOv8
- Computer Vision with OpenCV
- AI Model Training
- Dataset Annotation
- Image Processing
- Inventory Automation
- AI + IoT Integration

---

# 📄 License

This project is licensed under the MIT License.

---

# 👨‍💻 Author

**Raviteja Hegde**

MCA Project • AI & IoT Enthusiast

---

## ⭐ If you found this project useful, consider giving it a Star!
