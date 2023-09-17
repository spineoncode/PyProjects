# Importing Needed Modules
import tkinter as tk
import time
import pyttsx3
import threading

# Creating a list which contains all those timings at wich the alarm will ring.
allTimings = []
# Creating Speak Variable which when become false the the program won't alarm.
Speak = True

# This function updates the allTimings list with all the timings present in time.txt(which is actually getting used as a database)
def lookForTime():
    global allTimings
    with open("time.txt", "r") as Data:
        Timings = Data.readlines()
        for index, item in enumerate(Timings):
            Timings[index] = item[0:-1]
    allTimings = Timings

# This Function first updates the list by running lookForTime() so that it can ensure that it's not using false data and then it it clears all the widget from passed frame and adds new widgets(which actually show at what times the alarm will ring)
def timeCompell(frame):
    lookForTime()
    allTimings.sort()
    for widget in frame.winfo_children():
        widget.destroy()
    for item in allTimings:
        object = tk.Label(frame, text=f"Hey! Your Reminder Of Drinking Water Is Set To {item}, I'll Remind You!", font=("bahnschrift", 20))
        object.place(relx=0.05, rely=0.02)
        y += 0.1

# defining a LoudSpeaker function which actually alarms by telling the time.
def LoudSpeaker():
    Time = time.strftime("%H:%M")
    for item in allTimings:
        if item == Time:
            Hour = time.strftime("%H")
            Min = time.strftime("%M")
            pyttsx3.speak(f"It's {Hour} {Min}, Time To Drink Water")

# defining a function which runs a while loop and runs loudspeaker function every 1 sec.
def checkSpeaker():
    while Speak:
        time.sleep(1)
        LoudSpeaker()

# This function takes an argument (i.e text inside a entry widget which is getting processed as time) and saves into text.txt file. (when the program will rerun then the program can retrieve previous data from the file) and at the end runs timeCompell frame_topFunction So That The Program without restarting updates the information
def addTime(txt1):
    global allTimings
    time = txt1.get()
    timeMod = time.split(" ")
    if timeMod[1].lower() == "pm":
        pmTime = timeMod[0].split(":")
        pmTime[0] = str(int(pmTime[0]) + 12)
        time = ":".join(pmTime)
    elif timeMod[1].lower() == "am":
        amTime = timeMod[0].split(":")
        if len(amTime[0]) == 2:
            time = ":".join(amTime)
        elif len(amTime[0]) == 1:
            amTime[0] = "0"+str(int(amTime[0]))
            time = ":".join(amTime)
    with open("time.txt", "a") as Data:
        Data.write(f"{time}\n")
    timeCompell(frame_top)

# This function takes an argument (i.e text inside a entry widget which is getting processed as time) and deletes the time from text.txt file. (when the program will rerun then the program can retrieve previous data from the file) and at the end runs timeCompell frame_topFunction So That The Program without restarting updates the information
def subTime(txt1):
    global allTimings
    time = txt1.get()
    timeMod = time.split(" ")
    if timeMod[1].lower() == "pm":
        pmTime = timeMod[0].split(":")
        pmTime[0] = str(int(pmTime[0]) + 12)
        time = ":".join(pmTime)
    elif timeMod[1].lower() == "am":
        amTime = timeMod[0].split(":")
        if len(amTime[0]) == 2:
            time = ":".join(amTime)
        elif len(amTime[0]) == 1:
            amTime[0] = "0"+str(int(amTime[0]))
            time = ":".join(amTime)
    allTimings.remove(time)
    with open ("time.txt", "w") as Data:
        pass
    for i in allTimings:
        with open("time.txt", "a") as Data2:
            Data2.write(f"{i}\n")
    timeCompell(frame_top)

if __name__ == "__main__":

    # This creates a thread which will process the checkSpeaker function which actually runs a while loop which untill gets completly executed won't allow to run the furthur code
    t1 = threading.Thread(target=checkSpeaker, args=())
    # This starts the thread as a simultanious process and then moves on (to furthur code).
    t1.start()

    # creating the window
    mainWin = tk.Tk()
    # Fixing the window size
    mainWin.geometry("960x540")
    mainWin.minsize(960, 540)
    mainWin.maxsize(960, 540)
    # Titling the window as it's name
    mainWin.title("Water Reminder")

    # patitioning the window
    mainWin.columnconfigure(1,weight=4)
    mainWin.rowconfigure(0, weight=800)
    mainWin.rowconfigure(1, weight=1)
    mainWin.rowconfigure(2, weight=79)

    # making frames as per patitions
    frame_top=tk.Frame(mainWin,bg='#181e24')
    frame_middle=tk.Frame(mainWin,bg='green')
    frame_bottom=tk.Frame(mainWin,bg='#181e24')

    # running timeCompell function by passing frame top so that it populates the top patiion (or say frame).
    timeCompell(frame_top)

    frame_top.grid(row=0,column=1,sticky='wens')
    frame_middle.grid(row=1,column=1,sticky='wens')
    frame_bottom.grid(row=2,column=1,sticky='wens')

    # CREATING ENTRY BOX.
    timeAddEntry = tk.Entry(frame_bottom, width=100)
    timeAddEntry.place(relx=0.65, rely=0.45, anchor="e")

    # creating a add button which actually process a lambda function with no arguments and that lambda function is given to run a function (i.e addTime) with a parameter
    timeAddButton = tk.Button(frame_bottom, text="Add", command=lambda: addTime(timeAddEntry), width=20, bg="light green", font=("impact", 10))
    timeAddButton.place(relx=0.838, rely=0.47, anchor="e")
    
    # creating a subtract button which runs like above button but taking subTime as function and not addTime
    timeSubButton = tk.Button(frame_bottom, text="Subtract", command=lambda: subTime(timeAddEntry), width=20, bg="red", font=("impact", 10))
    timeSubButton.place(relx=0.978, rely=0.47, anchor="e")

    mainWin.mainloop()
    # making speak false so that the thread process stops
    Speak = False
