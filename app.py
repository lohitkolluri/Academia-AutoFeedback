from pynput.keyboard import Key, Controller
import time

# Create a Controller instance from pynput to control the keyboard
keyboard = Controller()

# Function to simulate pressing and releasing the Tab key
def pressTab():
    keyboard.press(Key.tab)
    time.sleep(0.1)
    keyboard.release(Key.tab)
    time.sleep(0.1)

# Function to simulate pressing and releasing the Down arrow key
def pressDown():
    keyboard.press(Key.down)
    time.sleep(0.1)
    keyboard.release(Key.down)
    time.sleep(0.1)

# Function to fill feedback by pressing Down arrow multiple times, waiting, and then pressing Tab
def fill_feedback():
    pressDown()  # Press Down arrow
    time.sleep(2)  # Wait for 2 seconds
    pressDown()  # Press Down arrow several times
    pressDown()
    pressDown()
    pressDown()
    pressDown()
    pressDown()
    pressDown()
    pressDown()
    pressDown()
    pressTab()  # Press Tab

# Print a message to inform the user
print("Get ready, and point your cursor at the first index position...")
time.sleep(3)  # Wait for 3 seconds

# Infinite loop to continuously fill feedback
while True:
    fill_feedback()
