from pynput.keyboard import Key, Controller
import time

keyboard = Controller()

def pressTab():
    keyboard.press(Key.tab)
    time.sleep(sleep_duration)
    keyboard.release(Key.tab)
    time.sleep(sleep_duration)

def pressDown():
    keyboard.release(Key.down)
    time.sleep(sleep_duration)

def fill_feedback(feedback_option):
    pressDown()
    time.sleep(sleep_duration)
    for _ in range(8):
        pressDown()
    pressTab()
    keyboard.type(feedback_option)

print("Select the speed for automation:")
print("1. Slow\n2. Medium (Recommended)\n3. Fast")

speed_selection = input("Enter the number for your desired speed: ")

speed_options = {"1": 1, "2": 0.4, "3": 0.2}
sleep_duration = speed_options.get(speed_selection, 0.4)

print("Select your feedback option:")
print("1. Average\n2. Good\n3. Poor\n4. Very Good")

feedback_selection = input("Enter the number for your feedback option: ")

feedback_options = {"1": "Average", "2": "Good", "3": "Poor", "4": "Very Good"}
selected_option = feedback_options.get(feedback_selection, "Average")

print(f"Prepare to give feedback at {speed_selection} speed! Position your cursor at the first index...")

time.sleep(5)

while True:
    fill_feedback(selected_option)
