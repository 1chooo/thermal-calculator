import tkinter as tk
from PIL import Image, ImageTk

def loginWindow():
    Login()

class Login():

    def __init__(self, master):
        
        self.root = master
        self.root.config()
        self.root.title("Login Page")
        self.root.geometry("960x540")

        initface(self.root)

class initface() :

    def __init__(self, master):

        self.root = master
        # self.root.config(bg="#98AFC7")
        img = Image.open("../../assets/imgs/Login.jpg")
        tk_img = ImageTk.PhotoImage(img)

        canvas = tk.Canvas(self.root, width=960, height=540)
        canvas.create_image(0, 0, anchor='nw', image=tk_img)   # 在 Canvas 中放入圖片
        canvas.pack()

        self.initface = tk.Frame(self.root)
