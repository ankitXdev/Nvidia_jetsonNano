# NVIDIA Cloud Lab by AiProff.ai | Basic Linux Commands Guide

## 📋 Introduction

Welcome to the **Basic Linux Commands Guide**! If you're new to Linux or the command line interface, this guide will teach you the essential commands you need to navigate, manage files, and work with your Jetson Nano or any Linux system.

This guide is designed for complete beginners and will help you become comfortable with the terminal.

---

## 🖥️ What is the Terminal?

The **terminal** (also called command line, shell, or console) is a text-based interface where you type commands to interact with your computer. While it might seem intimidating at first, it's a powerful tool that gives you precise control over your system.

### Opening the Terminal

**On Jetson Nano / Ubuntu:**
- Press `Ctrl + Alt + T`
- Or search for "Terminal" in applications

**On Windows (if using WSL):**
- Open "Ubuntu" or "WSL" from the Start menu

---

## 📂 Navigation Commands

### `pwd` - Print Working Directory

Shows your current location in the file system.

```bash
pwd
```

**Example Output:**
```
/home/username
```

**When to use:** When you're lost and need to know where you are.

---

### `ls` - List Directory Contents

Lists files and folders in the current directory.

```bash
# Basic listing
ls

# Detailed listing (with permissions, size, date)
ls -l

# Show hidden files (files starting with .)
ls -a

# Detailed listing including hidden files
ls -la

# Human-readable file sizes
ls -lh
```

**Example Output:**
```
assignment1  assignment2  assignment3  task1  task2  task3
```

**Common Options:**
- `-l` = long format (detailed information)
- `-a` = show all files (including hidden)
- `-h` = human-readable sizes (KB, MB, GB)
- `-t` = sort by modification time
- `-r` = reverse order

---

### `cd` - Change Directory

Moves you to a different folder.

```bash
# Go to a specific folder
cd assignment1

# Go back to parent directory
cd ..

# Go back two levels
cd ../..

# Go to home directory
cd ~
# or simply
cd

# Go to previous directory
cd -

# Go to root directory
cd /
```

**Examples:**
```bash
# Navigate to starter kit 1
cd /home/username/jetson_nano_kits/stater_kit1

# Go into task1 folder
cd task1

# Go back to stater_kit1
cd ..

# Go to assignment1
cd assignment1
```

---

## 📝 File Management Commands

### `mkdir` - Make Directory

Creates a new folder.

```bash
# Create a single folder
mkdir my_project

# Create multiple folders at once
mkdir folder1 folder2 folder3

# Create nested folders (parent directories too)
mkdir -p projects/python/assignment1

# Create folder with specific permissions
mkdir -m 755 my_folder
```

**Example:**
```bash
# Create a new project folder
mkdir opencv_project

# Create nested structure
mkdir -p experiments/test1/results
```

---

### `touch` - Create Empty File

Creates a new empty file or updates the timestamp of an existing file.

```bash
# Create a single file
touch myfile.txt

# Create multiple files
touch file1.py file2.py file3.py

# Create file with specific extension
touch test.jpg notes.md script.sh
```

**Example:**
```bash
# Create a Python script file
touch my_detection.py

# Create multiple image files
touch image1.jpg image2.jpg image3.jpg
```

---

### `cp` - Copy Files/Folders

Copies files or directories from one location to another.

```bash
# Copy a file
cp source.txt destination.txt

# Copy file to another directory
cp myfile.txt /path/to/destination/

# Copy multiple files to a directory
cp file1.txt file2.txt file3.txt /destination/

# Copy a folder and its contents (recursive)
cp -r folder1 folder2

# Copy with confirmation before overwriting
cp -i source.txt destination.txt

# Preserve file attributes (permissions, timestamps)
cp -p file.txt backup.txt
```

**Example:**
```bash
# Copy sample image from task1 to assignment1
cp task1/human.jpg assignment1/

# Backup your assignment
cp assignment1.py assignment1_backup.py

# Copy entire folder
cp -r task1 task1_backup
```

