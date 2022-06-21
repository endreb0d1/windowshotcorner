import os
from threading import Thread
import pyautogui
import time
from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk
import webbrowser
from pystray import MenuItem as item
import pystray

# design

#icon_folder = os.path.join(sys._MEIPASS, 'static')
# pyinstaller fix, uncomment the line above before building .exe

root = Tk()
root.iconbitmap("static\icn.ico")
# pyinstaller fix, comment out the line above before building .exe
root.title("WHC")
root.resizable(False, False) 
canvas = tk.Canvas(root, width = 260, height = 400, background = "#222222")
canvas.grid(columnspan = 3, rowspan = 3)

# title
title_text = tk.Label(root, text = "Windows Hot Corner", background = "#222222", fg = "#fbba00")
title_text.grid(column=1, row=0, pady = (50, 0))
title_text.configure(font=("Arial", 16))

# instructions
instructions = tk.Label(root, text = "This program will continue \n to run in the background \n if the window is closed. \n \n Right-click the system tray icon \n and choose Quit to close it.", background = "#222222", fg = "#ffffff")
instructions.grid(column=1, row=1)
    
# UI

# show app window
def show_window(icon, item):
    icon.stop()
    root.after(0,root.deiconify())

# hide app window and show a system tray icon
def hide_window():
    root.withdraw()
    menu=(item('Show', show_window), item('Quit', quit_window))
    image = Image.open("static\icn.ico")
    # pyinstaller fix, comment out the line above and uncomment the line below before building .exe
    # image = Image.open(icon_folder+"\icn.ico")
    icon=pystray.Icon("name", image, "Windows Hot Corner", menu)
    icon.run()

# quit the app
def quit_window(icon, item):
    icon.stop()
    root.destroy()
    os._exit(0)

root.protocol('WM_DELETE_WINDOW', hide_window)

# main function

def app_switcher():
    while True:
        pyautogui.FAILSAFE = False

        cursor = pyautogui.position()
        x = cursor[0]
        y = cursor[1]
        
        if x < 10 and y < 10:
            pyautogui.hotkey('alt', 'ctrl', 'tab')
            time.sleep(2)   

if __name__ == '__main__':
    Thread(target = app_switcher).start()

# hide app windows on start
hide_window()

root.mainloop()