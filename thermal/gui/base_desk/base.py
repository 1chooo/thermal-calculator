from thermal.gui.login.frame import LoginFrame


def init_base(root):
    BaseDesk(root)


class BaseDesk:
    title = "Login Page"
    geometry = "960x540"

    def __init__(self, master):
        self.root = master
        self.root.config()
        self.root.title(self.title)
        self.root.geometry(self.geometry)

        LoginFrame(self.root)
