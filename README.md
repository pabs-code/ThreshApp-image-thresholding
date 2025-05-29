# ThreshApp: Image Thresholding Tool with Streamlit

## 📚 Table of Contents

- [Project Overview](#project-overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Key Concepts](#key-concepts)
- [Example Screenshot and Video](#example-screenshot-and-video)
- [License](#license)

---

## Project Overview

This is a **Streamlit-based image thresholding application** that allows users to upload images and apply binary thresholding to segment the foreground from the background. It is designed for educational purposes, image processing experimentation, and simple computer vision tasks.

The app provides an intuitive interface where users can:
- Upload images in common formats (JPG, JPEG, PNG)
- Adjust a threshold slider to control the binarization process
- View both the original and thresholded images side-by-side



---

## Features

| Feature | Description |
|--------|-------------|
| ✅ Image Upload | Supports JPG, JPEG, and PNG formats |
| ✅ Threshold Slider | Adjust threshold value between 0 and 255 |
| ✅ Binarization | Applies binary thresholding to images |
| ✅ Visual Comparison | Displays original and thresholded image side-by-side |
| ✅ Temporary File Handling | Ensures no leftover files after session ends |


---

## Installation

### Prerequisites

Install the required packages using pip:

```bash
pip install streamlit opencv-python numpy
```

---

## Usage

### 1. Run the Application

Run the Streamlit app using:

```bash
streamlit run app.py
```

### 2. Upload an Image

Supported formats: JPG, JPEG, PNG.

### 3. Adjust Threshold

Use the slider to experiment with different threshold values (0–255).

---

## Key Concepts

| Concept | Description |
|--------|-------------|
| **Binary Thresholding** | Converts each pixel to either black (0) or white (255) based on a threshold value. |
| **Threshold Value** | A pixel intensity value used to split the image into foreground and background. |
| **Higher Threshold** | Results in fewer pixels being considered as "foreground", making the image less detailed. |
| **Lower Threshold** | Results in more pixels being considered as "foreground", making the image more detailed. |

Thresholding is widely used in applications like:
- Document scanning
- Object detection
- Medical imaging
- Optical character recognition (OCR)

---

## Example Screenshots and Video

| Feature          | Description                                          |
| ---------------- | ---------------------------------------------------- |
| Main Interface   | Streamlit app with title and instructions            |
| Threshold Slider | Interactive slider for adjusting threshold value     |
| Image Comparison | Side-by-side view of original and thresholded images |


https://github.com/user-attachments/assets/870ed6d4-7997-4efd-bb70-be7ff7b09cde

---

## License

This project is licensed under the MIT License - see [LICENSE](https://github.com/pabs-code/image-grayscale-histogram-generator/blob/main/LICENSE) file for details.

---

