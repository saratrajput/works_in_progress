"""
Start webcam and turn image to grayscale.
"""
import cv2
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # Detect contours in the image
    contours, hierarchy = cv2.findContours(gray, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    # Draw the contours on the image
    cv2.drawContours(frame, contours, -1, (0, 255, 0), 2)
    # Display the image
    cv2.imshow('frame', frame)
    # Exit when escape is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the capture
cap.release()
cv2.destroyAllWindows()