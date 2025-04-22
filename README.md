# ImageSegmenter - Thresholding Example

A Python application that demonstrates image thresholding using OpenCV.

## Overview
------------

Image thresholding is a fundamental operation in computer vision that separates the foreground from the background of an image based on pixel intensity values. This application provides a simple example of how to apply thresholding using OpenCV, with the capability to display and save the resulting image.

## Key Features
----------------

*   Reads an input image file in BGR format and converts it to grayscale.
*   Applies binary thresholding using a specified threshold value (default: 127).
*   Displays the original and thresholded images.
*   Saves the thresholded image to a new file.

## Prerequisites
----------------

*   Python 3.8+
*   OpenCV 4.x
*   NumPy

## Installation
---------------

To run this application, follow these steps:

1.  Install the required libraries using pip:
   
```bash
pip install opencv-python numpy
```

2.  Clone the repository or copy the code into a new file.
3.  Run the application using python:
```bash
python image_thresholding.py
```

## Usage
---------

1.  Upload an input image file using the Streamlit app.
2.  Adjust the threshold value (default: 127) as needed.
3.  Click "Apply Threshold" to separate the foreground from the background.
4.  View and save the resulting thresholded image.

