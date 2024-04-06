import threading
import time
import pyautogui
import msvcrt  # Import for Windows compatibility
import json
import os

file_name = "./_internal/data/data.json"
stop_event = threading.Event()


def read_file():
    try:
        f = open(file_name)
        return json.load(f)
    except:
        print(f"Failed to open {file_name}")
    try:
        f.close()
    except:
        print(f"Failed to close {file_name}")


def clicker():
    data = read_file()
    count = 0
    click_position = data["click_pos_x"], data["click_pos_y"]
    start()
    while count < data["click_count"]:
        try:
            # get cursor position
            pyautogui.click(click_position)
            time.sleep(data["click_interval"])
            count = count + 1
            print(f"Clicked {count} times at {click_position}")
            if stop_event.is_set():
                os.system("cls")
                print(f"Clicking Stopped. Clicked {count} times at {click_position}")
                count = 0
                break
        except:
            print(f"Error occurred")
            break
    stop_event.clear()


def input_listener():
    data = read_file()
    # clicker_thread = None
    print("Waiting for input...")
    while True:
        key = get_single_char()
        if key == data["start"]:
            clicker_thread = threading.Thread(target=clicker)
            clicker_thread.daemon = True
            clicker_thread.start()
        elif key == data["stop"]:
            # if clicker_thread is not None and clicker_thread.is_alive():
            stop_event.set()
            print("Program stopped...")
        elif key == data["exit"]:
            print("Exiting program...")
            clicker_thread.join()
            break


def get_single_char():
    while True:
        try:
            char = msvcrt.getch().decode("utf-8")  # Read a character without Enter
            if len(char) == 1:
                return char
            else:
                print(
                    "Please enter only one character."
                )  # Optional: Handle multi-character input
        except NameError:
            print("Input Error", NameError.name)


def start():
    count = 2
    while count > 0:
        print(f"Starting in {count}")
        time.sleep(1)
        count = count - 1


def main():
    thread1 = threading.Thread(target=input_listener)

    print("Starting input thread")

    thread1.daemon = True

    thread1.start()

    thread1.join()

    print("Thread Destroyed")


main()
