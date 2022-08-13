import pyautogui
from PIL import Image
import os
import time

dir_location = r'folder_location'
sleep_time = 5
counter = 1
max_counter = 5
while counter < max_counter:
    time.sleep(sleep_time)
    screenshot = pyautogui.screenshot()
    filename = str(max_counter) + '.png'
    screenshot_path = dir_location + filename
    screenshot.save(screenshot_path)
    print('screenhot taken for ' + filename)
    counter = counter + 1
