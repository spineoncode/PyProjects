import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename

def open_file(textBox):
    global filepath
    filepath = askopenfilename(filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    textBox.delete("1.0", tk.END)
    with open(filepath, "r") as input_file:
        text = input_file.read()
        textBox.insert(tk.END, text)
    mainWin.title(f"Simple Text Editor - {filepath}")

def save_file(textBox):
    global filepath
    filepath = asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")],
    )
    with open(filepath, "w") as output_file:
        text = textBox.get("1.0", tk.END)
        output_file.write(text)
    mainWin.title(f"Simple Text Editor - {filepath}")

mainWin = tk.Tk()
mainWin.title("Text Editor")

menu = tk.Menu(mainWin)
mainWin.config(menu=menu)

fileMenu = tk.Menu(menu, tearoff="off")
menu.add_cascade(label='File', menu=fileMenu)

fileMenu.add_command(label="Open", command=lambda: open_file(textBox))
fileMenu.add_command(label="Save as", command=lambda: save_file(textBox))
fileMenu.add_separator()
fileMenu.add_command(label="Exit", command=mainWin.quit)

mainWin.rowconfigure(0, weight=1)
mainWin.columnconfigure(0, weight=1)

textBox = tk.Text(master=mainWin)
textBox.pack(fill=tk.BOTH)

mainWin.mainloop()