---

### `mv` - Move or Rename Files/Folders

Moves files/folders to a new location or renames them.

```bash
# Rename a file
mv oldname.txt newname.txt

# Move file to another directory
mv myfile.txt /path/to/destination/

# Move multiple files
mv file1.txt file2.txt file3.txt /destination/

# Move and rename at the same time
mv old_folder/file.txt new_folder/newname.txt

# Move with confirmation before overwriting
mv -i source.txt destination.txt
```

**Example:**
```bash
# Rename your script
mv detect.py detect_person.py

# Move output to results folder
mv output.jpg results/

# Reorganize files
mv *.jpg images/
```

---

### `rm` - Remove Files/Folders

Deletes files or directories. **⚠️ BE CAREFUL - This is permanent!**

```bash
# Remove a file
rm myfile.txt

# Remove multiple files
rm file1.txt file2.txt file3.txt

# Remove with confirmation prompt
rm -i file.txt

# Remove a folder and all its contents (recursive)
rm -r folder_name

# Force remove without confirmation (dangerous!)
rm -rf folder_name

# Remove all .txt files in current directory
rm *.txt
```

**Example:**
```bash
# Delete a temporary file
rm temp.txt

# Delete backup folder
rm -r backup_folder

# Delete all output images
rm *_detected.jpg
```

**⚠️ WARNING:** 
- `rm` permanently deletes files (no trash/recycle bin)
- `rm -rf` is extremely dangerous - double-check before using
- Always verify the path before deleting

---

## 📄 File Viewing Commands

### `cat` - Display File Contents

Shows the entire contents of a file.

```bash
# Display file contents
cat myfile.txt

# Display multiple files
cat file1.txt file2.txt

# Display with line numbers
cat -n myfile.txt

# Combine files into a new file
cat file1.txt file2.txt > combined.txt
```

**Example:**
```bash
# View your Python script
cat detect_person_hog.py

# View README
cat how_to_get_started.md
```

---

### `less` - View File with Scrolling

Opens a file in a scrollable viewer (better for large files).

```bash
less myfile.txt
```

**Navigation inside `less`:**
- `Space` = scroll down one page
- `b` = scroll up one page
- `↓` or `j` = scroll down one line
- `↑` or `k` = scroll up one line
- `/search_term` = search for text
- `n` = next search result
- `q` = quit

**Example:**
```bash
# View a long log file
less output.log
```

---

### `head` - View First Lines

Shows the first few lines of a file (default: 10 lines).

```bash
# Show first 10 lines
head myfile.txt

# Show first 20 lines
head -n 20 myfile.txt

# Show first 5 lines
head -5 myfile.txt
```

---

### `tail` - View Last Lines

Shows the last few lines of a file (default: 10 lines).

```bash
# Show last 10 lines
tail myfile.txt

# Show last 20 lines
tail -n 20 myfile.txt

# Follow file in real-time (useful for logs)
tail -f logfile.txt
```

**Example:**
```bash
# Monitor a log file in real-time
tail -f training.log
```

---

## ✏️ Text Editing Commands

### `nano` - Simple Text Editor

Easy-to-use terminal text editor, perfect for beginners.

```bash
# Open existing file or create new one
nano myfile.txt

# Open file at specific line number
nano +25 myfile.py

# Open file in read-only mode
nano -v myfile.txt
```

**Nano Keyboard Shortcuts:**
- `Ctrl + O` = Save file (Write Out)
- `Ctrl + X` = Exit nano
- `Ctrl + K` = Cut current line
- `Ctrl + U` = Paste
- `Ctrl + W` = Search
- `Ctrl + \` = Search and replace
- `Ctrl + G` = Help menu
- `Alt + U` = Undo
- `Alt + E` = Redo

**Example Workflow:**
```bash
# Create and edit a Python script
nano my_script.py

