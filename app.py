import os
import cv2
import numpy as np
import streamlit as st
import tempfile


class ThresholdingApp:
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
        self.title = "Image Thresholding Tool: Segment Foreground from Background"
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

    def run(self):
        """Main application entry point."""
        self._show_title()

        # Process image upload
        temp_filename = self._process_upload()

        if temp_filename:
            # Create threshold slider
            threshold_value = st.slider(
                "Threshold Value",
                min_value=self.threshold_range[0],
                max_value=self.threshold_range[1],
                value=127
            )

            # Apply thresholding and display results
            thresholded_image = self._apply_thresholding(
                temp_filename, threshold_value)

            if thresholded_image is not None:
                st.image(
                    cv2.imread(temp_filename),
                    caption="Original Image",
                    use_container_width=True
                )

                st.image(
                    thresholded_image,
                    caption="Thresholded Image",
                    use_container_width=True
                )

                # Optional: Save thresholded image to file
                cv2.imwrite("thresholded_image.jpg", thresholded_image)

            # Clean up temporary file
            os.unlink(temp_filename)


if __name__ == "__main__":
    app = ThresholdingApp()
    app.run()
