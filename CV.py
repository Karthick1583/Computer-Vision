import cv2
import cvzone
from cvzone.HandTrackingModule import HandDetector
import pyautogui as auto
import time

cap = cv2.VideoCapture(0)

hd = HandDetector(maxHands=1, detectionCon=0.7)
while True:  # Use 'True' instead of '1' for an infinite loop
    ret, frame = cap.read()
    
    if not ret:  # Check if the frame is empty
        continue  # Skip the rest of the loop if the frame is empty
    
    frame = cv2.resize(frame, (1080, 720))
    hand, frame = hd.findHands(frame)
    cv2.imshow("frame", frame)
    
    if cv2.waitKey(1) == 27:  # Exit the loop if the 'Esc' key is pressed (ASCII code 27)
        break

cap.release()  # Release the video capture object
cv2.destroyAllWindows()  # Close all OpenCV windows
