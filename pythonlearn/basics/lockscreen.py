import pyautogui
import time

def timeIsUp():
    pyautogui.hotkey('win', 'r')
    pyautogui.typewrite('cmd\n')
    time.sleep(1)

    pyautogui.typewrite("rundll32.exe user32.dll, LockWorkStation\n")
