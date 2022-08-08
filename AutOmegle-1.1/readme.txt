Omegle Automation Bot
Made by Nadia
Discord: PhantomFoe#6012

This script will automate cycling through Omegle matches by sending a predetermined message and ending the chat. Note that this program uses the pyautogui library (https://pyautogui.readthedocs.io/en/latest/index.html), which controls the GUI during execution, meaning the user can't do much else while it's running. 

IMPORTANT: This script utilizes an infinite loop. To handle this, Pyautogui has a failsafe built in by default. To end the process, slam the mouse into the top-left corner of the screen. Do not attempt to use any hotkeys or keyboard shortcuts while this script is running. 

SETUP
- Make sure you have Python 3 installed (https://www.python.org/downloads/)
- run this command in your computer's command prompt/terminal:
    python3 -m pip install pyautogui
- Edit the variables in the User Edit Section to define the message to be sent and the number of hours the program will run (enter zero to run infinitely until the failsafe is activated)

USAGE
- Enter your interests on Omegle, continue to the first chat, end it, run the script, and switch back to the browser! The program will send your message to every match you connect to either until the failsafe is activated or the specified number of hours has elapsed.

Note: This program is very simple and does not have the ability to bypass temporary bans or captcha codes.