# Type your code...
# Press Ctrl + O to save
# Press Enter to confirm filename
# Press Ctrl + X to exit
```

---

### `vim` - Advanced Text Editor

Powerful but has a steeper learning curve. Has different modes.

```bash
# Open file
vim myfile.txt
```

**Basic Vim Commands:**
- Press `i` = Enter INSERT mode (start typing)
- Press `Esc` = Exit INSERT mode (back to NORMAL mode)
- Type `:w` = Save file
- Type `:q` = Quit
- Type `:wq` = Save and quit
- Type `:q!` = Quit without saving

**Getting Started with Vim:**
```bash
# Open file
vim script.py

# Press 'i' to start editing
# Type your code...
# Press 'Esc' when done
# Type ':wq' and press Enter to save and exit
```

---

## 🔍 Search and Find Commands

### `find` - Search for Files

Searches for files and directories based on criteria.

```bash
# Find files by name
find . -name "myfile.txt"

# Find all .jpg files
find . -name "*.jpg"

# Find all .py files (case insensitive)
find . -iname "*.py"

# Find files in specific directory
find /home/username -name "*.txt"

# Find files modified in last 7 days
find . -mtime -7

# Find files larger than 10MB
find . -size +10M

# Find and delete files
find . -name "*.tmp" -delete
```

**Example:**
```bash
# Find all Python files in current directory
find . -name "*.py"

# Find all image files
find . -name "*.jpg" -o -name "*.png"

# Find your assignment files
find . -name "assignment*.py"
```

---

### `grep` - Search Text in Files

Searches for text patterns within files.

```bash
# Search for text in a file
grep "search_term" myfile.txt

# Case-insensitive search
grep -i "search_term" myfile.txt

# Search recursively in all files
grep -r "search_term" .

# Show line numbers
grep -n "search_term" myfile.txt

# Search for whole word only
grep -w "search_term" myfile.txt

# Show files that don't contain the pattern
grep -v "search_term" myfile.txt

# Search in specific file types
grep -r "import cv2" --include="*.py"
```

**Example:**
```bash
# Find all files that import cv2
grep -r "import cv2" .

# Find where a function is used
grep -n "detectMultiScale" *.py

# Search for TODO comments
grep -r "TODO" .
```

---

## 📊 System Information Commands

### `whoami` - Current User

Shows your current username.

```bash
whoami
```

**Example Output:**
```
nvidia
```

---

### `hostname` - Computer Name

Shows your computer's hostname.

```bash
hostname
```

---

### `df` - Disk Space

Shows disk space usage.

```bash
# Basic disk usage
df

# Human-readable format
df -h

# Show specific filesystem
df -h /home
```

**Example Output:**
```
Filesystem      Size  Used Avail Use% Mounted on
/dev/mmcblk0p1   29G   15G   13G  54% /
```

---

### `du` - Directory Size

Shows size of directories and files.

```bash
# Size of current directory
du -sh .

# Size of specific directory
du -sh assignment1/

# Size of all subdirectories
du -sh */

# Detailed breakdown
du -h --max-depth=1
```

**Example:**
```bash
# Check size of your project folders
du -sh task1 task2 task3

# Find largest directories
du -h --max-depth=1 | sort -hr
```

---

### `free` - Memory Usage

Shows RAM and swap memory usage.

```bash
# Basic memory info
free

# Human-readable format
free -h

# Show in megabytes
free -m
```

---

### `top` - System Monitor

Real-time view of system processes and resource usage.

```bash
top
```

**Navigation in `top`:**
- `q` = quit
- `M` = sort by memory usage
- `P` = sort by CPU usage
- `k` = kill a process (enter PID)

**Alternative:** `htop` (more user-friendly, needs installation)
```bash
sudo apt-get install htop
htop
```

---

## 🔐 Permissions and Ownership

### `chmod` - Change File Permissions

Modifies file/folder permissions (read, write, execute).

```bash
# Make file executable
chmod +x script.sh

# Remove write permission
chmod -w file.txt

# Set specific permissions (owner=rwx, group=rx, others=r)
chmod 754 myfile.txt

