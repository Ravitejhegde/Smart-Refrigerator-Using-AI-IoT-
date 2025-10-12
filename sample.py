print("My AI project starts here!")
import cv2
from ultralytics import YOLO

cam = cv2.VideoCapture(0)
ret, frame = cam.read()

if ret:
    cv2.imwrite("milk_test.jpg", frame)
    print("Photo saved as milk_test.jpg")

cam.release()


