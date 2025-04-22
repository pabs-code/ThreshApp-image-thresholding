import cv2
import numpy as np
import streamlit as st
import tempfile


def image_thresholding(image_path, threshold_value=127):
    """
    Converts an image to grayscale and applies thresholding to segment the
    foreground from the background.

    Args:
        image_path (str): The path to the input image file.
        threshold_value (int): The threshold value for binarization.  Pixels
                                  with values above this are considered foreground,
                                  and pixels with values below or equal to this
                                  are considered background.

    Returns:
        numpy.ndarray: The thresholded image as a NumPy array.
    """

    # Read the image in BGR format (OpenCV's default)
    img = cv2.imread(image_path)

    if img is None:
        print(f"Error: Could not read image at {image_path}")
        return None

    # Convert the image to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Apply thresholding
    _, thresh = cv2.threshold(gray, threshold_value, 255, cv2.THRESH_BINARY)
    # _ is used to discard the return value of cv2.threshold (we only need the thresholded image)

    return thresh


def main():
    """
    Main function to set up the Streamlit app.
    """
    st.title("Image Thresholding Tool: Segment Foreground from Background")

    st.write("""
        **Threshold Value Explanation**:
        
        The threshold value determines the cutoff point in pixel intensity that separates the foreground from the background. 
        - **Higher Threshold Values**: This results in a smaller, less detailed foreground.
        - **Lower Threshold Values**: This results in a larger, more detailed foreground.

        Adjust the slider below to experiment with different threshold values and see how they affect the segmentation of your image.

        **Note**: The original image is displayed as it was uploaded. After applying thresholding, only pixel intensities are adjusted, not the color mode.
        """)

    uploaded_file = st.file_uploader("Upload an image...", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        # Save the uploaded file to a temporary location
        with tempfile.NamedTemporaryFile(delete=False, suffix=".jpg") as temp_file:
            temp_filename = temp_file.name
            temp_file.write(uploaded_file.getvalue())

        try:
            # Read the image from the temporary file
            img = cv2.imread(temp_filename)

            if img is None:
                st.error("Invalid image format. Please upload a JPG or PNG.")
                return

            # Apply thresholding
            threshold_value = st.slider(
                "Threshold Value", min_value=0, max_value=255, value=127
            )
            thresholded_image = image_thresholding(temp_filename, threshold_value)

            if thresholded_image is not None:
                # Display the original and thresholded images
                st.image(img, caption="Original Image", use_container_width=True)
                st.image(
                    thresholded_image,
                    caption="Thresholded Image",
                    use_container_width=True,
                )

                # Save the thresholded image to a file (optional)
                cv2.imwrite("thresholded_image.jpg", thresholded_image)
        finally:
            # Clean up the temporary file
            import os

            os.unlink(temp_filename)


if __name__ == "__main__":
    main()