# Make Python script executable
chmod +x my_script.py

# Change permissions recursively
chmod -R 755 folder/
```

**Permission Numbers:**
- `7` = read + write + execute (rwx)
- `6` = read + write (rw-)
- `5` = read + execute (r-x)
- `4` = read only (r--)
- `0` = no permissions (---)

---

### `chown` - Change Ownership

Changes the owner of files/folders.

```bash
# Change owner
sudo chown username file.txt

# Change owner and group
sudo chown username:groupname file.txt

# Change ownership recursively
sudo chown -R username:groupname folder/
```

---

## 🐍 Python-Specific Commands

### Running Python Scripts

```bash
# Run Python script
python3 script.py

# Run with verbose output
python3 -v script.py

# Check Python version
python3 --version
```

**Example:**
```bash
# Run your detection script
python3 detect_person_hog.py

# Run assignment
python3 assignment1.py
```

---

### `pip` - Python Package Manager

```bash
# Install a package
pip3 install opencv-python

# Install specific version
pip3 install opencv-python==4.5.3

# Install from requirements file
pip3 install -r requirements.txt

# List installed packages
pip3 list

# Show package info
pip3 show opencv-python

# Uninstall package
pip3 uninstall opencv-python

# Upgrade package
pip3 install --upgrade opencv-python
```

**Example:**
```bash
# Install required packages for assignments
pip3 install opencv-python psutil numpy
```

---

## 🌐 Network Commands

### `ping` - Test Connection

Tests network connectivity to a host.

```bash
# Ping a website
ping google.com

# Ping with specific count
ping -c 4 google.com

# Stop pinging with Ctrl + C
```

---

### `wget` - Download Files

Downloads files from the internet.

```bash
# Download a file
wget https://example.com/file.zip

# Download with custom filename
wget -O myfile.zip https://example.com/file.zip

# Continue interrupted download
wget -c https://example.com/largefile.zip
```

---

### `curl` - Transfer Data

Downloads or uploads data from/to servers.

```bash
# Download file
curl -O https://example.com/file.txt

# Download and save with custom name
curl -o myfile.txt https://example.com/file.txt

# Display webpage content
curl https://example.com
```

---

## 🔧 System Management Commands

### `sudo` - Run as Administrator

Executes commands with superuser (root) privileges.

```bash
# Install software
sudo apt-get install package-name

# Edit system file
sudo nano /etc/config.conf

# Reboot system
sudo reboot

# Shutdown system
sudo shutdown now
```

**⚠️ Important:** Use `sudo` carefully - it has full system access!

---

### Package Management (Ubuntu/Debian)

```bash
# Update package list
sudo apt-get update

# Upgrade all packages
sudo apt-get upgrade

# Install a package
sudo apt-get install package-name

# Remove a package
sudo apt-get remove package-name

# Search for a package
apt-cache search keyword

# Clean up unused packages
sudo apt-get autoremove
```

**Example:**
```bash
# Install Python and OpenCV dependencies
sudo apt-get update
sudo apt-get install python3-pip python3-opencv
```

---

## 📋 Useful Shortcuts and Tips

### Terminal Shortcuts

- `Ctrl + C` = Cancel/stop current command
- `Ctrl + Z` = Suspend current process
- `Ctrl + D` = Exit terminal/logout
- `Ctrl + L` = Clear screen (same as `clear`)
- `Ctrl + A` = Move cursor to beginning of line
- `Ctrl + E` = Move cursor to end of line
- `Ctrl + U` = Delete from cursor to beginning of line
- `Ctrl + K` = Delete from cursor to end of line
- `Ctrl + R` = Search command history
- `↑` / `↓` = Navigate command history
- `Tab` = Auto-complete filenames/commands

---

### Command Chaining

```bash
# Run commands sequentially (one after another)
cd assignment1 ; ls ; pwd

# Run second command only if first succeeds
cd assignment1 && python3 assignment1.py

# Run second command only if first fails
cd assignment1 || echo "Directory not found"

