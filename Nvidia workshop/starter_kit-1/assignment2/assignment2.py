# ============================================================================
#                        NVIDIA Cloud Lab by AiProff.ai
#    Assignment 2: Haar Cascade Face Detection with System Resource Monitoring
# ============================================================================
# Reference: Study task2/detect_person_haar_sys.py to understand the workflow
# 
# Your Task: Build upon Assignment 1 by adding system monitoring capabilities
# This assignment teaches you how to monitor CPU and GPU usage during detection
# ============================================================================

# QUESTION 1: What libraries are needed for system resource monitoring?
# TODO: Import computer vision library
import cv2
# TODO: Import library for CPU monitoring
import psutil
# TODO: Import library for running shell commands (subprocess)
# TODO: Import time, re, sys, os modules



# QUESTION 2: How can we retrieve GPU statistics on Jetson Nano?
# TODO: Create a function called get_gpu_usage() that returns GPU stats
# TODO: Use subprocess.Popen() to execute tegrastats command
# TODO: Set interval to 1000ms using ['tegrastats', '--interval', '1000']
# TODO: Let it run for 2 seconds using time.sleep(2)
# TODO: Terminate the process and get output
# TODO: Return the last line of output
# TODO: Add try-except error handling
def get_gpu_usage():
    # TODO: Implement the function body here
    pass



# QUESTION 3: How do you format raw GPU statistics into a readable table?
# TODO: Create a function called format_gpu_stats(raw_stats) 
# TODO: Use regex (re module) to extract RAM, SWAP, CPU, frequencies, temperatures
# TODO: Format into a nice table with borders and labels
# TODO: Return formatted string
def format_gpu_stats(raw_stats):
    # TODO: Implement parsing and formatting logic
    pass



# QUESTION 4: How do you load and validate images with detailed feedback?
# TODO: Load "image.jpg" using cv2.imread()
# TODO: Check if file exists using os.path.exists()
# TODO: Add error handling with informative messages
# TODO: Print success message with image dimensions



# QUESTION 5: Why convert to grayscale for Haar Cascade?
# TODO: Convert image to grayscale using cv2.cvtColor()
# TODO: Use cv2.COLOR_BGR2GRAY conversion



# QUESTION 6: How do you implement image resizing for optimal processing?
# TODO: Calculate scale factor for max dimension of 800 pixels
# TODO: Resize both color and grayscale images if needed
# TODO: Print original and new dimensions



# QUESTION 7: How do you load and validate Haar Cascade classifier?
# TODO: Set cascade_path to "haarcascade_frontalface_default.xml"
# TODO: Check if file exists using os.path.exists()
# TODO: Load using cv2.CascadeClassifier()
# TODO: Validate with .empty() method



# QUESTION 8: How do you perform face detection with timing?
# TODO: Record start time using time.time()
# TODO: Use detectMultiScale() with parameters: scaleFactor=1.1, minNeighbors=5, minSize=(30,30)
# TODO: Calculate detection_time = time.time() - start_time
# TODO: Print detection time and face count
# TODO: Print details of each face (position and size)



# QUESTION 9: How do you draw bounding boxes on detected faces?
# TODO: Iterate through faces array
# TODO: Draw green rectangles using cv2.rectangle()
# TODO: Use color (0, 255, 0) and thickness 2



# QUESTION 10: How do you save output with proper naming?
# TODO: Save image as "assignment2_face_detected.jpg"
# TODO: Print success message



# QUESTION 11: How do you measure CPU utilization?
# TODO: Use psutil.cpu_percent(interval=1) for accurate measurement
# TODO: Store in cpu_usage variable



# QUESTION 12: How do you retrieve and format GPU statistics?
# TODO: Call get_gpu_usage() function
# TODO: Pass result to format_gpu_stats() function
# TODO: Print CPU usage percentage
# TODO: Print formatted GPU stats table



# QUESTION 13: How do you print a complete summary?
# TODO: Print a nice summary with borders showing:
#       - Number of faces detected
#       - Output filename
#       - System monitoring complete message



# QUESTION 14: How do you manage window lifecycle?
# TODO: Call cv2.destroyAllWindows()
# NOTE: cv2.imshow() may be commented out for headless systems


# ============================================================================
# CHALLENGE (Optional):
# 1. Compare resource usage with different image sizes
# 2. Log metrics to a file with timestamps
# 3. Add memory usage monitoring using psutil.virtual_memory()
# 4. Create a complete progress tracker with [1/8], [2/8], etc. like Task 2
# 5. Parse and display individual temperature readings from GPU stats
# 6. Add color-coded status messages (✅ ❌ ⚠️)
# ============================================================================
