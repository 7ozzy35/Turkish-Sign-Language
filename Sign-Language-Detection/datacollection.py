#Dataset oluşturma

import cv2
from cvzone.HandTrackingModule import HandDetector
import numpy as np
import math
import time

cap = cv2.VideoCapture(0)
detector = HandDetector(maxHands=2) # İki el algılama
offset = 20
imgSize = 500
counter = 0

folder = "Sign-Language-Detection\Data\Konusmak"  # Oluşturulan resmin dosya yolu

# El kırpma
while True:
    success, img = cap.read()
    hands, img = detector.findHands(img)
    if hands:
        for hand in hands:  # Her el için ayrı işlem yap
            x, y, w, h = hand['bbox']

            imgWhite = np.ones((imgSize, imgSize, 3), np.uint8) * 255

            imgCrop = img[y - offset:y + h + offset, x - offset:x + w + offset]
            imgCropShape = imgCrop.shape

            aspectRatio = h / w

            if aspectRatio > 1:
                k = imgSize / h
                wCal = math.ceil(k * w)
                imgResize = cv2.resize(imgCrop, (wCal, imgSize))
                imgResizeShape = imgResize.shape
                wGap = math.ceil((imgSize - wCal) / 2)
                imgWhite[:, wGap: wCal + wGap] = imgResize

            else:
                k = imgSize / w
                hCal = math.ceil(k * h)
                imgResize = cv2.resize(imgCrop, (imgSize, hCal))
                imgResizeShape = imgResize.shape
                hGap = math.ceil((imgSize - hCal))
                imgWhite[hGap: hCal + hGap, :] = imgResize

            cv2.imshow('ImageWhite', imgWhite)

            # Resim kaydetme
            if cv2.waitKey(1) & 0xFF == ord('s'):
                counter += 1
                cv2.imwrite(f'{folder}/Image_{counter}_{time.time()}.jpg', imgWhite)
                print(f"Image_{counter} saved.")

    cv2.imshow('Image', img)
    key = cv2.waitKey(1)
    
    # Çıkış
    if key == ord("q"):
        break
