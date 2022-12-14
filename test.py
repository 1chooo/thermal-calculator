"""
This test is successfully to call the package gui
"""

import tkinter as tk

from gui.BaseDesk import base


root = tk.Tk()

if __name__ == "__main__":

    base.init_base(root)
    root.mainloop()
