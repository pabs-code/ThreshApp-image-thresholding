# Image Thresholding Tool with Streamlit

## 📚 Table of Contents

- [Project Overview](#project-overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Code Structure](#code-structure)
- [Example Screenshots and Videos (#example-screenshots-and-video)
- [Technical Notes](#technical-notes)
- [License](#license)

---

## 📚 Project Overview

This is a **Streamlit-based application** for image thresholding that segments the foreground from the background using object-oriented principles. The tool provides an intuitive interface for experimenting with different threshold values.

---

## 📦 Features

- ✅ **Interactive Threshold Slider**: Adjust threshold value between 0 and 255.
- ✅ **Image Segmentation**: Apply binary thresholding to grayscale images.
- ✅ **Visual Comparison**: Display original and thresholded images side-by-side.
- ✅ **Modular Architecture**: Clean, object-oriented code structure with clear separation of concerns.

---

## 🛠️ Installation

### Prerequisites

Install the required packages using pip:

```bash
pip install streamlit opencv-python numpy
```

---

## 🧪 Usage

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

## 🧩 Code Structure

### 📦 Project Architecture

```
image_thresholding_tool/
│
├── app.py              # Main application with OOP structure
└── README.md           # Project explantion file
└── requirements.txt    # file with needed libraries

```

---

## 📊 Example Screenshots and Video

| Feature          | Description                                          |
| ---------------- | ---------------------------------------------------- |
| Main Interface   | Streamlit app with title and instructions            |
| Threshold Slider | Interactive slider for adjusting threshold value     |
| Image Comparison | Side-by-side view of original and thresholded images |


https://github.com/user-attachments/assets/870ed6d4-7997-4efd-bb70-be7ff7b09cde

---

## 📄 License

This project is licensed under the MIT License - see [LICENSE](https://github.com/pabs-code/image-grayscale-histogram-generator/blob/main/LICENSE) file for details.

---

## 💡 Technical Notes

1. **Streamlit Integration**:
   - The app uses `streamlit` for the web interface.
   - Requires running with `streamlit run app.py`.

2. **Image Processing**:
   - Uses OpenCV's `cv2.threshold()` for binary thresholding.
   - Converts to grayscale before processing.

3. **Temporary File Handling**:
   - Ensures proper cleanup with `os.unlink()`.
   - Uses `tempfile.NamedTemporaryFile` for secure file management.

4. **Thresholding Behavior**:
   - Pixels above threshold become white (255).
   - Pixels at or below threshold become black (0).

---

