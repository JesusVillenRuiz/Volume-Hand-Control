import cv2
import time
import numpy as np
import HandTrackingModule as htm

from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

#########################################
wCam, hCam = 720, 140
#########################################


cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
# cv2.namedWindow("Img", cv2.WND_PROP_FULLSCREEN)
# cv2.setWindowProperty("Img", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
cap.set(3, wCam)
cap.set(4, hCam)
pTime = 0
detector = htm.handDetector(detectionCon=0.7, maxHands=1)
start = False

devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(
    IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))
# volume.GetMute()
# volume.GetMasterVolumeLevel()
volRange = volume.GetVolumeRange()
minVol = volRange[0]
maxVol = volRange[1]
vol = 0
volBar = 400
volPer = 0
area = 0
colorVol = (255, 0, 0)
xs, ys = 0, 0
puls = 40

while True:
    success, img = cap.read()

    # Find Hand
    img = cv2.flip(img, 1)
    img = detector.findHands(img)
    apagar = cv2.imread("apagarcuad.png")
    img[290:350, 500:563] = apagar
    lmList, bbox = detector.findPosition(img, draw=True)
    if len(lmList) != 0:

        # Filter based on size
        area = (bbox[2] - bbox[0]) * (bbox[3] - bbox[1]) // 100
        # print(area)
        if 200 < area < 1000:

            # Find Distance between index and Thumb
            length, img, lineInfo = detector.findDistance(4, 8, img)
            puls, _, li = detector.findDistance(8, 12, img)
            xs, ys = li[4], li[5]
            if puls < 40:
                cv2.circle(img, (li[4], li[5]), 10, (0, 0, 255), cv2.FILLED)

            print(length)

            # Convert Volume
            volBar = np.interp(length, [50, 200], [400, 150])
            volPer = np.interp(length, [50, 200], [0, 100])

            # Reduce resolution to make it smoother
            smoothness = 5
            volPer = smoothness * round(volPer / smoothness)
            # Check fingers up
            fingers = detector.fingersUp()
            # print(fingers)

            # If pinky is down set volume
            if not fingers[4] and not fingers[3] and not fingers[2] and start:
                volume.SetMasterVolumeLevelScalar(volPer / 100, None)
                # h,w,_ = img.shape
                # print(h,w)
                # img = img[100:int(h-volPer/50), 200:int(w-volPer/50)]
                # img = htm.zoom(img, (volPer/50)+1)
                # img = cv2.resize(img, dsize=None, fx=(volPer/50)+1, fy=(volPer/50)+1)
                cv2.circle(img, (lineInfo[4], lineInfo[5]), 10, (0, 255, 0), cv2.FILLED)
                colorVol = (0, 255, 0)
            else:
                colorVol = (255, 0, 0)

    if not start:
        cv2.rectangle(img, (450, 400), (195, 360), (100, 200, 5), cv2.FILLED)
        cv2.putText(img, f'S  T  A  R  T', (205, 390), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)

        if (450 > xs > 195) and (400 > ys > 360) and puls < 40:
            start = True

    if start:
        # Drawings
        cv2.rectangle(img, (50, 150), (85, 400), (255, 0, 0), 3)
        cv2.rectangle(img, (50, int(volBar)), (85, 400), (255, 0, 0), cv2.FILLED)
        cv2.putText(img, f'{int(volPer)}%', (40, 450), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 0), 2)
        cVol = int(volume.GetMasterVolumeLevelScalar() * 100)
        cv2.putText(img, f'Vol Set: {int(cVol)}', (410, 50), cv2.FONT_HERSHEY_COMPLEX, 1, colorVol, 2)
        cv2.rectangle(img, (410, 40), (200, 80), (50, 0, 205), cv2.FILLED)
        cv2.putText(img, f'S  T  O  P', (215, 70), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)
        if (410 > xs > 200) and (80 > ys > 40) and puls < 40:
            start = False

    if (555 > xs > 505) and (345 > ys > 295) and puls < 40:
        exit()

    # Frame rate
    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime

    cv2.putText(img, f'FPS: {int(fps)}', (40, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 0), 2)

    cv2.imshow("Img", img)
    cv2.waitKey(1)
