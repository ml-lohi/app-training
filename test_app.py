from tkinter import *
import sys, os

class MainWindow():

    def __init__(self, master, title, size):
        self.master = master
        self.title = title
        self.size = size
        self.master.title(self.title)
        self.master.geometry(self.size)

        self.hitext = Label(self.master,
                        text="some random text,\n to change the previous text lol").pack(fill=X, pady=10)

        self.productButton = Button(self.master,
                             text="second window",
                                width=15,
                                command=self.productButtonClicked).place(x=15, y=55)

        self.quitMainWindow = Button(self.master,
                                 text="exit",
                                 width=15,
                                 command=self.on_cancel).place(x=170, y=55)

    def productButtonClicked(self):
        #productWindow = Toplevel()
        obj = ProductMenuWindow(self, "second window", "260x100")
        #productFenster = ProductMenuWindow(productWindow,)

    def on_cancel(self):
        self.master.destroy()        


class ProductMenuWindow(Toplevel):

    def __init__(self, parent, title, size):
        super().__init__(name='product_main_menu')

        self.parent = parent

        self.title(title)

        self.size = size

        self.geometry(size)

        self.text = Label(self, text="what do you want to buy?").pack(fill=X, pady=10)

        self.gobackButton = Button(self,
                               text="go back to main window",
                               width=20,
                               command=self.on_cancel).place(x=55, y=50) #here should be the command for the button

    def on_cancel(self):
        self.destroy()

if __name__ == "__main__":
    mainWindow = Tk()
    mainFenster = MainWindow(mainWindow, "root/main/first window", "300x95")
    mainWindow.mainloop()