import pyautogui
import time
import pytesseract
from PIL import Image
from tkinter import *
from tkinter import ttk

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"


CHAR_GAP = 0.01

try:
    while True:
        x1, y1 = pyautogui.position()
        positionStr = 'X: ' + str(x1).rjust(4) + ' Y: ' + str(y1).rjust(4)
        print(positionStr, end='')
        print('\b' * len(positionStr), end='', flush=True)
except KeyboardInterrupt:
    print('\n')

try:
    while True:
        x2, y2 = pyautogui.position()
        positionStr = 'X: ' + str(x2).rjust(4) + ' Y: ' + str(y2).rjust(4)
        print(positionStr, end='')
        print('\b' * len(positionStr), end='', flush=True)
except KeyboardInterrupt:
    print('\n')

left = min(x1, x2)
top = min(y1, y2)
right = max(x1, x2)
bottom = max(y1, y2)
width = right - left
height = bottom - top

region=(left,top,width,height)
pyautogui.screenshot("text.png",region=region)
img = Image.open('text.png')

raw_text = pytesseract.image_to_string(img, config="--psm 6")
text = raw_text.strip().replace("\n", " ")

time.sleep(3)
pyautogui.write(text, interval=CHAR_GAP)
