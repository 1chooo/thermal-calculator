"""
This includes the class to build
the second page of the gui.
"""



from tkinter import *
from PIL import Image, ImageTk


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