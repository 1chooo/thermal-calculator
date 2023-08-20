"""

"""


from tkinter import *
from PIL import Image, ImageTk


class BaseDesk:

    def __init__(self, master) -> None:

        self.root = master
        self.root.config()
        self.root.title("Login Page")
        self.root.geometry("960x540")

        LoginFrame(self.root)


class LoginFrame:

    def __init__(self, master):

        self.admin_username = "admin"
        self.admin_pwd = "admin"

        self.caution = None
        self.root = master
        self.root.config(bg='#98AFC7')
        self.root.title("Login Page")
        self.root.geometry("960x540")

        """
            Build the Menu Bar
            Wish List: 
                1. Switch to the calculator
                2. Switch to the about us
                3. Switch to the background
                4. Switch to the guide
                5. log out
            The problem may meet is the link of the objects!!!
        """
        # self.menu = Menu(self.root)
        # self.menu_bar = Menu(self.menu)
        # # self.menu_bar.add_command(label='Open')
        # # self.menu_bar.add_command(label='Save')
        # self.menu_bar.add_command(
        #     label='Exit',
        #     command=root.destroy,
        # )
        # self.menu.add_cascade(label='File', menu=self.menu_bar)
        #
        # # with the config() then we can add to the window
        # self.root.config(menu=self.menu)

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
            Add image to the background
        """
        self.bg_img = Image.open('./assets/imgs/Login.jpg')
        print(self.bg_img)
        self.tk_bg_img = ImageTk.PhotoImage(self.bg_img)
        print(self.tk_bg_img)
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
            command=self.__loginFunc,
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

    def __loginFunc(self,):

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


class Dashboard:

    image_data_base = []


    def __init__(self, master) -> None:

        self.root = master
        self.root.config(bg='#98AFC7')
        self.root.title("Dashboard")
        self.root.geometry("960x540")

        """
            Create the lower Frame in the window
        """
        self.dashboard_frame = Frame(
            self.root,
            bg="#BCC6CC",
        )
        self.dashboard_frame.place(
            relx=0,
            rely=0,
            relheight=1,
            relwidth=1,
        )

        """
            Add the canvas layer on the lower Frame
        """
        self.canvas = Canvas(
            self.dashboard_frame,
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
            Add the image to the background
        """
        self.bg_img = Image.open('./assets/imgs/Dashboard.jpg')
        self.tk_bg_img = ImageTk.PhotoImage(self.bg_img)
        self.image_data_base.append(self.tk_bg_img)
        print(self.tk_bg_img)
        print(self.image_data_base[-1])
        self.canvas.create_image(
            480,
            270,
            anchor='center',
            image=self.image_data_base[0],
        )

        """
            test part: 
            to add the text to test canvas
        """
        # self.canvas.create_text(
        #     30,
        #     30,
        #     text='test',
        # )


class ImageProgressing:

    # def __init__(self) -> None:

    def __create_canvas(self, width_, height_) -> None:

        self.canvas = Canvas(
            width=width_,
            height=height_,
            bg='violet',
            bd=0,
        )
        self.canvas.grid()


    def __embed_img(self, img_path) -> None:

        img = Image.open(img_path)
        img = ImageTk.PhotoImage(img)
        self.canvas.create_image(
            0,
            0,
            image=img,
            anchor='nw',
        )


if __name__ == '__main__':

    root = Tk()
    BaseDesk(root)

    root.mainloop()