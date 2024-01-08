from pynput.keyboard import Key, Controller
import time

# Create a keyboard controller instance for input automation
keyboard = Controller()

# Function to simulate pressing and releasing the Tab key
def pressTab():
    keyboard.press(Key.tab)
    time.sleep(0.1)  # Small delay for a natural feel
    keyboard.release(Key.tab)
    time.sleep(0.1)  # Pause before the next action

# Function to simulate pressing and releasing the Down arrow key
def pressDown():
    keyboard.press(Key.down)
    time.sleep(0.1)  # Small delay for a natural feel
    keyboard.release(Key.down)
    time.sleep(0.1)  # Pause before the next action

# Function to automate the feedback form filling process
def fill_feedback():
    pressDown()  # Navigate to the feedback section
    time.sleep(2)  # Allow time for thoughtful consideration
    for _ in range(6):  # Press Down arrow multiple times for detailed feedback
        pressDown()
    pressTab()  # Move to the next feedback section

# Inform the user before starting the automated feedback
print("Prepare to give your feedback! Position your cursor at the first index...")

# Allow a few seconds for the user to get ready
time.sleep(3)

# Infinite loop for continuous feedback form filling
while True:
    fill_feedback()
