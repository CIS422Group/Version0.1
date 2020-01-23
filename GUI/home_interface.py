import tkinter as tk
from tkinter import filedialog, Text
import os

root = tk.Tk() #Establishes structure for app window

def inputFile():
	filename = filedialog.askopenfilename(initialdir="./..", title="Select File")
	#insert I/O here for the given filename

canvas = tk.Canvas(root, height = 500, width = 700, bg='#1FB7C9')
canvas.pack()

inputRoster = tk.Button(root, text="Input Roster", padx=10, pady=10, fg="#E74C3C", command=inputFile).place(relx=.3, rely=.1)
# inputRoster.pack()

teacherView = tk.Button(root, text="Teacher View", padx=10, pady=10, fg="#E74C3C").place(relx=.5, rely=.1)
# teacherView.pack()

root.title("Cold Call System")
#root.iconbitmap('cold_call.icns') #Attempt to change icon for program... :(

root.mainloop()
