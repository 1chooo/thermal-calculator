# -*- coding: utf-8 -*-
"""
Create Date: 2023/08/19
Author: @1chooo(Hugo ChunHo Lin)
Version: v0.0.2
"""

from tkinter import Tk
from thermal.gui.base_desk import base


def main() -> None:
    root = Tk()
    base.init_base(root)
    root.mainloop()

if __name__ == "__main__":
    main()
