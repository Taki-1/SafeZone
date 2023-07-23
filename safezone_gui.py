from cgitb import text
from time import sleep
import tkinter as tk
from tkinter import Y, Label, messagebox
from turtle import textinput, width
from pystray import MenuItem as item
import pystray
from PIL import Image, ImageTk
import os

win = tk.Tk()

win.title('SafeZone V1.1')
win.geometry('800x400')
win.resizable(False, False)


# taskbar hide and show functions
def quit_window(icon, item):
    icon.stop()
    win.destroy()
def show_window(icon, item):
    icon.stop()
    win.after(0, win.deiconify())
def hide_window():
    win.withdraw()
    image = Image.open("favicon.ico")
    menu = (item('Show', show_window), item('Quit', quit_window))
    icon = pystray.Icon("name", image, "Alarm System Active", menu)
    icon.run()
def exit_func():
    win.destroy()
    os.exit()
    exit()

def blocking_func():
    pass

title1 = tk.Label(win, text="Welcome to SafeZone", foreground="black", background="white")
checkbtn = tk.Checkbutton(win, command=func1)


title1.place(x=380, y=180)
checkbtn.place(x=380, y=220)


win.protocol('WM_DELETE_WINDOW', hide_window) # hide app in taskbar on click of terminate button
win.mainloop()