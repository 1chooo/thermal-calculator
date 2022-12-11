import tkinter as tk
from gui.login.gui import loginWindow


root = tk.Tk()
root.withdraw()

if __name__ == "__main__" :

    loginWindow()

    root.mainloop()