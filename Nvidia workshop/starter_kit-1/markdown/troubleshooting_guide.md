# Jetson Nano Starter Kit 1 - Troubleshooting Guide

**A Complete Guide to Solving Common Issues in Face Detection Tasks**

---

## Table of Contents

1. [Verify OpenCV Installation](#verify-opencv-installation)
2. [Problem 1: Haar Cascade XML File Path Error](#problem-1-haar-cascade-xml-file-path-error)
3. [Problem 2: No Faces Detected](#problem-2-no-faces-detected)
4. [Problem 3: System Monitoring - Missing psutil](#problem-3-system-monitoring---missing-psutil)
5. [Problem 4: Task 3 - dlib Module Not Found](#problem-4-task-3---dlib-module-not-found)
6. [Problem 5: GUI Display Errors](#problem-5-gui-display-errors)
7. [Problem 6: tegrastats Command Not Found](#problem-6-tegrastats-command-not-found)
8. [Common Troubleshooting Tips](#common-troubleshooting-tips)
9. [OpenCV Build Process Summary](#opencv-build-process-summary)

---

## Verify OpenCV Installation

Before starting any task, verify that OpenCV is properly installed on your Jetson Nano.

### Check OpenCV Version

```bash
pkg-config --modversion opencv4
```

**If OpenCV is NOT installed**, you'll see:
```
Package opencv4 was not found in the pkg-config search path.
Perhaps you should add the directory containing `opencv4.pc`
to the PKG_CONFIG_PATH environment variable
No package 'opencv4' found
```

**If OpenCV IS installed**, you'll see a version number:
```
4.8.0
```

### Test OpenCV in Python

```bash
python3 - <<'EOF'
import cv2
print("OpenCV version:", cv2.__version__)
print("CUDA enabled devices:", cv2.cuda.getCudaEnabledDeviceCount())
EOF
```

**Expected Outputs:**

✅ **GPU-Accelerated Build (Ideal for Jetson Nano):**
```
OpenCV version: 4.8.0
CUDA enabled devices: 1
```
Your GPU-accelerated OpenCV build is ready!

⚠️ **CPU-Only Build:**
```
OpenCV version: 4.x.x
CUDA enabled devices: 0
```
or
```
OpenCV version: 4.x.x
CUDA module not available in this OpenCV build
```

❌ **Not Installed:**
```
ModuleNotFoundError: No module named 'cv2'
```
You need to install OpenCV first (see [OpenCV Build Process](#opencv-build-process-summary)).

---

## Problem 1: Haar Cascade XML File Path Error

**Applies to:** Task 1, Task 2

### The Problem

When running face detection with Haar Cascade (Task 1 or Task 2), you might encounter:

```
cv2.error: OpenCV(4.8.0) error: (-2:Unspecified error) 
Unable to open file 'haarcascade_frontalface_default.xml'
```

Or the cascade loads but `.empty()` returns True.

### Why This Happens

The Haar Cascade XML file is not in the expected location. The task files expect the XML file to be in the **same directory** as the Python script.

### Solution Steps

#### Step 1: Download the Haar Cascade XML File

1. Visit: [https://github.com/opencv/opencv/tree/master/data/haarcascades](https://github.com/opencv/opencv/tree/master/data/haarcascades)
2. Find and click on: `haarcascade_frontalface_default.xml`
3. Click the **"Raw"** button to view the raw file
4. Right-click and "Save As..." or press `Ctrl+S` to download
5. Save it with the exact name: `haarcascade_frontalface_default.xml`

#### Step 2: Place the XML File Correctly

Your project structure should look like this:

**For Task 1:**
```
task1/
├── detect_person_haar.py
├── image.jpg
└── haarcascade_frontalface_default.xml  ← Place XML file here
```

**For Task 2:**
```
task2/
├── detect_person_haar_sys.py
├── image.jpg
└── haarcascade_frontalface_default.xml  ← Place XML file here
```

**For Assignments:**
```
assignment1/
├── assignment1.py
├── image.jpg
└── haarcascade_frontalface_default.xml  ← Place XML file here
```

#### Step 3: Verify the File Path in Code

The task files use this path:
```python
cascade_path = "haarcascade_frontalface_default.xml"
face_cascade = cv2.CascadeClassifier(cascade_path)

# Validate it loaded correctly
if face_cascade.empty():
    raise SystemExit(f"Failed to load cascade at {cascade_path}")
```

### Alternative: Use OpenCV's Built-in Path (If Available)

Some OpenCV installations include the XML files. You can try:

```python
import cv2
import os

# Try to use OpenCV's data directory
try:
    cascade_path = cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
    print(f"Using OpenCV path: {cascade_path}")
except AttributeError:
    # Fallback to local file
    cascade_path = "haarcascade_frontalface_default.xml"
    print(f"Using local path: {cascade_path}")

face_cascade = cv2.CascadeClassifier(cascade_path)
```

### Quick Test

After placing the XML file, test it:

```bash
cd task1
python3 -c "import cv2; fc = cv2.CascadeClassifier('haarcascade_frontalface_default.xml'); print('✅ Loaded!' if not fc.empty() else '❌ Failed!')"
```

---

## Problem 2: No Faces Detected

**Applies to:** All Tasks (1, 2, 3)

### The Problem

Your script runs successfully but detects 0 faces:
```
Detected 0 face(s). Output saved to task1_face_detected.jpg
```

### Common Causes

1. **Image doesn't contain faces** - Verify your test image actually has visible faces
2. **Detection parameters are too strict** - Default parameters might miss faces
3. **Image quality issues** - Low resolution, poor lighting, or extreme angles
4. **Face is too small or too large** - Outside the detection range

### Solutions

#### Solution 1: Adjust Haar Cascade Parameters (Tasks 1 & 2)

The `detectMultiScale()` function has several parameters you can tune:

**Default (Strict):**
```python
faces = face_cascade.detectMultiScale(
    gray,
    scaleFactor=1.1,
    minNeighbors=5,
    minSize=(30, 30)
)
```

**More Sensitive (Detects More):**
```python
faces = face_cascade.detectMultiScale(
    gray,
    scaleFactor=1.05,    # Lower = more thorough (slower)
    minNeighbors=3,      # Lower = more detections (more false positives)
    minSize=(20, 20)     # Smaller = detect smaller faces
)
```

**Less Sensitive (Fewer False Positives):**
```python
faces = face_cascade.detectMultiScale(
    gray,
    scaleFactor=1.2,     # Higher = faster but might miss faces
    minNeighbors=7,      # Higher = more strict (fewer false positives)
    minSize=(50, 50)     # Larger = ignore small faces
)
```

**Parameter Explanations:**
- `scaleFactor`: How much the image is reduced at each scale (1.05 - 1.3)
  - Lower values = more scales checked = more detections but slower
- `minNeighbors`: How many neighbors each candidate rectangle should have (3-8)
  - Lower values = more detections but more false positives
- `minSize`: Minimum face size in pixels (20x20 to 100x100)
  - Smaller values = detect smaller/distant faces

#### Solution 2: Check Image Quality

```python
import cv2

# Load and inspect image
img = cv2.imread("image.jpg")
if img is None:
    print("❌ Failed to load image!")
else:
    print(f"✅ Image loaded: {img.shape[1]}x{img.shape[0]} pixels")
    
    # Check if image is too small
    if img.shape[0] < 100 or img.shape[1] < 100:
        print("⚠️  Image is very small - faces might not be detected")
    
    # Check if image is too large (might need resizing)
    if img.shape[0] > 2000 or img.shape[1] > 2000:
        print("⚠️  Image is very large - consider resizing for faster detection")
```

#### Solution 3: Test with Different Images

Try with different test images to isolate the issue:
- Use images with clear, frontal faces
- Ensure good lighting
- Avoid extreme angles or occlusions
- Try images with different face sizes

#### Solution 4: For Task 3 (HOG/DNN Method)

Task 3 uses a different detection method. If using dlib's HOG:

```python
import dlib

# Adjust upsampling parameter
hog_face_detector = dlib.get_frontal_face_detector()

# Default (faster)
faces = hog_face_detector(gray, 0)  # No upsampling

# More sensitive (slower but detects smaller faces)
faces = hog_face_detector(gray, 1)  # Upsample once
# or
faces = hog_face_detector(gray, 2)  # Upsample twice (very slow)
```

If using OpenCV DNN (fallback in Task 3):

```python
# Adjust confidence threshold
confidence_threshold = 0.5  # Default

# More sensitive
confidence_threshold = 0.3  # Detects more but may have false positives

# In detection loop:
if confidence > confidence_threshold:  # Use your threshold
    # Process detection
```

---

## Problem 3: System Monitoring - Missing psutil

**Applies to:** Task 2, Task 3, Assignment 2, Assignment 3

### The Problem

You want to monitor CPU and GPU usage during detection, but get:

```
ModuleNotFoundError: No module named 'psutil'
```

### Why This Happens

The `psutil` library is not installed by default. It's a Python library for retrieving system information (CPU, memory, etc.).

### Solution: Install psutil

```bash
sudo apt install python3-psutil
```

Or using pip:
```bash
pip3 install psutil
```

### Verify Installation

```bash
python3 -c "import psutil; print('✅ psutil installed:', psutil.__version__)"
```

### How psutil is Used in Tasks

**Task 2 and Task 3 use psutil for CPU monitoring:**

```python
import psutil

# Get CPU usage percentage
cpu_usage = psutil.cpu_percent(interval=1)
print(f"CPU Usage: {cpu_usage}%")
```

**Advanced Usage (Optional):**

```python
import psutil

# Get detailed CPU info
print(f"CPU Count: {psutil.cpu_count()} cores")
print(f"CPU Usage per core: {psutil.cpu_percent(percpu=True)}")

# Get memory info
memory = psutil.virtual_memory()
print(f"Memory: {memory.used / (1024**3):.2f} GB / {memory.total / (1024**3):.2f} GB")
print(f"Memory Usage: {memory.percent}%")
```

---

## Problem 4: Task 3 - dlib Module Not Found

**Applies to:** Task 3, Assignment 3

### The Problem

When running Task 3 (HOG face detection), you might see:

```
ModuleNotFoundError: No module named 'dlib'
```

### Why This Happens

Task 3 uses dlib's HOG face detector for more accurate detection. However, dlib is not installed by default.

### Solution 1: Install dlib (Recommended)

```bash
# Install dependencies first
sudo apt-get install -y python3-dev build-essential cmake

# Install dlib
pip3 install dlib
```

**Note:** Installing dlib can take 5-10 minutes as it compiles from source.

### Solution 2: Use the DNN Fallback (Automatic)

Task 3 is designed with a fallback mechanism. If dlib is not available, it automatically uses OpenCV's DNN face detector.

The code automatically handles this:

```python
try:
    import dlib
    print("✅ Using dlib's HOG face detector")
    use_dlib = True
except ImportError:
    print("⚠️  dlib not available, using OpenCV DNN as fallback...")
    use_dlib = False
    # Falls back to OpenCV DNN
```

**What this means:**
- If dlib is installed → Uses HOG (faster, less accurate)
- If dlib is NOT installed → Uses DNN (slower, more accurate)
- Both methods work fine!

### Verify What Method Task 3 Will Use

```bash
cd task3
python3 -c "
try:
    import dlib
    print('✅ Task 3 will use: HOG (dlib)')
except ImportError:
    print('⚠️  Task 3 will use: DNN (OpenCV fallback)')
"
```

### DNN Model Files

If using the DNN fallback, Task 3 will automatically download these files:
- `deploy.prototxt` - Model architecture
- `res10_300x300_ssd_iter_140000.caffemodel` - Pre-trained weights

These will be downloaded automatically when you run Task 3 for the first time.

---

## Problem 5: GUI Display Errors

**Applies to:** All Tasks (1, 2, 3)

### The Problem

When running scripts via SSH or without a display, you get:

```
Unable to init server: Could not connect: Connection refused
(python3:1234): Gtk-WARNING **: cannot open display:
cv2.error: OpenCV(4.8.0) error: (-2:Unspecified error) 
Can't initialize GTK backend in function 'cvInitSystem'
```

### Why This Happens

You're running your script in an **environment without GUI display support**:
- Logged into Jetson Nano via SSH or terminal-only session
- No display connected
- Running in a headless environment

`cv2.imshow()` requires a display (X server/GTK) which is not available in headless environments.

### Solution: Tasks Already Handle This!

All task files have `cv2.imshow()` **commented out** by default:

```python
# Display result (commented out for headless systems)
# cv2.imshow("Haar Face Detection", img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
```

**The output images are still saved!**

```python
# This works regardless of display
cv2.imwrite("task1_face_detected.jpg", img)
print(f"Detected {len(faces)} face(s). Output saved to task1_face_detected.jpg")
```

### If You Have a Display Connected

If you're running with a display connected (HDMI monitor), you can **uncomment** these lines:

```python
# Uncomment these lines if you have a display
cv2.imshow("Haar Face Detection", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
```

### How to View Output Images

**Option 1: Transfer to Your Computer (SSH)**
```bash
# From your computer
scp username@jetson-ip:~/task1/task1_face_detected.jpg ./
```

**Option 2: Use a Web Browser**
Set up a simple HTTP server:
```bash
cd task1
python3 -m http.server 8000
```
Then visit: `http://jetson-ip:8000` in your browser

**Option 3: View on Jetson with Display**
```bash
# If you have a display connected
eog task1_face_detected.jpg  # Eye of GNOME image viewer
# or
display task1_face_detected.jpg  # ImageMagick
```

---

## Problem 6: tegrastats Command Not Found

**Applies to:** Task 2, Task 3, Assignment 2, Assignment 3

### The Problem

When running Task 2 or Task 3, you see:

```
Error reading GPU stats: [Errno 2] No such file or directory: 'tegrastats'
```

### Why This Happens

`tegrastats` is a **Jetson-specific command** for monitoring GPU/system stats. This error occurs when:
- Running on a non-Jetson device (regular PC, laptop, etc.)
- Jetson tools are not in the PATH
- Running on unsupported Jetson model

### Solution 1: Expected Behavior on Non-Jetson Devices

This is **not actually an error** - it's expected behavior! The tasks handle this gracefully:

```python
def get_gpu_usage():
    try:
        # Try to run tegrastats
        output = subprocess.check_output("tegrastats ...", shell=True)
        return output.decode("utf-8").strip()
    except Exception as e:
        return f"Error reading GPU stats: {e}"  # ← Graceful handling
```

**The script continues to run and complete successfully!**

Output will show:
```
CPU Usage: 45.2%
GPU Stats:
Error reading GPU stats: [Errno 2] No such file or directory: 'tegrastats'
```

This is fine - your detection still works, you just don't get GPU stats.

### Solution 2: On Jetson Nano - Verify tegrastats

If you ARE on a Jetson Nano but still get this error:

```bash
# Check if tegrastats exists
which tegrastats

# Try running it manually
tegrastats --interval 1000 --count 1
```

If not found, add to PATH:
```bash
export PATH=$PATH:/usr/bin
```

### Solution 3: Skip GPU Monitoring (For Testing)

You can modify the code to skip GPU monitoring:

```python
# Comment out GPU monitoring section
# cpu_usage = psutil.cpu_percent(interval=1)
# gpu_stats = get_gpu_usage()
# print(f"\nCPU Usage: {cpu_usage}%")
# print("GPU Stats:")
# print(gpu_stats)

print("\n⚠️  System monitoring skipped (not on Jetson)")
```

### What tegrastats Shows (On Jetson Nano)

When working on a Jetson Nano, tegrastats provides:
- RAM usage
- SWAP usage
- CPU usage per core with frequencies
- GPU frequency and usage
- EMC frequency
- Temperature sensors (PLL, CPU, PMIC, GPU, etc.)

Example output:
```
RAM 2295/3956MB (lfb 14x4MB) SWAP 661/1978MB (cached 47MB) 
CPU [13%@1479,off,off,off] EMC_FREQ 3%@1600 GR3D_FREQ 40%@318 
PLL@35.5C CPU@39C PMIC@50C GPU@37C AO@45C thermal@38.25C
```

---

## Common Troubleshooting Tips

### 1. Image File Not Found

**Error:**
```
Failed to load 'image.jpg'
```

**Solutions:**
- Verify the image file is in the **same folder** as your Python script
- Check the filename (case-sensitive on Linux)
- Try using an absolute path: `/home/username/task1/image.jpg`
- List files in directory: `ls -la`

**Test:**
```python
import os
print("Current directory:", os.getcwd())
print("Files here:", os.listdir('.'))
print("Image exists:", os.path.exists('image.jpg'))
```

### 2. Permission Denied When Saving Output

**Error:**
```
Permission denied: 'task1_face_detected.jpg'
```

**Solutions:**
- Check folder write permissions: `ls -la`
- Make folder writable: `chmod +w .`
- Run script from your home directory
- Check disk space: `df -h`

### 3. Script Runs But No Output File

**Possible Causes:**
- Script exited early due to error (check full output)
- Writing to a different directory than expected
- Filename typo in code

**Debug:**
```python
import os
output_path = "task1_face_detected.jpg"
try:
    cv2.imwrite(output_path, img)
    print(f"✅ Saved to: {os.path.abspath(output_path)}")
except Exception as e:
    print(f"❌ Failed to save: {e}")
```

### 4. "Image is empty" or Black Output

**Possible Causes:**
- Image didn't load properly (`img` is None)
- Wrong color space
- Image processing error

**Fix:**
```python
# Always check if image loaded
img = cv2.imread("image.jpg")
if img is None:
    raise SystemExit("❌ Failed to load image!")

print(f"✅ Image shape: {img.shape}")  # Should show (height, width, 3)
```

### 5. Slow Performance

**Tips for Faster Processing:**

```python
# Resize large images
max_dimension = 800
scale = max_dimension / max(img.shape[:2])
if scale < 1.0:
    img = cv2.resize(img, (int(img.shape[1]*scale), int(img.shape[0]*scale)))
    print(f"✅ Resized to {img.shape[1]}x{img.shape[0]} for faster processing")
```

**Performance Comparison:**
- Task 1 (Haar Cascade): ~40ms per image (fast)
- Task 3 (HOG): ~100-150ms per image (slower but more accurate)
- Task 3 (DNN): ~80-120ms per image (balanced)

### 6. Compare Detection Results Between Methods

**Quick Test Script:**

```python
import cv2
import time

img = cv2.imread("image.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Test Haar Cascade
cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
start = time.time()
haar_faces = cascade.detectMultiScale(gray, 1.1, 5, minSize=(30,30))
haar_time = time.time() - start

print(f"Haar Cascade: {len(haar_faces)} faces in {haar_time:.3f}s")
```

---

## OpenCV Build Process Summary

If you need to build OpenCV from source on your Jetson Nano (to enable CUDA/GPU acceleration):

| Step | Command | Description |
|------|---------|-------------|
| 1 | `git clone https://github.com/opencv/opencv.git` | Download OpenCV source code |
| 2 | `cd opencv && mkdir build && cd build` | Create build directory |
| 3 | `cmake -D CMAKE_BUILD_TYPE=RELEASE -D WITH_CUDA=ON ..` | Configure with CUDA support |
| 4 | `make -j4` | Compile using 4 CPU cores |
| 5 | `sudo make install` | Install OpenCV system-wide |
| 6 | `sudo ldconfig` | Refresh library paths |
| 7 | `python3 -c "import cv2; print(cv2.__version__)"` | Verify installation |
| 8 | Test CUDA functions | Confirm GPU acceleration |

**Important Notes:**
- Building OpenCV from source can take **2-4 hours** on Jetson Nano
- Ensure adequate cooling and power supply (5V 4A recommended)
- Monitor temperature during build: `watch -n 1 tegrastats`
- For Jetson Nano, use `-j2` or `-j3` to avoid overheating

**Quick Build Command:**
```bash
cmake -D CMAKE_BUILD_TYPE=RELEASE \
      -D WITH_CUDA=ON \
      -D CUDA_ARCH_BIN="5.3" \
      -D WITH_CUBLAS=ON \
      -D WITH_CUDNN=ON \
      -D OPENCV_DNN_CUDA=ON \
      -D ENABLE_FAST_MATH=ON \
      -D CUDA_FAST_MATH=ON \
      -D BUILD_EXAMPLES=OFF \
      ..
```

---

## Quick Reference

### File Structure Checklist

```
starter_kit1/
├── task1/
│   ├── detect_person_haar.py
│   ├── image.jpg
│   ├── haarcascade_frontalface_default.xml  ← Required!
│   └── task1_face_detected.jpg              ← Generated output
│
├── task2/
│   ├── detect_person_haar_sys.py
│   ├── image.jpg
│   ├── haarcascade_frontalface_default.xml  ← Required!
│   └── task2_face_detected.jpg              ← Generated output
│
└── task3/
    ├── detect_face_hog.py
    ├── image.jpg
    ├── deploy.prototxt                      ← Auto-downloaded (DNN)
    ├── res10_300x300_ssd_iter_140000.caffemodel  ← Auto-downloaded (DNN)
    └── task3_face_detected_hog.jpg          ← Generated output
```

### Test Commands

```bash
# Verify OpenCV
python3 -c "import cv2; print('OpenCV:', cv2.__version__)"

# Verify psutil
python3 -c "import psutil; print('psutil:', psutil.__version__)"

# Check if dlib available
python3 -c "import dlib; print('dlib available')" 2>/dev/null || echo "dlib not available (DNN fallback will be used)"

# Test Haar Cascade file
python3 -c "import cv2; fc = cv2.CascadeClassifier('haarcascade_frontalface_default.xml'); print('Cascade: OK' if not fc.empty() else 'Cascade: FAIL')"

# Run task tests
cd task1 && python3 detect_person_haar.py
cd task2 && python3 detect_person_haar_sys.py
cd task3 && python3 detect_face_hog.py
```

### Detection Parameters Quick Guide

**Haar Cascade (Tasks 1 & 2):**
```python
faces = face_cascade.detectMultiScale(
    gray,
    scaleFactor=1.1,    # 1.05-1.3 (lower = more sensitive)
    minNeighbors=5,     # 3-8 (lower = more detections)
    minSize=(30, 30)    # (20,20)-(100,100) (smaller = detect smaller faces)
)
```

**HOG/DNN (Task 3):**
```python
# dlib HOG
faces = hog_detector(gray, 1)  # 0-2 (higher = detect smaller faces, slower)

# OpenCV DNN
confidence_threshold = 0.5  # 0.3-0.7 (lower = more detections)
```

---

## Summary

This troubleshooting guide covered:

✅ **Verifying OpenCV installation** and checking GPU support  
✅ **Problem 1:** Haar Cascade XML file path issues (Tasks 1 & 2)  
✅ **Problem 2:** No faces detected - parameter tuning  
✅ **Problem 3:** Missing psutil for system monitoring (Tasks 2 & 3)  
✅ **Problem 4:** dlib not found - automatic DNN fallback (Task 3)  
✅ **Problem 5:** GUI display errors in headless environments  
✅ **Problem 6:** tegrastats not available on non-Jetson systems  
✅ **Common Tips:** File handling, permissions, performance optimization  
✅ **OpenCV Build Process:** Building from source with CUDA support  

---

**Remember:** Most "errors" in Tasks 2 and 3 (like tegrastats or dlib not found) are handled gracefully by the code and don't prevent the tasks from completing successfully!

For additional help, refer to:
- Task reference files (`task1/`, `task2/`, `task3/`)
- `how_to_get_started.md` for complete learning guide
- OpenCV Documentation: [https://docs.opencv.org/](https://docs.opencv.org/)
- Jetson Community: [https://forums.developer.nvidia.com/](https://forums.developer.nvidia.com/)

---

**Happy debugging! 🚀**

