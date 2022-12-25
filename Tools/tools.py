from tkinter import *
from PIL import Image, ImageTk


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