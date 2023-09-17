import os
import tkinter as tk
import time
from tkinter import simpledialog
from tkinter import ttk
from tkinter import messagebox

# import pyperclip

try:
    os.makedirs(".\\Catas")
except FileExistsError:
    pass

allFiles = os.listdir(".\Catas")


def dataWindow():
    class Category:
        def __init__(self, categoryName):
            global allFiles
            allFiles = os.listdir(".\Catas")
            self.fileToOpen = f".\\Catas\\{categoryName}.txt"
            self.allPsswords = {}
            allSitesPass = []

            if (f"{categoryName}.txt") in allFiles:
                with open(self.fileToOpen, "r") as Data:
                    allSitesPass = Data.readlines()
                    for item in allSitesPass:
                        id, Pass = item.split(":")
                        self.allPsswords[id] = Pass[0:-1]
            else:
                with open(self.fileToOpen, "w") as Data:
                    print(f"New Category Created: {categoryName}")
                    allSitesPass = Data.readlines()
                    for item in allSitesPass:
                        id, Pass = item.split(":")
                        self.allPsswords[id] = Pass[0:-1]

            self.allSitesPass = allSitesPass

        def savePassword(self, siteName, password):
            siteExists = False
            for item in self.allPsswords.keys():
                if item == siteName:
                    siteExists = True
            if siteExists != True:
                self.allPsswords[siteName] = password
                print("Password Added!")
            else:
                print("It already exists!")

        def remPassword(self, siteName):
            siteExists = False
            for item in self.allPsswords.keys():
                if item == siteName:
                    siteExists = True
            if siteExists == True:
                del self.allPsswords[siteName]
            else:
                print("It doesn't exists!")

        def updatePass(self, siteName, password):
            siteExists = False
            for item in self.allPsswords.keys():
                if item == siteName:
                    siteExists = True
            if siteExists == True:
                self.allPsswords[siteName] = password
                print("Password Updated!")
            else:
                print("It doesn't exists!")

        def saveData(self):
            dataToBeWritten = []
            for item in self.allPsswords:
                dataToBeWritten.append(f"{item}:{self.allPsswords[item]}\n")
            with open(self.fileToOpen, "w") as Data:
                Data.writelines(dataToBeWritten)

    def showCatas():
        global allFiles
        try:
            for category in allFiles:
                listbox.insert(tk.END, "")
                listbox.insert(tk.END, f"     {category[0:-4]}")
        except Exception as e:
            print(e)

    def addCata():
        global allFiles
        try:
            answer = simpledialog.askstring(
                "Input", "Enter Name Of Catagory", parent=root
            )
            if answer != "":
                listbox.insert(tk.END, "")
                listbox.insert(tk.END, f"     {answer}")
                allFiles.append(f"{answer}.txt")
                with open(f".\\Catas\\{answer}.txt", "w") as Data:
                    pass
            else:
                messagebox.showinfo("", "You Didn't Enter Anything")
        except:
            pass

    def remCata():
        global allFiles
        try:
            selected_index = listbox.curselection()
            value = f"{listbox.get(selected_index)[5:]}\n"
            listbox.delete(selected_index)
            listbox.delete(selected_index[0] - 1)
            allFiles.remove(f"{(value[0:-1])}.txt")
            os.remove(f".\\Catas\\{(value[0:-1])}.txt")
        except:
            pass

    def openCata():
        def addSitePass():
            try:
                site = simpledialog.askstring(
                    "Input", "Enter Name Of Site Or Application", parent=root
                )
                passwordToSite = simpledialog.askstring(
                    "Input", f"Enter Password For {site}", parent=root
                )
                if site != "":
                    if passwordToSite != "":
                        obj.savePassword(site, passwordToSite)
                        obj.saveData()
                        newWin.destroy()
                        openCata()
                else:
                    messagebox.showinfo("", "You Didn't Enter Anything")
            except:
                pass

        def remSitePass():
            try:
                curItem = tree.focus()
                sitePass = tree.item(curItem)["values"]
                selected_item = tree.selection()[0]
                tree.delete(selected_item)
                obj.remPassword(sitePass[0])
                obj.saveData()
            except IndexError:
                messagebox.showerror(
                    "No Selection", "How Would We Know What To Remove!"
                )

        def copySitePass():
            try:
                curItem = tree.focus()
                sitePass = tree.item(curItem)["values"][1]
                # pyperclip.copy(sitePass)
            except IndexError:
                messagebox.showerror("No Selection", "Select To Copy!")

        try:
            selected_index = listbox.curselection()
            value = f"{listbox.get(selected_index)[5:]}"
            obj = Category(value)

            newWin = tk.Toplevel(root)
            newWin.title(f"Passwords Saved In {value}")

            style = ttk.Style()
            style.theme_use("clam")

            tree = ttk.Treeview(
                newWin,
                column=("Website", "Password"),
                show="headings",
                height=len(obj.allPsswords),
            )
            tree.column("# 1", anchor=tk.CENTER)
            tree.heading("# 1", text="Website")
            tree.column("# 2", anchor=tk.CENTER)
            tree.heading("# 2", text="Password")

            for item in obj.allPsswords.keys():
                tree.insert(
                    "", "end", text="1", values=(f"{item}", f"{obj.allPsswords[item]}")
                )

            tree.grid(row=0, column=0, sticky="news", pady=10, padx=10)

            btnAdd = ttk.Button(master=newWin, text="Add", command=addSitePass)
            btnAdd.grid(row=1, column=0, sticky="news", pady=10, padx=10)

            btnSub = ttk.Button(master=newWin, text="Remove", command=remSitePass)
            btnSub.grid(row=2, column=0, sticky="news", pady=10, padx=10)

            btnCopy = ttk.Button(master=newWin, text="Copy", command=copySitePass)
            btnCopy.grid(row=3, column=0, sticky="news", pady=10, padx=10)

            newWin.mainloop()
        except Exception as error:
            messagebox.showerror("Error", error)

    root = tk.Tk()
    root.geometry("1280x720")

    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=3)
    root.rowconfigure(1, weight=48)
    root.rowconfigure(2, weight=1)

    root.grid_propagate(False)

    lblWish = tk.Label(root, text="Hello", font=("grobold", 25))
    lblWish.grid(row=0, column=0, sticky="wns", padx=15, pady=15)

    frmCatas = tk.Frame(root, bg="blue")
    frmCatas.grid(row=1, column=0, sticky="news", padx=15, pady=15)

    scrollbar = tk.Scrollbar(frmCatas)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    listbox = tk.Listbox(
        frmCatas,
        width=180,
        yscrollcommand=scrollbar.set,
        font=("Arial", 12),
        bg="#2d343a",
    )

    showCatas()

    listbox.pack(side=tk.LEFT, fill=tk.BOTH)
    scrollbar.config(command=listbox.yview)

    frmBtns = tk.Frame(root)
    frmBtns.grid(row=2, column=0, sticky="news")

    btnAddCata = tk.Button(
        frmBtns,
        text="+",
        font=("impact", 15),
        width=15,
        bg="light blue",
        border=0,
        command=addCata,
    )
    btnAddCata.grid(row=0, column=0, sticky="nws", padx=15, pady=15)

    btnRemCata = tk.Button(
        frmBtns,
        text="-",
        font=("impact", 15),
        width=15,
        bg="light blue",
        border=0,
        command=remCata,
    )
    btnRemCata.grid(row=0, column=1, sticky="nws", padx=15, pady=15)

    btnOpenCata = tk.Button(
        frmBtns,
        text="Open",
        font=("impact", 15),
        width=15,
        bg="light blue",
        border=0,
        command=openCata,
    )
    btnOpenCata.grid(row=0, column=2, sticky="nws", padx=15, pady=15)

    root.mainloop()

