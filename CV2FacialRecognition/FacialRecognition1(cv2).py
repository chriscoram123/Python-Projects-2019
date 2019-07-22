# START...cv2 intigrated jpg facial comparison
# Imports for script
import cv2
import numpy as np

# Variables 
cap = cv2.VideoCapture(0)


# While true, imshow will stay open in loop creating constant frame operation
while(True):
   # Capture frame-by-frame
   ret, frame = cap.read()

   # Display the resulting frame
   cv2.imshow('frame',frame)
   if cv2.waitKey(20) & 0xFF == ord('q'):
     break

# Functions will activate to complete script actions
cap.release()
cv2.destroyAllWindows()
