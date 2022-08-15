import pyautogui
import time
import pyperclip
import platform
VERSION = 1.2

# USER EDIT SECTION
MESSAGE = "This is a test message"  # Write your message here in quotes
# Number of hours to run the program (input zero to run infinitely until failsafe cancel)
TIME = 0

# SETUP
pyautogui.FAILSAFE = True
pyautogui.PAUSE = .2
pyperclip.copy(MESSAGE)
t_end = time.time() + (TIME*3600)


def bot():
    time.sleep(5)
    if(platform.system() == "Windows" or platform.system() == "Linux"):
        pyautogui.hotkey('ctrl', 'v')
    # hotkey function not working for macOS right now, will simplify when repaired
    elif(platform.system() == "Darwin"):
        pyautogui.keyDown('command')
        pyautogui.press('v')
        pyautogui.keyUp('command')
    pyautogui.press('enter')
    time.sleep(.5)
    pyautogui.press('esc', presses=4)


# Main
time.sleep(5)   # Allow time to switch to browser window
pyautogui.press('esc')  # To begin the process after user ends the first chat
if (TIME == 0):
    while True:
        bot()
else:
    while (time.time() < t_end):
        bot()
