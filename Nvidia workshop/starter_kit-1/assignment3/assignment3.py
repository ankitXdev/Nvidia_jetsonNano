# ============================================================================
#                        NVIDIA Cloud Lab by AiProff.ai
#         Assignment 3: HOG Face Detection with System Monitoring
# ============================================================================
# Reference: Study task3/detect_face_hog.py to understand the workflow
# 
# Your Task: Implement HOG-based face detection and compare with Haar Cascade
# This assignment uses HOG (or DNN fallback) and includes system monitoring
# ============================================================================

# QUESTION 1: What libraries are needed for HOG face detection with monitoring?
# TODO: Import cv2, psutil, subprocess, time, re, sys, os



# QUESTION 2: How do you retrieve GPU statistics? (Same as Assignment 2)
# TODO: Create get_gpu_usage() function
# TODO: Use subprocess.Popen() with tegrastats command
# TODO: Return the last line of output after 2 seconds
def get_gpu_usage():
    pass



# QUESTION 3: How do you format GPU statistics? (Same as Assignment 2)
# TODO: Create format_gpu_stats(raw_stats) function
# TODO: Parse RAM, SWAP, CPU cores, frequencies, temperatures using regex
# TODO: Return formatted table with borders
def format_gpu_stats(raw_stats):
    pass



# QUESTION 4: How do you load and validate images?
# TODO: Load "image.jpg"
# TODO: Check if file exists using os.path.exists()
# TODO: Add error handling and print dimensions



# QUESTION 5: Why convert to grayscale for HOG?
# TODO: Convert to grayscale (HOG can work with color, but grayscale is faster)



# QUESTION 6: How do you resize for optimal processing?
# TODO: Calculate scale for max 800 pixels
# TODO: Resize both color and grayscale images if needed



# QUESTION 7: How do you initialize HOG face detector?
# TODO: Try to import dlib library
# TODO: If available, use dlib.get_frontal_face_detector()
# TODO: If not available, use OpenCV DNN as fallback
# TODO: Set use_dlib flag accordingly
# HINT: Use try-except ImportError block



# QUESTION 8: How do you perform face detection with HOG/DNN?
# TODO: Record start time
# TODO: If using dlib: call hog_face_detector(gray, 1) and convert rectangles
# TODO: If using DNN: create blob, run forward pass, filter by confidence > 0.5
# TODO: Calculate detection time
# TODO: Print detection method used, time, and face count



# QUESTION 9: How do you draw bounding boxes with HOG results?
# TODO: Iterate through faces
# TODO: Draw BLUE rectangles using cv2.rectangle()
# TODO: Use color (255, 0, 0) to distinguish from Haar Cascade (green)



# QUESTION 10: How do you add informative labels to the image?
# TODO: Use cv2.putText() to add:
#       - Detection method name at (10, 30)
#       - Number of faces at (10, 60)
#       - Detection time at (10, 90)
# TODO: Use font=cv2.FONT_HERSHEY_SIMPLEX, size=0.7, color=(255,0,0), thickness=2



# QUESTION 11: How do you save output with proper naming?
# TODO: Save as "assignment3_face_detected_hog.jpg"



# QUESTION 12: How do you print detection summary?
# TODO: Print a summary table with:
#       - Detection method used
#       - Number of faces detected
#       - Detection time
#       - Output filename



# QUESTION 13: How do you print method comparison information?
# TODO: Print a comparison table between Haar Cascade and HOG/DNN
# TODO: Include information about speed, accuracy, use cases
# HINT: See Task 3 for the comparison format



# QUESTION 14: How do you collect system resource statistics?
# TODO: Get CPU usage with psutil.cpu_percent(interval=1)
# TODO: Get and format GPU stats
# TODO: Print CPU usage and formatted GPU stats



# QUESTION 15: How do you print final summary?
# TODO: Print completion summary with:
#       - Number of faces detected with method name
#       - Detection time
#       - Output filename
#       - System monitoring status
# TODO: Print next steps suggesting comparison with Task 1



# QUESTION 16: How do you cleanup?
# TODO: Call cv2.destroyAllWindows()


# ============================================================================
# CHALLENGE (Optional):
# 1. Download and test with the DNN model if dlib is not available
# 2. Compare detection results between dlib HOG and OpenCV DNN
# 3. Run the same image through Assignment 1 (Haar) and Assignment 3 (HOG)
#    - Compare detection times
#    - Compare accuracy (which detected more/better?)
#    - Compare resource usage
# 4. Test with images at different angles and lighting conditions
# 5. Add a side-by-side comparison showing both Haar and HOG results
# 6. Implement the full progress tracker [1/9], [2/9], etc. like Task 3
# ============================================================================
