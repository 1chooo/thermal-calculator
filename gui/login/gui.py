import tkinter as tk

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

    def __init__(self):
