import cv2
import time
from ultralytics import YOLO
from datetime import datetime

# Load trained model
model = YOLO("./runs/detect/train4/weights/best.pt")

# Open webcam
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

    # Show live camera feed
    cv2.imshow("Smart Fridge Camera", frame)

    # Wait for key press
    key = cv2.waitKey(1) & 0xFF

    # --- Press 'c' to capture a photo ---
    if key == ord('c'):
        # Save photo with timestamp
        filename = f"fridge_{datetime.now().strftime('%Y%m%d_%H%M%S')}.jpg"
        cv2.imwrite(filename, frame)
        print(f"📸 Photo saved as {filename}")

        # Run YOLO detection on saved photo
        results = model.predict(source=filename, conf=0.10, save=True)
        count = len(results[0].boxes)
        print(f"🥛 Milk packets detected: {count}")

        # Optional: if less than 2, trigger alert
        if count < 2:
            print("⚠️ Milk is running low! Send message to vendor.")

    # --- Press 'q' to quit ---
    elif key == ord('q'):
        print("👋 Closing camera...")
        break

cap.release()
cv2.destroyAllWindows()
