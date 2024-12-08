import threading
import time
import pyautogui
import json
import os
from pynput import keyboard  # Using pynput for key listening
import msvcrt  # Keeping this for single character input where needed

file_name = "./data/data.json"
stop_event = threading.Event()
clicker_thread = None


# Function to read data from JSON file
def read_file():
    try:
        with open(file_name) as f:
            return json.load(f)
    except Exception as e:
        print(f"Failed to open {file_name}: {e}")
        return None


# Function to perform the clicking operation
def clicker():
    data = read_file()
    if not data:
        return
    count = 0
    click_position = data["click_pos_x"], data["click_pos_y"]
    start()
    while count < data["click_count"]:
        try:
            pyautogui.click(click_position)
            time.sleep(data["click_interval"])
            count += 1
            print(f"Clicked {count} times at {click_position}")
            if stop_event.is_set():
                print(f"Clicking Stopped. Clicked {count} times at {click_position}")
                break
        except Exception as e:
            print(f"Error occurred during clicking: {e}")
            break
    stop_event.clear()


# Function to handle key presses
def on_press(key):
    global clicker_thread
    data = read_file()
    if not data:
        return

    try:
        if key.char == data["start"]:  # Start clicking on specific key press
            if not clicker_thread or not clicker_thread.is_alive():
                clicker_thread = threading.Thread(target=clicker)
                clicker_thread.start()
        elif key.char == data["stop"]:  # Stop clicking
            stop_event.set()
            print("Clicking stopped.")
        elif key.char == data["exit"]:  # Exit the program
            stop_event.set()
            if clicker_thread:
                clicker_thread.join()
            print("Exiting program...")
            return False  # This stops the key listener
    except AttributeError:  # Handle special keys like Ctrl, Shift, etc.
        pass


# Countdown before starting
def start():
    count = 2
    while count > 0:
        print(f"Starting in {count} seconds...")
        time.sleep(1)
        count -= 1


# Main function to start key listener
def main():
    print("Starting input listener...")
    # Start the listener in a non-blocking thread
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()  # Keep the listener running

    print("Program has exited.")


if __name__ == "__main__":
    main()

