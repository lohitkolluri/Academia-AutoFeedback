from pynput.keyboard import Key, Controller
import time

# Create a keyboard controller instance for input automation
keyboard = Controller()

# Function to simulate pressing and releasing the Tab key
def pressTab():
    keyboard.press(Key.tab)
    time.sleep(0.01)  # Reduced sleep duration
    keyboard.release(Key.tab)
    time.sleep(0.01)  # Reduced sleep duration

# Function to simulate pressing and releasing the Down arrow key
def pressDown():
    keyboard.release(Key.down)
    time.sleep(0.01)  # Reduced sleep duration

# Function to automate the feedback form filling process based on user selection
def fill_feedback(feedback_option):
    pressDown()  # Navigate to the feedback section
    time.sleep(0.5)  # Reduced sleep duration
    for _ in range(8):  # Press Down arrow multiple times for detailed feedback
        pressDown()
    pressTab()  # Move to the next feedback section
    
    # Replace "Selection" with the user's feedback option
    keyboard.type(feedback_option)

# Prompt the user to select a feedback option
print("Select your feedback option:")
print("1. Average")
print("2. Good")
print("3. Poor")
print("4. Very Good")

# Get user input for feedback selection
feedback_selection = input("Enter the number corresponding to your feedback option: ")

# Map user input to the corresponding feedback option
feedback_options = {
    "1": "Average",
    "2": "Good",
    "3": "Poor",
    "4": "Very Good"
}

selected_option = feedback_options.get(feedback_selection, "Average")  # Default to "Average" if input is invalid

# Inform the user before starting the automated feedback
print("Prepare to give your feedback! Position your cursor at the first index...")

# Allow a few seconds for the user to get ready
time.sleep(3)

# Infinite loop for continuous feedback form filling
while True:
    fill_feedback(selected_option)
