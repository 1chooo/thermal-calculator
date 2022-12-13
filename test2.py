import tkinter
l=[]
class Test:

    def __init__(self, master):
        canvas = tkinter.Canvas(master)
        canvas.grid(row=0, column=0)
        photo = tkinter.PhotoImage(file='./assets/imgs/Login.png')
        l.append(photo)
        canvas.create_image(0, 0, image=photo)

root = tkinter.Tk()
test = Test(root)
root.mainloop()


# import tkinter
#
# class Test:
#     def __init__(self, master):
#         canvas = tkinter.Canvas(master)
#         canvas.grid(row = 0, column = 0)
#         self.photo = tkinter.PhotoImage(file='./assets/imgs/Login.png') # Changes here
#         canvas.create_image(0, 0, image=self.photo) # Changes here
#
# root = tkinter.Tk()
# test = Test(root)
# root.mainloop()