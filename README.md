# ImageFilter

ImageFilter is a Python application that allows users to apply a variety of filters to images, making it easy to enhance and modify photos. With a user-friendly command-line interface, you can choose from different filtering options to transform your images creatively.

Features
Filter Options:
Grayscale: Converts the image to shades of gray.
Blurring (Gaussian): Applies a Gaussian blur to the image.
Edge Detection (Canny): Detects edges in the image using the Canny algorithm.
Color Swapping: Swaps the color channels of the image.
Brightness Adjustment: Increases brightness using scalar multiplication or addition.
Pencil Sketch Effect: Converts the image to a pencil sketch.
Transpose: Flips the image dimensions.
Getting Started
To start the application, run the following command in your terminal:
`python main.py`
This will launch the program, prompting you to select an image and a filter to apply.

Requirements
Python 3.x
Required libraries: OpenCV, NumPy, Matplotlib
How It Works
Choose an Image: You can select from several predefined images.
Select a Filter: Choose from a variety of filters to apply to the selected image.
Process the Image: The application processes the image and saves the output in the specified directory.
Visual Confirmation: Displays both the original and the processed images for comparison.
Output
The processed image will be saved as processed_image_<number>.jpg in the output_images directory.
