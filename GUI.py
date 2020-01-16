"""
The main GIU window for selecting students

Author: Jimmy Lam
Last Modified: 1/13/20
"""

import tkinter as tk
import time

def printGUI(textWindow, text, hStartIdx, hEndIdx):
    textWindow.pack()
    textWindow.insert('1.0', ' ' * 60)  # clear names
    textWindow.insert('1.0', text)

    textWindow.tag_add('tag1', '1.{}'.format(hStartIdx), '1.{}'.format(hEndIdx))
    textWindow.tag_config('tag1', background='green')


def main():
    name1 = "Maura McCabe"
    name2 = "Jimmy Lam"
    name3 = "Lucas Hyatt"
    name4 = "Yin Jin"
    name5 = 'Noah Tigner'

    win = tk.Tk()
    win.title("Current Cold Calling List")

    textWindow = tk.Text(win, height=1, width=60, font=('Courier', 16))

    names = "{}   {}   {}   {}".format(name1, name2, name3, name4)

    highlightBegin = len(name1) + 3
    highlightEnd = highlightBegin + len(name2)
    printGUI(textWindow, names, highlightBegin, highlightEnd)
    win.update()

    print('highlighting changing in 3 seconds...')
    time.sleep(3)

    highlightBegin = len(name1) + len(name2) + 6
    highlightEnd = highlightBegin + len(name3)
    printGUI(textWindow, names, highlightBegin, highlightEnd)
    win.update()

    print('list changing in 3 seconds...')
    time.sleep(3)

    names = "{}   {}   {}   {}".format(name2, name3, name4, name5)

    highlightBegin = 0
    highlightEnd = highlightBegin + len(name2)
    printGUI(textWindow, names, highlightBegin, highlightEnd)
    win.update()

    print("\n--- End of test. Close the cold calling window to exit ---")

    win.mainloop() # blocks until the window is closed


if __name__ == '__main__':
    main()

"""
Sources:
- examples: https://www.python-course.eu/tkinter_text_widget.php
- font size edit: https://stackoverflow.com/questions/30685308/how-do-i-change-the-text-size-in-a-label-widget-python-tkinter
- highlight name: https://www.tutorialspoint.com/python/tk_text.htm
"""

