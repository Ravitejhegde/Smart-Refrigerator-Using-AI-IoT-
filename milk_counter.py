import cv2
from ultralytics import YOLO
from datetime import datetime
import smtplib
from email.mime.text import MIMEText
import easyocr

# ----------------------------
# Email Alert Function
# ----------------------------
def send_email_alert(count, text_details):
    sender = "hegderaviteja4@gmail.com"
    receiver = "hegderaviteja4@gmail.com"
    password = "zmxa gekj kjcp gwyo"  # Gmail app password

    subject = "Smart Fridge Alert 🚨"
    body = f"""
Milk packets detected: {count}

Detected text from packets:
{text_details}

⚠ Milk is running low! Please refill.
"""

    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = sender
    msg["To"] = receiver

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(sender, password)
            server.sendmail(sender, receiver, msg.as_string())
        print("📧 Alert email sent successfully!")
    except Exception as e:
        print(f"❌ Error sending email: {e}")

# ----------------------------
# Load YOLO & OCR Models
# ----------------------------
model = YOLO("./runs/detect/train2/weights/best.pt")
reader = easyocr.Reader(['en'], gpu=False)  # OCR for English

# ----------------------------
# Open Webcam
# ----------------------------
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("❌ Camera not detected")
    exit()

print("✅ Camera started. Press 'c' to capture photo, 'q' to quit.")

while True:
    ret, frame = cap.read()
    if not ret:
        print("❌ Failed to grab frame")
        break

    cv2.imshow("Smart Fridge Camera", frame)
    key = cv2.waitKey(1) & 0xFF

    # --- Capture Photo ---
    if key == ord('c'):
        filename = f"fridge_{datetime.now().strftime('%Y%m%d_%H%M%S')}.jpg"
        cv2.imwrite(filename, frame)
        print(f"📸 Photo saved as {filename}")

        # YOLO Detection
        results = model.predict(source=filename, conf=0.05, save=True)
        count = len(results[0].boxes)
        print(f"🥛 Milk packets detected: {count}")

        text_summary = ""

        if count > 0:
            img = cv2.imread(filename)
            for i, box in enumerate(results[0].boxes.xyxy):
                x1, y1, x2, y2 = map(int, box[:4])
                crop = img[y1:y2, x1:x2]

                # OCR Reading
                detected_text = reader.readtext(crop)
                texts = [t[1] for t in detected_text]
                joined_text = " ".join(texts)
                text_summary += f"\nPacket {i+1}: {joined_text}"
                print(f"🧾 Packet {i+1} text: {joined_text}")

        else:
            text_summary = "No packets found."

        # Send alert if milk is low
        if count < 2:
            print("⚠ Milk is running low! Sending alert with OCR details...")
            send_email_alert(count, text_summary)

    elif key == ord('q'):
        print("👋 Closing camera...")
        break

cap.release()
cv2.destroyAllWindows()
