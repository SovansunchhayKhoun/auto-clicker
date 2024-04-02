import threading
import time
import pyautogui
import msvcrt  # Import for Windows compatibility
import os
import json

f = open('data.json')
data = json.load(f)
stop_event = threading.Event()

def clicker():
  count = 0
  click_position = data['click_pos_x'], data['click_pos_y']
  start()
  while count < data['click_count']:
    try:
      # get cursor position
      pyautogui.click(click_position)
      time.sleep(data['click_interval'])
      count = count + 1
      print(f"Clicked {count} times at {click_position}")
      if stop_event.is_set():
        os.system('cls')
        print(f"Clicked {count} times at {click_position}")
        count = 0
        break
    except:
      print(f"Error occurred")
      break
  stop_event.clear()

def input_listener():
  clicker_thread = None
  print("Waiting for input...")
  while True:
    key = get_single_char()
    if key == data['start']:
      clicker_thread = threading.Thread(target=clicker)
      clicker_thread.daemon = True
      clicker_thread.start()
    elif key == data['stop']:
      if clicker_thread is not None and clicker_thread.is_alive():
        stop_event.set()
      print('Program stopped...')
    elif key == data['exit']:
      print('Exiting program...')
      break
      
def get_single_char():
  while True:
    try:
      char = msvcrt.getch().decode('utf-8')  # Read a character without Enter
      if len(char) == 1:
          return char
      else:
          print("Please enter only one character.")  # Optional: Handle multi-character input
    except NameError:
      print("Input Error", NameError.name)

def start():
  count = 2
  while count > 0:
    print(f'Starting in {count}')
    count = count - 1
    time.sleep(1)

def main():
  thread1 = threading.Thread(target=input_listener)

  thread1.start()

  thread1.join()

main()
f.close()
