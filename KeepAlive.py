import pyautogui
import time

pyautogui.FAILSAFE = False

print("Now you can minimize this screen and move to other works this will never let your system automatically locked.")
print("However, by pressing CTRL+C you can terminate this program anytime.")
while True:
#  timer for 5 mins.
    time.sleep(300)
    pyautogui.press('ctrl')


