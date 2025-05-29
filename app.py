import os
import cv2
import numpy as np
import streamlit as st
import tempfile


class BinaryThresholdingApp:
    """
    A Streamlit application for image thresholding using streamlit.

    Attributes:
        title (str): Title of the Streamlit application
        threshold_range (tuple): Range for threshold slider [min, max]
    """

    def __init__(self):
        """Initialize the application with Streamlit configuration."""
        st.set_page_config(
            page_title="Image Thresholding Tool",
            layout="wide"
        )
        self.title = "Image Binary Thresholding Tool: Segment Foreground from Background"
        self.threshold_range = (0, 255)

    def _show_title(self):
        """Display the application title with explanatory text."""
        st.title(self.title)

        st.markdown("""
        ### 🧠 Threshold Value Explanation
        - **Higher Values**: Smaller, less detailed foreground
        - **Lower Values**: Larger, more detailed foreground
        
        Adjust the slider below to experiment with different threshold values.
        
        ⚠️ The original image is displayed as-is. Thresholding only affects pixel intensities.
        """)

    def _process_upload(self):
        """Handle image upload and temporary file management."""
        uploaded_file = st.file_uploader(
            "Upload an image...", type=["jpg", "jpeg", "png"]
        )

        if uploaded_file is None:
            return None

        # Create temporary file for image processing
        with tempfile.NamedTemporaryFile(delete=False, suffix=".jpg") as temp_file:
            temp_filename = temp_file.name
            temp_file.write(uploaded_file.getvalue())

        return temp_filename

    def _apply_thresholding(self, image_path, threshold_value):
        """
        Apply binary thresholding to an image.

        Args:
            image_path (str): Path to the input image file
            threshold_value (int): Threshold value for binarization

        Returns:
            numpy.ndarray: Thresholded image as a NumPy array
        """
        # Read the image in BGR format (OpenCV's default)
        img = cv2.imread(image_path)

        if img is None:
            st.error("Invalid image format. Please upload a JPG or PNG.")
            return None

        # Convert to grayscale
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        # Apply thresholding
        _, thresh = cv2.threshold(
            gray, threshold_value, 255, cv2.THRESH_BINARY)

        return thresh

    def main(self):
        """Run the Streamlit application logic."""
        self._show_title()

        temp_filename = self._process_upload()

        if temp_filename:
            threshold_value = st.slider(
                "Threshold Value",
                min_value=self.threshold_range[0],
                max_value=self.threshold_range[1],
                value=127
            )

            thresholded_image = self._apply_thresholding(
                temp_filename, threshold_value)

            if thresholded_image is not None:
                # Display original image (converted to RGB)
                rgb_original = cv2.cvtColor(
                    cv2.imread(temp_filename), cv2.COLOR_BGR2RGB)
                st.image(rgb_original, caption="Original Image",
                         use_container_width=True)

                # Display thresholded image (already grayscale)
                st.image(thresholded_image, caption="Thresholded Image",
                         use_container_width=True)

                # Optional: Save thresholded image (in BGR format)
                cv2.imwrite("thresholded_image.jpg", thresholded_image)

            os.unlink(temp_filename)


if __name__ == "__main__":
    app = BinaryThresholdingApp()
    app.main()  # Call the `main()` function to start the Streamlit application
