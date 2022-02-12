# Volume-Hand-Control
It is my final project for the subject Computer Vision. This program will track your hands and their respective movements. It will also modify the volume of your PC depending on the distance between your thumb and index finger.

## Mediapipe

MediaPipe offers cross-platform, customizable ML solutions for live and streaming media.

You can click here and see Mediapipe's web : https://mediapipe.dev/

## OpenCv

OpenCV (Open Source Computer Vision Library) is an open source computer vision and machine learning software library. OpenCV was built to provide a common infrastructure for computer vision applications and to accelerate the use of machine perception in the commercial products. Being a BSD-licensed product, OpenCV makes it easy for businesses to utilize and modify the code.

## Pycaw

Python Core Audio Windows Library, working for both Python2 and Python3.

You can visit the github of it here : https://github.com/AndreMiras/pycaw

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install all three.

```bash
pip install mediapipe

pip install pycaw

pip install opencv-python
```

If installing opencv fails, here you hace a guide of them: https://github.com/opencv/opencv-python/blob/master/README.md

## Usage 
### Mediapipe

```python
import mediapipe as mp

mp_face_mesh = mp.solutions.face_mesh

```

### Pycaw

```python

from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(
    IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))
volume.GetMute()
volume.GetMasterVolumeLevel()
volume.GetVolumeRange()
volume.SetMasterVolumeLevel(-20.0, None)

```

### OpenCv

```python

import cv2

```

## Personal recommendation for easier installation:

-Use Pycharm as a programming environment.

-Create a new project.

-Include the files inside.

-Once the project is created, follow these steps:

-In Pycharm click on the top left on "File", then on Settings and you will see where it says "Project: *name of your project*".

-Click on "Pyhton interpreter", the same on the "+" button and look for each of the three mentioned libraries, mediapipe, opencv and pycaw, and click on install package.

Then you can check it has been installed correctly.

![alt text](https://github.com/JesusVillenRuiz/Volume-Hand-Control/blob/f9524098655f5ed15e866e5a8ebca153ea0ae597/Examples/HowToInstall.png?raw=true)

## Run the project

Just run the VolumeHandControlAdvance.py file.

## RESULTS

### Start Menu

![alt text](https://github.com/JesusVillenRuiz/Volume-Hand-Control/blob/f9524098655f5ed15e866e5a8ebca153ea0ae597/Examples/Inicio.png?raw=true) 

### Mouse mode

If you join your index finger and middle finger, a red circle will appear. This means that you are left clicking, simulating a mouse (Your hand is now a computer mouse!), if you put the red circle on top of any button, it will do its functionality.

![alt text](https://github.com/JesusVillenRuiz/Volume-Hand-Control/blob/f9524098655f5ed15e866e5a8ebca153ea0ae597/Examples/MouseMode.png?raw=true) 

### Control the volume of your PC without buttons!

If you lower the last three fingers of your hand a green circle will appear between your thumb and index finger. Now you are modifying the volume of your computer based on the distance between these fingers.

You can adjust the volume without lowering your fingers and simply lower them to set it.

![alt text](https://github.com/JesusVillenRuiz/Volume-Hand-Control/blob/f9524098655f5ed15e866e5a8ebca153ea0ae597/Examples/VolumeControl.png?raw=true) 


