# ============================================================================
#                        NVIDIA Cloud Lab by AiProff.ai
#                  Assignment 1: Haar Cascade Face Detection
# ============================================================================
# Reference: Study task1/detect_person_haar.py to understand the complete workflow
# 
# Your Task: Complete this face detection program by filling in the missing code.
# Read each question carefully and refer to the reference file when needed.
# ============================================================================

# QUESTION 1: Which Python library provides computer vision functions?
# TODO: Import the required library
import cv2


# QUESTION 2: What is the first step in processing an image?
# TODO: Load "image.jpg" into a variable named 'img'



# QUESTION 3: Why is error handling important when loading files?
# TODO: Check if the image loaded successfully
# TODO: If not, exit the program with an appropriate message



# QUESTION 4: Why do Haar Cascades work better with grayscale images?
# TODO: Convert the loaded image to grayscale using cv2.cvtColor()
# TODO: Store the result in a variable named 'gray'



# QUESTION 5: What is a Haar Cascade classifier and how do you load it?
# TODO: Build the path to haarcascade_frontalface_default.xml
# TODO: The file should be in the same directory as this script
cascade_path = "haarcascade_frontalface_default.xml"
# TODO: Load the cascade classifier using cv2.CascadeClassifier()
# TODO: Store it in a variable named 'face_cascade'



# QUESTION 6: How do you validate that the cascade loaded successfully?
# TODO: Check if the cascade is empty using .empty() method
# TODO: If empty, raise SystemExit with an error message



# QUESTION 7: How does face detection work with detectMultiScale()?
# TODO: Use face_cascade.detectMultiScale() on the grayscale image
# TODO: Set parameters: scaleFactor=1.1, minNeighbors=5, minSize=(30, 30)
# TODO: Store results in a variable named 'faces'



# QUESTION 8: How do we visualize detected faces?
# TODO: Iterate through the faces array using a for loop
# TODO: Each face is represented as (x, y, w, h)
# TODO: Draw blue rectangles using cv2.rectangle() with color (255, 0, 0) and thickness 2



# QUESTION 9: How do we display results to the user?
# TODO: Show the image in a window using cv2.imshow()
cv2.imshow("Haar Cascade Face Detection", img)
# TODO: Wait for key press using cv2.waitKey(0)
# TODO: Cleanup windows using cv2.destroyAllWindows()



# QUESTION 10: How do we persist results?
# TODO: Save the output image as "assignment1_face_detected.jpg"
# TODO: Print detection statistics showing number of faces detected


# ============================================================================
# CHALLENGE (Optional):
# 1. Modify detection parameters (scaleFactor, minNeighbors) and observe changes
# 2. Add text labels showing face count on the image
# 3. Try detecting faces in multiple images
# 4. Compare with Task 3 (HOG method) - which is faster? More accurate?
# ============================================================================
