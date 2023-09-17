import tkinter as tk
from tkinter import messagebox

def previousSession():
    try:
        with open("tasks.txt", "r") as Tasks:
            tskList = Tasks.readlines()
        for i in tskList:
            listbox.insert(tk.END, "")
            listbox.insert(tk.END, f"     {i[0:-1]}")
    except:
        messagebox.showerror("Sorry!", "Some Error Occured!")

def addTask(entry):
    Task = entry.get()
    if Task != "":
        with open("tasks.txt", "a") as Tasks:
            Tasks.write(f"{Task}\n")
        listbox.insert(tk.END, "")
        listbox.insert(tk.END, f"     {Task}")
    else:
        messagebox.showwarning("Warning", "Please Enter A Task")

def delete_task():
    try:
        selected_index = listbox.curselection()
        value = f"{listbox.get(selected_index)[5:]}\n"
        print(value)
        listbox.delete(selected_index)
        listbox.delete(selected_index[0]-1)
        print(value)
        with open("tasks.txt", "r") as Tasks:
            tskList = Tasks.readlines()
            tskList_copy = tskList.copy()
            for item in tskList_copy:
                if value == item:
                    tskList.remove(item)
        with open("tasks.txt", "w") as Tasks:
            Tasks.writelines(tskList)
    except:
        messagebox.showwarning("Warning", "Please select a task to delete.")

root = tk.Tk()
width = root.winfo_screenwidth()
height = round(0.9 * root.winfo_screenheight())
root.geometry(f"{width}x{height}")

root.rowconfigure(0, weight=1)
root.rowconfigure(1, weight=9)
root.rowconfigure(2, weight=3)
root.columnconfigure(0, weight=1)

lbl_Heading = tk.Label(text="To Do List", font=("grobold", 25), bg="light blue")
lbl_Heading.grid(row=0, column=0, sticky="news")

frm_tasks = tk.Frame(border=0)
frm_tasks.grid(row=1, column=0, sticky="news")

scrollbar = tk.Scrollbar(frm_tasks)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

listbox = tk.Listbox(
    frm_tasks, width=180, yscrollcommand=scrollbar.set, font=("Arial", 12), bg="#2d343a"
)

previousSession()

listbox.pack(side=tk.LEFT, fill=tk.BOTH)
scrollbar.config(command=listbox.yview)

frm_buttons = tk.Frame(bg="#333333", border=0)
frm_buttons.grid(row=2, column=0, sticky="news")

ent_task = tk.Entry(master=frm_buttons, width=100)
ent_task.place(anchor="c", relx=0.5, rely=0.3)

btn_add = tk.Button(
    border=0,
    bg="light green",
    master=frm_buttons,
    text="Add Task",
    command=lambda: addTask(ent_task),
)
btn_add.place(anchor="c", relx=0.45, rely=0.6)

btn_sub = tk.Button(
    border=0, bg="red", master=frm_buttons, text="Delete", command=delete_task
)
btn_sub.place(anchor="c", relx=0.55, rely=0.6)

root.mainloop()
