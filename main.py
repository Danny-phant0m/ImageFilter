# importing OpenCV(cv2) module
import cv2
 
if __name__ == "__main__":
    try:
        print("Choose a image to apply a filter to ")
        print("1. Image_1")
        print("2. Image_2")
        print("3. Image_3")
        print("4. Image_4")
        image_number = int(input()) # gets the users input and makes sure that it is a number

        # Save image in set directory
        img = cv2.imread('images/Image_'+str(image_number)+'.jpg')# loads the image to open cv

        print("Choose a filter to apply to the image")
        print("1. Grayscale")
        print("2. Blurring (Gaussian)")
        print("3. Edge Detection (Canny)")
        print("4. Color Swapping")
        filter_number = int(input())

    except ValueError:
        print("That's not an int!")

