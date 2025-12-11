import pyautogui
import time

from PIL import ImageStat

#rgb = 206, 38, 54

pyautogui.FAILSAFE = True
print("three seconds to get into position")
time.sleep(3)
mx, my = pyautogui.position()

SIZE = 20
screen_w, screen_h = pyautogui.size()

left = mx
top = my
width = SIZE//2
height = SIZE//2

region = (left,top,width,height)

def color(region_box):
    img = pyautogui.screenshot(region=region_box)
    stat = ImageStat.Stat(img)
    r, g, b = stat.mean[:3]
    return (r, g, b)

initial_color = (206, 38, 54)

COLOR_THRESHOLD = 40

def color_dist(c1,c2):
    return ((c1[0] - c2[0]) ** 2 + (c1[1] - c2[1]) ** 2 + (c1[2] - c2[2]) ** 2) ** 0.5  # euclidian color distance

try:
    pyautogui.click(left, top)

    while True:
        current = color(region)
        dist = color_dist(initial_color, current)

        if dist > COLOR_THRESHOLD:
            pyautogui.click(left, top)
            break

        time.sleep(0.0001)
except KeyboardInterrupt:
    print("exited")