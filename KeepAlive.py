import pyautogui
import time

pyautogui.FAILSAFE = False

print("Now you can minimize this screen and move to other works this will never let your system automatically locked")
print("By pressing CTRL+C you can terminate this program anytime")
while True:
    # time.sleep(240)
    # for i in range (0,50):
    #     pyautogui.moveTo(631,i*10)
    # time.sleep(300)
    # for i in range (0,1):
    #     pyautogui.press('prntscrn')
    time.sleep(300)
    pyautogui.press('prntscrn')