def checkFrame(widget):
    if isinstance(widget, tk.Frame):
        return "Frame"
    else:
        return "Not Frame"


submitClick = 0
Password = ""
rewritePass = 0


def guideText(lblTxt):
    global rewritePass
    global firstStart
    global submitClick
    if firstStart:
        try:
            if submitClick == 0 and rewritePass == 1:
                lblTxt.config(text="Create Password (Your Password Didn't Match)")
                entPass.delete(0, tk.END)
            elif submitClick == 1:
                lblTxt.config(text="Rewrite Password")
            else:
                lblTxt.config(text="Create Password")
        except:
            print("Exception Handled!")
    else:
        lblTxt.config(text="Enter Password")


def submitPass(entbox, lblTxt):
    global root
    global rewritePass
    global Password
    global submitClick
    if entbox.get() == "":
        submitClick = 0
        Password = ""
    elif submitClick == 0:
        Password = entbox.get()
        entbox.delete(0, tk.END)
        submitClick = 1
    else:
        if entbox.get() == Password:
            with open("PAMADA.txt", "w") as PassData:
                PassData.write(f"{Password}\n")
            root.destroy()
            dataWindow()
        else:
            rewritePass = 1
            submitClick = 0
            Password = ""
    guideText(lblTxt)


def enterPass(entbox):
    global root
    global rewritePass
    global Password
    global submitClick

    Password = entbox.get()
    entbox.delete(0, tk.END)

    with open("PAMADA.txt", "r") as PassData:
        PassInFile = PassData.read()
    if PassInFile[0:-1] == Password:
        root.destroy()
        dataWindow()
    else:
        lblGuide.config(text="Wrong Password! Enter Again")


if __name__ == "__main__":
    firstStart = False

    try:
        with open("PAMADA.txt", "r") as PMD:
            if (Line := PMD.readline()) != "":
                pass
            else:
                firstStart = True
    except FileNotFoundError:
        with open("PAMADA.txt", "w") as PMD:
            pass
        firstStart = True

    root = tk.Tk()
    root.geometry("900x500")
    root.resizable(False, False)

    root.rowconfigure([1], weight=3)
    root.rowconfigure([3], weight=4)
    root.rowconfigure([0, 2], weight=1)
    root.columnconfigure(0, weight=1)
    lblWelcome = tk.Label(root, text="Welcome!", font=("impact", 30))
    lblWelcome.grid(row=0, column=0, sticky="ews")

    lblGuide = tk.Label(root, text="Enter Password", font=("code", 15))
    lblGuide.grid(row=1, column=0, sticky="sw", padx=10)

    entPass = tk.Entry(root, width=79, font=("arial", 15))
    entPass.grid(row=2, column=0, padx=10)

    if firstStart == True:
        btnSub = tk.Button(
            root,
            text="    Next    ",
            font=("arial", 10),
            bg="maroon",
            fg="white",
            border=0,
            command=lambda: submitPass(entPass, lblGuide),
        )
        btnSub.grid(row=3, column=0, padx=10, sticky="nw", pady=10)
    else:
        btnSub = tk.Button(
            root,
            text="    Next    ",
            font=("arial", 10),
            bg="maroon",
            fg="white",
            border=0,
            command=lambda: enterPass(entPass),
        )
        btnSub.grid(row=3, column=0, padx=10, sticky="nw")
    guideText(lblGuide)

    root.mainloop()
