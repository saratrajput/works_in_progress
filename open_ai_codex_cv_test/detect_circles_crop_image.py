"""
Start webcam and turn image to grayscale.
"""
import cv2
import numpy as np


cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # Crop image to 300x300
    crop_img = gray[0:300, 0:300]
    # Find circles in the image
    circles = cv2.HoughCircles(crop_img, cv2.HOUGH_GRADIENT, 1, 20, param1=50, param2=30, minRadius=0, maxRadius=0)
    # Draw circles
    if circles is not None:
        circles = np.uint16(np.around(circles))
        for i in circles[0, :]:
            # Draw outer circle
            cv2.circle(crop_img, (i[0], i[1]), i[2], (0, 255, 0), 2)
            # Draw inner circle
            cv2.circle(crop_img, (i[0], i[1]), 2, (0, 0, 255), 3)
    # Show image
    cv2.imshow('frame', crop_img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()