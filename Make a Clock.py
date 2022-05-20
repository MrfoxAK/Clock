from tkinter import *
from tkinter.ttk import *

from time import strftime

root = Tk()
root.title("Clock")
# root.geometry("250x25")

def time():
    str = strftime("%H:%M:%S %p")
    label.config(text=str)
    label.after(1000, time)

label = Label(root, font=("ds-digital,100"),background="black",foreground="cyan")
label.pack(anchor="center")

time()

mainloop()
















