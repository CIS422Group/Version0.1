"""
The main GIU window for selecting students

Author: Jimmy Lam
Last Modified: 1/13/20
"""

import tkinter as tk

def guiWindow():
    name1 = "Maura McCabe"
    name2 = "Jimmy Lam"
    name3 = "Lucas Hyatt"
    name4 = "Yin Jin"
    name5 = 'Noah Tigner'

    win = tk.Tk()
    win.title("Current Cold Calling List")

    t = tk.Text(win, height=1, width=60, font=('Courier', 16))
    t.pack()
    #t.insert('1.0', ' ' * 60)  # cannot use \t, won't work
    t.insert(tk.END, name1)  # insert('<line#>.<index>', <text to insert>)
    t.insert(tk.END, '   ')
    t.insert(tk.END, name2)  # offset by 15 characters from beginning per name
    t.insert(tk.END, '   ')
    t.insert(tk.END, name3)
    t.insert(tk.END, '   ')
    t.insert(tk.END, name4)

    beginIdx = len(name1) + 3
    t.tag_add('tag1', '1.{}'.format(beginIdx), '1.{}'.format(beginIdx + len(name2)))
    t.tag_config('tag1', background='green')

    tk.mainloop()

guiWindow()

"""
Sources:
- examples: https://www.python-course.eu/tkinter_text_widget.php
- font size edit: https://stackoverflow.com/questions/30685308/how-do-i-change-the-text-size-in-a-label-widget-python-tkinter
- highlight name: https://www.tutorialspoint.com/python/tk_text.htm
"""