# Run command in background
python3 long_script.py &
```

---

### Redirects and Pipes

```bash
# Save output to file (overwrite)
ls > files.txt

# Append output to file
ls >> files.txt

# Redirect error messages
python3 script.py 2> errors.txt

# Redirect both output and errors
python3 script.py > output.txt 2>&1

# Pipe output to another command
ls | grep ".py"

# Count lines in file
cat file.txt | wc -l
```

---

## 🎓 Practice Exercises

Try these exercises to practice what you've learned:

### Exercise 1: Navigation and File Creation
```bash
# 1. Check your current location
pwd

# 2. List all files
ls -la

# 3. Create a new folder called "practice"
mkdir practice

# 4. Go into that folder
cd practice

# 5. Create three empty files
touch file1.txt file2.txt file3.txt

# 6. List files to verify
ls

# 7. Go back to parent directory
cd ..
```

### Exercise 2: Working with Starter Kit
```bash
# 1. Navigate to starter kit 1
cd stater_kit1

# 2. List all directories
ls

# 3. Go into task1
cd task1

# 4. View the Python script
cat detect_person_hog.py

# 5. Copy the sample image to assignment1
cp human.jpg ../assignment1/

# 6. Navigate to assignment1
cd ../assignment1

# 7. Verify the file was copied
ls
```

### Exercise 3: Editing Files
```bash
# 1. Create a new Python file
nano test.py

# 2. Type some code:
# print("Hello from Linux!")

# 3. Save with Ctrl+O, exit with Ctrl+X

# 4. Run the script
python3 test.py

# 5. View the file contents
cat test.py
```

---

## 🆘 Getting Help

### Built-in Help

```bash
# Show command manual
man command_name

# Show brief help
command_name --help

# Search manual pages
man -k keyword

# Get info about a command
info command_name
```

**Example:**
```bash
# Learn more about ls
man ls

# Quick help for cp
cp --help
```

---

## 📝 Quick Reference Cheat Sheet

| Command | Purpose | Example |
|---------|---------|---------|
| `pwd` | Show current directory | `pwd` |
| `ls` | List files | `ls -la` |
| `cd` | Change directory | `cd assignment1` |
| `mkdir` | Create directory | `mkdir my_folder` |
| `touch` | Create file | `touch file.txt` |
| `cp` | Copy | `cp file.txt backup.txt` |
| `mv` | Move/rename | `mv old.txt new.txt` |
| `rm` | Delete | `rm file.txt` |
| `cat` | View file | `cat script.py` |
| `nano` | Edit file | `nano file.txt` |
| `grep` | Search text | `grep "search" file.txt` |
| `find` | Find files | `find . -name "*.py"` |
| `chmod` | Change permissions | `chmod +x script.sh` |
| `python3` | Run Python | `python3 script.py` |
| `pip3` | Install packages | `pip3 install package` |
| `sudo` | Run as admin | `sudo apt-get update` |

---

## 🎯 Next Steps

Now that you know basic Linux commands:

1. **Practice regularly** - The more you use the terminal, the more comfortable you'll become
2. **Explore the file system** - Navigate around and see how things are organized
3. **Read the manuals** - Use `man` to learn more about commands
4. **Start coding** - Use these commands to work through the starter kit assignments
5. **Experiment safely** - Create a test folder and practice commands there

---

## 💡 Pro Tips

1. **Use Tab for auto-completion** - Start typing and press Tab to complete filenames/commands
2. **Use arrow keys** - ↑ and ↓ to scroll through previous commands
3. **Be careful with `rm`** - Always double-check before deleting files
4. **Read error messages** - They usually tell you exactly what's wrong
5. **Create backups** - Before making major changes, copy important files
6. **Use `ls` often** - Keep track of where you are and what files exist
7. **Start simple** - Master basic commands before moving to advanced ones

---

**Happy Learning! 🚀**

Remember: Everyone starts as a beginner. Take your time, practice regularly, and don't be afraid to make mistakes - that's how you learn!

