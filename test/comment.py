

# import tkinter as tk
# from PIL import Image, ImageTk
#
#
# class BaseDesk:
#
#     def __init__(self, master):
#
#         self.root = master
#         self.root = config()
#         self.root.title("Login Page")
#         self.root.geometry("960x540")
#
#         initface(self.root)
#
#
# class initface:
#
#     def __init__(self, master):
#
#         self.root = master
#
#         img = Image.open("./assets/imgs/Login.jpg")
#         tk_img = ImageTk.PhotoImage(img)
#
#         label = tk.Label(root, image=tk_img)  # 設定 anchor
#         label.pack()
#
#         # canvas = Canvas(root, width=960, height=540)
#         # canvas.create_image(0, 0, anchor='nw', image=tk_img)  # 在 Canvas 中放入圖片
#         # canvas.pack()
#
# class DashBoard:
#
#
#
#
# if __name__ == '__main__':
#
#     root = tk.Tk()
#     BaseDesk(root)
#     root.mainloop()


import tkinter as tk
from gui.login.gui import loginWindow

root = tk.Tk()
root.withdraw()

if __name__ == "__main__" :

    loginWindow()

    root.mainloop()