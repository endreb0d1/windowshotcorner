# Windows Hot Corner

This app mimics the macOS hot corner function.\n
By default it mimics pressing "alt, ctrl, tab" when the cursor is moved
to the top left corner of the screen, so the user doesn't need to click 
on the icons in the taskbar,\n
or press key combinations when switching windows.

![whc](https://i.imgur.com/sDEkmYL.jpeg)

## Requirements 

```
Python 3
```

## Installation and Use

Run the script, or pack it in an .exe with pyinstaller

```
pyinstaller --noconsole --onefile --add-data "static;static" whc.py
```

uncomment the 3 lines marked in the code before building.
