
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk



class InitialFace(tk.Tk):

    def __init__(self, master):

        super().__init__()

        self.root = master
        self.root.config()
        self.root.title("Login Page")
        self.root.geometry("960x540")

        # self.python_image = tk.PhotoImage(file='./assets/imgs/Login.png')
        # ttk.Label(self, image=self.python_image).pack()

        img = tk.PhotoImage(file='./assets/imgs/Login.png')
        label = tk.Label(root, image=img, width=200, height=200, anchor='nw')
        label.pack()

        self.InitialFace = tk.Frame(self.master, )
        self.InitialFace.pack()

        btn = tk.Button(self.InitialFace, text="change", command=self.change)
        btn.pack()



    def change(self, ):

        self.InitialFace.destroy()
        face1(self.master)


class face1():

    def __init__(self, master):

        self.master = master
        self.master.config(bg="blue")
        self.face1 = tk.Frame(self.master, )
        self.face1.pack()
        btn_back = tk.Button(self.face1, text="face1 back", command=self.back)
        btn_back.pack()

    def back(self):

        self.face1.destroy()
        InitialFace(self.master)


if __name__ == "__main__":

    root = tk.Tk()
    InitialFace(root)
    root.mainloop()