import pyautogui
import time
pyautogui.FAILSAFE = True
pyautogui.PAUSE = .2

# USER EDIT SECTION
MESSAGE = "This is a test message"  # Write your message here in quotes
# Number of hours to run the program (input zero to run infinitely until failsafe cancel)
TIME = 1


t_end = time.time() + (TIME*3600)
time.sleep(5)   # Allow time to switch to browser window
pyautogui.press('esc')  # To begin the process after user ends the first chat


def bot(MESSAGE):
    time.sleep(5)
    pyautogui.write(MESSAGE, interval=.03)
    pyautogui.press('enter')
    time.sleep(3)
    pyautogui.press('esc', presses=4)


# Main loop
if (TIME == 0):
    while True:
        bot(MESSAGE)
else:
    while (time.time() < t_end):
        bot(MESSAGE)
