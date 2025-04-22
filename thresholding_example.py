import cv2
import numpy as np

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


if __name__ == '__main__':
    # Loading example image
    image_file = './img/sample-one.jpg'
    
    # Create a dummy image if one doesn't exist for testing purposes
    try:
        img = cv2.imread(image_file)
        if img is None:
            raise FileNotFoundError
    except FileNotFoundError:
        print("Image not found, creating a dummy image.")
        dummy_img = np.zeros((100, 100, 3), dtype=np.uint8)
        cv2.imwrite(image_file, dummy_img)

    thresholded_image = image_thresholding(image_file, threshold_value=127)

    if thresholded_image is not None:
        # Display the original and thresholded images
        cv2.imshow('Original Image', cv2.imread(image_file))
        cv2.imshow('Thresholded Image', thresholded_image)
        cv2.waitKey(0)  # Wait for any key press to close the windows
        cv2.destroyAllWindows()

        # Save the thresholded image:
        cv2.imwrite("./img/thresholded_image.jpg", thresholded_image)
