import cv2
import numpy as np

cap = cv2.VideoCapture("videos/vid1.mp4")
new_width = 600
new_height = 600
while True:
    ret, frame = cap.read()
    frame = cv2.resize(frame, (new_width,new_height))
    if not ret:
        break
    else:
        cv2.imshow("window", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
cap.release()
cv2.destroyAllWindows()