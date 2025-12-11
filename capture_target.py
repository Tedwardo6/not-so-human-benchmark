import pyautogui
import time

x1 = 2000
y1 = 500
x2 = 2050
y2 = 450

left = x1
top = y1
width = x2 - x1
height = y1 - y2

region = (left, top, width, height)
img = pyautogui.screenshot(region=region)
img.save("target.png")

print("Saved target.png in folder")