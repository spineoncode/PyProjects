import sys
from pathlib import Path
import time
import pyautogui
import PIL.Image

commands = sys.argv

if len(commands) < 4:
    for i in range((4 - len(commands))):
        commands.append("")

path = Path(commands[1])

if path.exists():
    pass
elif commands[1] == "":
    commands[1] = "./"
else:
    print("Error: No such directory!")
    exit(0)

saveLoc = f"{commands[1]}Screenshot.png"

if commands[2] != "":
    saveLoc = f"{commands[1]}{commands[2]}.png"

if commands[3] != "":
    try:
        sleepTime = int()
    except:
        sleepTime = 0
else:
    sleepTime = 0

time.sleep(sleepTime)
img = pyautogui.screenshot()
img.save(saveLoc)
image = PIL.Image.open(saveLoc)
image.show(image)
