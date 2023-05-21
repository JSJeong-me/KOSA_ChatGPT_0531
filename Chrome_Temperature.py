
# > act as a Python programmer


# > Write Python code to accomplish the following steps

# Open a new tab in your default browser and navigate to Google.
# Wait a few seconds to let the page load.
# Use pyautogui to type 'current temperature' into the active field (this will be the Google search bar if Google was the active window and the page had time to load properly).
# Press the 'Enter' key to execute the search.


import time
import webbrowser
import pyautogui

# Open a new tab in your default browser and navigate to Google.
webbrowser.open('http://www.google.com')

# Wait a few seconds to let the page load.
time.sleep(3)

# Use pyautogui to type 'current temperature' into the active field.
pyautogui.typewrite('current temperature')
time.sleep(3)

# Press the 'Enter' key to execute the search.
pyautogui.press('enter')
