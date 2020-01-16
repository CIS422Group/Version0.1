"""
The main GIU window for selecting students

Author: Jimmy Lam
Last Modified: 1/13/20
"""

import tkinter as tk
import time

class GUI:
    def __init__(self, winTitle: str, highlightColor: str):
        self.title = winTitle
        self.t = tk.Tk()
        self.bgColor = highlightColor
        self.window = tk.Text(self.t, height=1, width=60, font=('Courier', 16))

        self.t.title(self.title)  # set window description

    def update(self, text: str, highlightStart: int, highlightEnd: int):
        """ Prints the names given in <text> to the GUI screen.
        highlightStart is the starting index of the highlighting
        and highlightEnd is the ending index.
        """
        self.window.pack()
        self.window.insert('1.0', ' ' * 60)  # clear names
        self.window.insert('1.0', text)      # write text to GUI

        # now add highlighting
        self.window.tag_add('tag1', '1.{}'.format(highlightStart), '1.{}'.format(highlightEnd))
        self.window.tag_config('tag1', background=self.bgColor)
        self.t.update()

def main():
    name1 = "Maura McCabe"
    name2 = "Jimmy Lam"
    name3 = "Lucas Hyatt"
    name4 = "Yin Jin"
    name5 = 'Noah Tigner'

    gui = GUI('Students on deck', 'green')

    print('Starting GUI test')

    names = "{}   {}   {}   {}".format(name1, name2, name3, name4)

    highlightBegin = len(name1) + 3
    highlightEnd = highlightBegin + len(name2)
    gui.update(names, highlightBegin, highlightEnd)

    print('highlighting changing in 3 seconds...')
    time.sleep(3)

    highlightBegin = len(name1) + len(name2) + 6
    highlightEnd = highlightBegin + len(name3)
    gui.update(names, highlightBegin, highlightEnd)

    print('list changing in 3 seconds...')
    time.sleep(3)

    names = "{}   {}   {}   {}".format(name2, name3, name4, name5)

    highlightBegin = 0
    highlightEnd = highlightBegin + len(name2)
    gui.update(names, highlightBegin, highlightEnd)

    print("\n--- End of test. Close the cold calling window to exit ---")

    gui.t.mainloop()  # blocks until the window is closed

if __name__ == '__main__':
    main()

"""
Sources:
- examples: https://www.python-course.eu/tkinter_text_widget.php
- font size edit: https://stackoverflow.com/questions/30685308/how-do-i-change-the-text-size-in-a-label-widget-python-tkinter
- highlight name: https://www.tutorialspoint.com/python/tk_text.htm
"""

