import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk


class BaseDesk:

    def __init__(self, master):

        self.root = master
        self.root.config()
        self.root.title("Login Page")
        self.root.geometry("960x540")

        LoginFrame(self.root)


class LoginFrame:

    def __init__(self, master):

        self.root = master
        self.root.config(bg='#98AFC7')
        self.root.title("Login Page")
        self.root.geometry("960x540")

        """
        Create the lower Frame in the window
        """
        self.loginFrame = tk.Frame(self.root, bg="#BCC6CC")
        self.loginFrame.place(relx=0, rely=0, relheight=1, relwidth=1)

        """
        Add the canvas layer on the lower Frame
        """
        self.canvas = Canvas(
            self.loginFrame,
            width=960,
            height=540,
            bd=0,
            cursor='arrow',
        )
        self.canvas.pack(side=TOP, anchor=W, padx=0, pady=0)

        self.bg_img = Image.open('./assets/imgs/Login.jpg')
        self.tk_bg_img = ImageTk.PhotoImage(self.bg_img)
        self.canvas.create_image(480, 270, anchor='center', image=self.tk_bg_img)

        self.btn_img = Image.open('./assets/imgs/Login_btn.png')
        self.tk_btn_img = ImageTk.PhotoImage(self.btn_img)
        # self.canvas.create_image(720, 474, anchor='center', image=self.tk_btn_img)
        self.btn = tk.Button(
            self.loginFrame,
            # text='Login',
            command=self.test,
            image=self.tk_btn_img,
            bd=0,
            cursor='mouse',
            # bg="#BCC6CC",
        )
        self.canvas.create_window(720, 474, anchor='center', window=self.btn)

        self.entry_img = Image.open('./assets/imgs/username_entry.png')
        self.tk_entry_img = ImageTk.PhotoImage(self.entry_img)
        self.canvas.create_image(720, 275, anchor='center', image=self.tk_entry_img)

        self.username_entry = Entry(self.canvas, bd=0)
        self.username_entry.config(bg="#EFEFEF", fg="black")
        self.username_entry.place(x=580, y=275, width=270.0, height=30)

        self.pwd_entry = Entry(self.canvas, bd=0)
        self.pwd_entry.config(bg="#EFEFEF", fg="black")
        self.pwd_entry.place(x=580, y=377, width=270.0, height=30)


    def test(self):

        if self.username_entry.get() != '':
            print(self.username_entry.get())
            print(self.pwd_entry.get())

        print("test")


if __name__ == '__main__':

    root = tk.Tk()
    BaseDesk(root)

    root.mainloop()