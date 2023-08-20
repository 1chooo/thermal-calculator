from tkinter import *
from Thermal.tk_gui.Login.frame import LoginFrame


def init_base(root):

    BaseDesk(root)


class BaseDesk:

    def __init__(self, master):

        self.root = master
        self.root.config()
        self.root.title("Login Page")
        self.root.geometry("960x540")

        LoginFrame(self.root)