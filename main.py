import cv2
import numpy as np

cap = cv2.VideoCapture("videos/vid1.mp4")
new_width = 480
new_height = 480
while True:
    ret, frame = cap.read()
    frame = cv2.resize(frame, (new_width,new_height))
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gaussian = cv2.GaussianBlur(gray, (5,5), 0)
    canny = cv2.Canny(gray, 150, 100)
    ret, thresh = cv2.threshold(canny, 100, 255, cv2.THRESH_BINARY)
    if not ret:
        break
    else:
        cv2.imshow("window", )
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
cap.release()
cv2.destroyAllWindows()