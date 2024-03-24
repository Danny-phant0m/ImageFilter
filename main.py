# importing OpenCV(cv2) module
import cv2
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
 
if __name__ == "__main__":
    try:
        print("Choose a image to apply a filter to ")
        print("1. Image_1")
        print("2. Image_2")
        print("3. Image_3")
        print("4. Image_4")
        image_number = int(input()) # gets the users input and makes sure that it is a number

        clear_screen()
        # Save image in set directory
        img = cv2.imread('images/Image_'+str(image_number)+'.jpg')# loads the image to open cv
        print(img)
        print("Choose a filter to apply to the image")
        print("1. Grayscale")
        print("2. Blurring (Gaussian)")
        print("3. Edge Detection (Canny)")
        print("4. Color Swapping")
        filter_number = int(input())

        clear_screen()
        # Apply the filter based on choice
        if filter_number == 1:
            filtered_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        elif filter_number == 2:
            filtered_image = cv2.GaussianBlur(img, (5, 5), 0)
        elif filter_number == 3:
            filtered_image = cv2.Canny(img, 100, 200) 
        elif filter_number == 4:
            B, G, R = cv2.split(img)
            filtered_image = cv2.merge((R, B, G))
        else:
            print("Invalid filter choice. Please choose from 1-4.")
            exit()

        # Output confirmation message
        print("\nThe chosen filter has been applied to the image.")
        print("Your processed image is saved as 'processed_image_"+str(image_number)+".jpg'")

        # Save the processed image
        cv2.imwrite('processed_image_'+str(image_number)+'.jpg', filtered_image)

    except ValueError:
        print("That's not an int!")

