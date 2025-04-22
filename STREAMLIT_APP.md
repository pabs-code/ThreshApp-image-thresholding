# Image Thresholding Tool: Segment Foreground from Background

## Overview

This is a web-based application built with **Streamlit** that allows users to upload an image, apply thresholding to segment the foreground from the background, and view both the original and thresholded images side by side.

## How It Works

1. **Upload Image**: Users can upload an image file (JPG, JPEG, PNG).
2. **Threshold Adjustment**: A slider is provided to adjust the threshold value. The higher the threshold, the less detailed the foreground will be.
3. **Display Results**: Both the original and thresholded images are displayed side by side.

## Getting Started

### Prerequisites

- Python 3.7 or later
- Streamlit: `pip install streamlit`

### Installation

1. Clone this repository to your local machine:
    ```sh
    git clone https://github.com/yourusername/image-thresholding-tool.git
    cd image-thresholding-tool
    ```

2. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```

### Running the App

1. Start the Streamlit app by running:
    ```sh
    streamlit run app.py
    ```

2. Open your web browser and go to `http://localhost:8501` to see the app in action.


### requirements.txt

The `requirements.txt` file listing all dependencies:

```txt
streamlit==1.44.1
opencv-python==4.11.0
numpy==1.26.4
```

### Explanation of Dependencies

- **Streamlit**: The web framework used to build the app.
- **OpenCV-Python**: For image processing tasks like converting images to grayscale and applying thresholding.
- **Numpy**: For handling numerical operations on arrays, though it's not strictly necessary for this specific task, it's often useful in other OpenCV operations.

