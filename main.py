import cv2
import os
width = 1280
height = 720
folderPath = "Slides"

cap = cv2.VideoCapture(0)
cap.set(3, 640)  # Set width
cap.set(4, 480)  # Set height

pathImages = sorted(os.listdir(folderPath), key=len)
print(pathImages)

imgNumber = 0

while True:
  success, img =cap.read()
  pathFullImage = os.path.join(folderPath,pathImages[imgNumber])
  imgCurrent = cv2.imread(pathFullImage)
  
  cv2.imshow("Image", img)
  cv2.imshow("Presentation", imgCurrent)
  key = cv2.waitKey(1)
  if key == ord('q'):
    break