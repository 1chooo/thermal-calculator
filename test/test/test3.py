"""
This is successful to show the full image.
"""


import tkinter as tk
from tkinter import ttk


class LoginBase(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Login Page')
        self.geometry('960x540')

        # btn = tk.Button(self, text="change", command=self.change)
        # btn.config(width='20', height='3')
        # btn.pack()
        # btn.place(relx=10, rely=0.5)
        # btn.pack()

        self.python_image = tk.PhotoImage(file='../../assets/imgs/Login.png')
        ttk.Label(self, image=self.python_image).pack()

        btn = tk.Button(self, text="change", command=self.change)
        btn.config(width='20', height='3')
        btn.place(relx=0.5, rely=0.5)
        btn.pack()



    def change(self, ):

        self.destroy()
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
        LoginBase()


if __name__ == "__main__":

    app = LoginBase()
    app.mainloop()