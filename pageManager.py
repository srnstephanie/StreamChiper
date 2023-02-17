import Menu
import mysql.connector
from tkinter import Tk

class pageManager():
    def __init__(self):
        self.user = None
        self.window = Tk()
        self.window.geometry("650x420")
        self.window.configure(bg = "#C8F4DE")
        self.window.title('MyOwnStreamCipher')
        self.window.resizable(False, False)
        
        self.page = Menu.MenuPage(master = self.window, pageManager = self)

    def run(self):
        self.page.startPage()
    
    def Menu(self):
        self.page = Menu.MenuPage(master = self.window, pageManager = self)
        self.page.startPage()