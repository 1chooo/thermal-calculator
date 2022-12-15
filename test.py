"""
This test is successfully to call the package gui
"""

from tkinter import *
from gui.BaseDesk import base


root = Tk()

if __name__ == "__main__":

    base.init_base(root)
    root.mainloop()
