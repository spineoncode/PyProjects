import time
from plyer import notification

# This Can Be Fetched From A Server Too And Can Be Manipulated With An Application
toDoList = {
    "Make Android App": ["2128", "You Need To Get Working"],
    "Learn Rust Language": ["2129", "You Have To Learn a New Language"]
}

flag = True
try:
    while True:
        for task in toDoList.keys():
            nIcon = "./Images/Pic_1.ico" # This to can be changed by specifying icon's paths
            nTitle, nDescription = task, toDoList[task][1]

            if time.strftime("%H%M") == toDoList[task][0]:
                if flag:
                    notification.notify(
                        title = nTitle,
                        message = nDescription,
                        app_icon = nIcon,
                        timeout = 5,
                        toast = True
                    )
                flag = False
            else:
                flag = True
            time.sleep(10)
except KeyboardInterrupt:
    print("Exiting...")
    print("Thanks For Using!")
