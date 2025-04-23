# Image Thresholding Tool: Segment Foreground from Background

## Overview

Image thresholding is a fundamental operation in computer vision that separates the foreground from the background of an image based on pixel intensity values. This application demonstrates this process using both a traditional OpenCV script and a Streamlit web app, providing flexibility for different use cases.

## Key Features (Both Implementations)
----------------

*   Reads an input image file in BGR format.
*   Converts the image to grayscale.
*   Applies binary thresholding using a specified threshold value (default: 127).
*   Displays the original and thresholded images.
*   Saves the thresholded image to a new file.

## Prerequisites
----------------

*   Python 3.8+
*   OpenCV 4.x
*   NumPy
*   Streamlit

## Installation & Running (OpenCV Script)
---------------

To run the traditional OpenCV script:

1.  Install the required libraries using pip:
    ```bash
    pip install opencv-python numpy
    ```
2.  Clone the repository or copy the code into a new file (e.g., `image_thresholding.py`).
3.  Run the application using python:
    ```bash
    python image_thresholding.py
    ```

## Installation & Running (Streamlit App)
---------------

To run the Streamlit web app:

1. Clone this repository to your local machine:
    ```sh
    git clone https://github.com/yourusername/image-thresholding-tool.git
    cd image-thresholding-tool
    ```

2. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```

3. Start the Streamlit app by running:
    ```sh
    streamlit run app.py
    ```

4. Open your web browser and go to `http://localhost:8501` to see the app in action.


## Usage (Streamlit App)

1.  Upload an input image file using the Streamlit app.
2.  Adjust the threshold value (default: 127) as needed via the slider.
3.  Click "Apply Threshold" to separate the foreground from the background.
4.  View and save the resulting thresholded image.

## Dependencies

- **Streamlit**: The web framework used to build the app.
- **OpenCV-Python**: For image processing tasks like converting images to grayscale and applying thresholding.
- **Numpy**: For handling numerical operations on arrays, though it's not strictly necessary for this specific task, it's often useful in other OpenCV operations.
```
