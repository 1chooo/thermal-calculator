from tkinter import Tk
from Thermal2.tk_gui.BaseDesk import base


def main() -> None:
    root = Tk()
    base.init_base(root)
    root.mainloop()
