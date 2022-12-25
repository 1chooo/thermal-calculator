from tkinter import *
from PIL import Image, ImageTk

from gui.Dashboard.dashboard import Dashboard


class LoginFrame:

    def __init__(self, master):

        self.root = master
        self.root.config(bg='#98AFC7')
        self.root.title("Login Page")
        self.root.geometry("960x540")

        """
        Create the lower Frame in the window
        """
        self.loginFrame = Frame(
            self.root,
            bg="#BCC6CC",
        )
        self.loginFrame.place(
            relx=0,
            rely=0,
            relheight=1,
            relwidth=1,
        )

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
        self.canvas.pack(
            side=TOP,
            anchor=W,
            padx=0,
            pady=0,
        )

        """
        add image to the background
        """
        self.bg_img = Image.open('./assets/imgs/Login.jpg')
        self.tk_bg_img = ImageTk.PhotoImage(self.bg_img)
        self.canvas.create_image(
            480,
            270,
            anchor='center',
            image=self.tk_bg_img,
        )

        """
        Build the login button
        """
        self.btn_img = Image.open('./assets/imgs/Login_btn.png')
        self.tk_btn_img = ImageTk.PhotoImage(self.btn_img)
        self.btn = Button(
            self.loginFrame,
            # text='Login',
            command=self.loginFunc,
            image=self.tk_btn_img,
            bd=0,
            cursor='mouse',
            # bg="#BCC6CC",
        )
        self.canvas.create_window(
            720,
            474,
            anchor='center',
            window=self.btn,
        )

        """
        Build the username input entry
        """
        self.entry_img = Image.open('./assets/imgs/username_entry.png')
        self.tk_entry_img = ImageTk.PhotoImage(self.entry_img)
        self.canvas.create_image(
            720,
            275,
            anchor='center',
            image=self.tk_entry_img
        )

        """
        Build the password input entry
        """
        self.username_entry = Entry(
            self.canvas,
            bd=0,
        )
        self.username_entry.config(
            bg="#EFEFEF",
            fg="black",
        )
        self.username_entry.place(
            x=580,
            y=275,
            width=270.0,
            height=30,
        )

        self.pwd_entry = Entry(
            self.canvas,
            bd=0,
        )
        self.pwd_entry.config(
            bg="#EFEFEF",
            fg="black",
        )
        self.pwd_entry.place(
            x=580,
            y=377,
            width=270.0,
            height=30,
        )

    def __loginFunc(self, ):

        print("The login button has been clicked!!!")

        if self.username_entry.get() != '':

            if self.username_entry.get() == "admin" and self.pwd_entry.get() == "admin":

                print("Username:", self.username_entry.get())
                print("Password:", self.pwd_entry.get())
                print("Login Successfully!!!")

                # self.loginFrame.destroy()
                Dashboard(self.root)

            else:

                print("Username:", self.username_entry.get())
                print("Password:", self.pwd_entry.get())

                print("This user are not in our data base!!!")

                """
                    Wish List:
                    Maybe we can add the caution to the user.
                """
                # self.caution = Canvas(
                #     self.loginFrame,
                #     width=200,
                #     height=50,
                #     bd=0,
                #     bg='#BCC6CC'
                # )
                # self.caution.create_text(
                #     480,
                #     270,
                #     text="Please enter the correct info.",
                #     fill='black',
                # )

            # print("Username:", self.username_entry.get())
            # print("Password:", self.pwd_entry.get())
            # print("Login Successfully!!!")
            #
            # self.loginFrame.destroy()
            # Dashboard(self.root)