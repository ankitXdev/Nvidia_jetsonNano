################################################################################
#                        NVIDIA Cloud Lab by AiProff.ai                            #
#                          CAPSTONE PROJECT                                    #
#                    Starter Kit 1 - Final Challenge                           #
################################################################################
#
# WHAT IS A CAPSTONE PROJECT?
# ===========================
# A "capstone" is the final stone placed at the top of a building or structure,
# representing completion and achievement. In education, a CAPSTONE PROJECT is:
#
# - The FINAL and most COMPREHENSIVE project in a course
# - Combines ALL skills and knowledge learned previously
# - Tests your ability to work INDEPENDENTLY
# - Demonstrates MASTERY of the subject
# - Prepares you for REAL-WORLD applications
#
# Think of it as your "graduation project" for Starter Kit 1!
#
################################################################################
#                          PROJECT OVERVIEW                                     #
################################################################################
#
# MISSION: Build a Multi-Object Detection System with Performance Monitoring
#
# You will create a detection system that can:
# 1. Detect PERSONS in images using HOG
# 2. Detect CARS/VEHICLES in images
# 3. Monitor system resources (CPU, GPU, Memory)
# 4. Measure detection performance
# 5. Generate detailed reports
#
################################################################################
#                          IMPORTANT RULES                                      #
################################################################################
#
# ⚠️  NO CODE PROVIDED - You write EVERYTHING from scratch
# ⚠️  NO HINTS - Figure it out using your knowledge and research
# ⚠️  INDEPENDENT WORK - Show your problem-solving skills
#
# You may reference:
# ✓ Previous task files (task1, task2, task3)
# ✓ Previous assignments (assignment1, assignment2, assignment3)
# ✓ OpenCV documentation
#
################################################################################
#                       CORE REQUIREMENTS (MUST COMPLETE)                       #
################################################################################
#
# REQUIREMENT 1: Multi-Object Detection
# ======================================
# A) PERSON DETECTION using HOG
#    - Detect all persons in the image
#    - Draw GREEN bounding boxes around detected persons
#    - Count total persons detected
#
# B) CAR/VEHICLE DETECTION
#    - Detect all cars in the image (research required!)
#    - Draw BLUE bounding boxes around detected cars
#    - Count total cars detected
#
# REQUIREMENT 2: Visual Output
# =============================
# - Load input image: "street_scene.jpg"
# - Draw GREEN rectangles around persons
# - Draw BLUE rectangles around cars
# - Add text labels showing object type ("Person", "Car")
# - Display the annotated image in a window
# - Save the output image as "capstone_output.jpg"
#
# REQUIREMENT 3: System Resource Monitoring
# ==========================================
# A) CPU Usage - Measure CPU usage percentage during detection
# B) GPU Usage - Get GPU statistics using tegrastats (Jetson Nano)
# C) Memory Usage - Measure RAM before/after detection
# D) Detection Time - Measure time for person detection, car detection, and total
#
# REQUIREMENT 4: Statistics Report
# =================================
# Print a comprehensive report to console with:
# - Total persons detected
# - Total cars detected
# - Total objects detected
# - CPU usage percentage
# - GPU usage statistics
# - Detection times
# - Memory consumption
# - Output file confirmation
#
# Example Output:
# ===== DETECTION RESULTS =====
# Persons Detected: 3
# Cars Detected: 5
# Total Objects: 8
#
# ===== PERFORMANCE METRICS =====
# Person Detection Time: 0.245 seconds
# Car Detection Time: 0.312 seconds
# Total Processing Time: 0.557 seconds
#
# ===== SYSTEM RESOURCES =====
# CPU Usage: 67.5%
# Memory Before: 1.2 GB
# Memory After: 1.5 GB
# Memory Used: 0.3 GB
#
################################################################################
#                   ADDITIONAL TASKS (ADVANCED CHALLENGES)                      #
################################################################################
#
# TASK A: Confidence Filtering
# - Display confidence scores for each detection
# - Filter detections below confidence threshold 0.5
#
# TASK B: Batch Processing
# - Process multiple images from a folder
# - Generate summary statistics
#
# TASK C: Image Preprocessing
# - Implement brightness/contrast enhancement
# - Compare results with/without preprocessing
#
# TASK D: Performance Optimization
# - Test different image scales (400px, 800px, 1200px)
# - Compare performance metrics
#
# TASK E: Error Handling & Logging
# - Implement try-except blocks
# - Create log file with timestamps
#
# TASK F: Detection Parameters Tuning
# - Experiment with different detection parameters
# - Save optimal parameters to config file
#
# TASK G: Visual Enhancements
# - Add object count overlay
# - Add timestamp to image
# - Create color-coded legend
#
# TASK H: Resource Alerts
# - Set CPU/memory thresholds
# - Display warnings if exceeded
#
# TASK I: Multi-Threading (Advanced)
# - Run detections in parallel
# - Compare sequential vs parallel performance
#
# TASK J: Detection Comparison
# - Compare HOG vs Haar Cascade methods
# - Generate comparison report
#
################################################################################
#                         RESOURCES FOR CAR DETECTION                           #
################################################################################
#
# CAR DETECTION CHALLENGE:
# ========================
# OpenCV provides a built-in person detector, but NOT a car detector.
# You need to find or use pre-trained models for car/vehicle detection.
#
# Download Haar Cascade XML files for car detection:
# 
# 1. Official OpenCV Haar Cascades:
#    https://github.com/opencv/opencv/tree/master/data/haarcascades
#
# 2. Vehicle Detection Haar Cascades (RECOMMENDED):
#    https://github.com/andrewssobral/vehicle_detection_haarcascades
#    - Download 'cars.xml' file from this repository
#
################################################################################
#                         SUBMISSION REQUIREMENTS                               #
################################################################################
#
# Submit:
# 1. capstone_project.py (your complete code)
# 2. capstone_output.jpg (output image)
# 3. capstone_report.txt (statistics - optional)
# 4. capstone_log.txt (log file - optional)
#
################################################################################
#                     NOW... WRITE YOUR CODE BELOW!                            #
################################################################################

# YOUR CODE STARTS HERE
# Build everything from scratch using your knowledge from previous tasks.
# Research, experiment, and solve problems independently.
# Good luck! 💪🚀

