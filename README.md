Frame capture
# First edition
## Overview

Given a set up webcam, the program can open the camera, capture the frames and store the frames as jpg file in a folder.

## Open Source Model
Python Library: Opencv 

OpenCV download:  pip3 install opencv-python or pip install opencv-python

## Design

The project is written in python file.

## Procedure:

            1.Use cv2.VideoCapture()to get a video capture object for the camera. 

            2.Set up infinite while loop and use the read() method  to read the frames
               using the above created object.

            3.Use cv2.imshow() method to show the frames in the video.

            4. Save each frame using cv2.imwrite()

            4. Use time.sleep() method to suspend execution for the given number of seconds.

            5. Break the loop when the users clicks a specific key.

            6.Release the VideoCapture and destroy all the windows.      



### Important file

framecapture.py

### Report

The first edition is doing OK when the light is sufficient and people are at a normal distance from the camera.

### Need Update

The project is only the first edition. I will keep update.
