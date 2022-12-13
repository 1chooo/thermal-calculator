import tkinter
import tkinter as tk
from PIL import Image, ImageTk
import os


photo_list = []

class BaseDesk():

    def __init__(self, master):

        self.root = master
        self.root.config()
        self.root.title("Login Page")
        self.root.geometry("960x540")

        InitialFace(self.root)


class InitialFace():

    def __init__(self, master):

        self.master = master
        # self.master.config(bg="green")

        canvas = tkinter.Canvas(master)
        canvas.grid(row=0, column=0)
        img = Image.open('./assets/imgs/Login.png').resize((960, 540))
        photo = tkinter.PhotoImage(img)
        photo_list.append(photo)
        canvas.create_image(0, 0, image=photo)

        # print(photo_list)

        # self.InitialFace = tk.Frame(self.master, )
        # self.InitialFace.pack()



        # btn = tk.Button(self.InitialFace, text="change", command=self.change)
        # btn.pack()



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
    BaseDesk(root)
    root.mainloop()