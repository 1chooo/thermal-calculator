from tkinter import Tk
from thermal.gui.base_desk import base


def main() -> None:
    root = Tk()
    base.init_base(root)
    root.mainloop()
