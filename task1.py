"""
##### Task 1
Create a "Madlib" that has the users enter in a variety of noun/verb/adjectives.
When they press a button, it should update the contents of a label to display
the completed madlib.
What is a madlib? Visit https://www.madlibs.com/printables/ to see some Madlibs
you might use in your assignment
"""

#Part invitation letter

import tkinter as tk 
from tkinter import *

win = tk.Tk()


label1 = Label(win, width=15, text="Dear " textvariable=labelData)
e1 = Entry(win, text="Noun, ", width=10)
label2 = Label(win, width=15, text="you " textvariable=labelData)
e2 = Entry(win, text="are/aren't" width=10)
label



e1.pack()
e2.pack()








win.mainloop()