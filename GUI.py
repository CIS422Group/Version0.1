"""
The main GIU window for selecting students

Author: Jimmy Lam
Last Modified: 1/13/20
"""

import tkinter as tk

def giuwWindow():
    name1 = "Jimmy Lam"
    name2 = "Maura McCabe"
    name3 = "Lucas Hyatt"
    name4 = "Yin Jin"
    name5 = 'Noah Tigner'

    win = tk.Tk()
    win.title("Current Cold Calling List")

    t = tk.Text(win, height=1, width=60, font=('Courier', 16))
    t.pack()
    t.insert('1.0', '                                 ')  # cannot use \t, won't work
    t.insert('1.0',  name2)  # insert('<line#>.<index>', <text to insert>)
    t.insert('1.15', name1)  # offset by 15 characters from beginning per name
    t.insert('1.30', name3)
    t.insert('1.45', name4)

    #t.tag_add('tag1', '1.0 + 15c', '1.0 + {}c + 15c'.format(len(name2)))
    t.tag_add('tag1', '1.15', '1.15 + {}c'.format(len(name1)))

    t.tag_config('tag1', background='green')

    tk.mainloop()

giuwWindow()

"""
Sources:
- examples: https://www.python-course.eu/tkinter_text_widget.php
- font size edit: https://stackoverflow.com/questions/30685308/how-do-i-change-the-text-size-in-a-label-widget-python-tkinter
- highlight name: https://www.tutorialspoint.com/python/tk_text.htm
"""

