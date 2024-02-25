# Live-Color-Detection-using-OpenCV

This project demonstrates live color detection using OpenCV, a popular computer vision library. It allows you to detect and track specific colors in real-time video streams from your webcam. The color detection process involves setting upper and lower thresholds for the HSV (Hue, Saturation, Value) color space.

## Installation
To run this project, ensure you have Python installed on your system along with the following dependencies:
OpenCV, NumPy

## Running
Adjust the trackbars to set the upper and lower thresholds for the color you want to detect.

Hold the object of the desired color in front of your webcam, and you will see the color being detected and highlighted in real-time.

## Code Explanation
The script color_detection.py performs the following steps:

-Initializes trackbars for adjusting upper and lower HSV values. <br>
-Captures live video from the webcam. <br>
-Converts each frame to the HSV color space. <br>
-Applies a mask to isolate the desired color. <br>
-Performs morphological operations for noise reduction. <br>
-Displays the original frame, mask, and result showing only the detected color.
