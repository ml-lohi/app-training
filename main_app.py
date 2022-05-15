"""
    Turorial from:
    https://realpython.com/python-gui-tkinter/
    https://medium.com/swlh/easy-steps-to-create-an-executable-in-python-using-pyinstaller-cc48393bcc64
"""
import tkinter as tk
from simple_app import SimpleApp
from matplotlib_app import MatplotlibApp
from utils.app_interface import AppInterface


class MainApp(AppInterface):
    
    def __init__(self, root):
        self.root = root
        self.root.title("Main app")
        self.root.geometry("400x400")
        self.root.configure(bg="black")
        self.simple_app = SimpleApp(self.root)
        self.matplotlib_app = MatplotlibApp(self.root)
        
    def run(self):
        self.frm_top = tk.Frame(self.root,bg="black")
        self.frm_top.pack(side=tk.TOP)
        self.frm_bottom = tk.Frame(self.root,bg="black")
        self.frm_bottom.pack(side=tk.TOP)

        lbl = self.create_label(self.frm_top, text="Choose the application to run")
        lbl.pack()
        btn_first_app = self.create_button(self.frm_bottom, text="Simple app")
        btn_first_app.bind("<Button-1>", lambda event: self.choose_app(id = 0))
        btn_first_app.pack()
        
        btn_second_app = self.create_button(self.frm_bottom, text="Matplotlib app")
        btn_second_app.bind("<Button-1>", lambda event: self.choose_app(id = 1))
        btn_second_app.pack()
        
        self.root.mainloop()
    
    def choose_app(self, id):
        self.clear_frame(self.frm_bottom)
        self.clear_frame(self.frm_top)
        if id == 0:
            self.simple_app.run()
        else:
            self.matplotlib_app.run()

if "__main__" == __name__:
    gui = tk.Tk()
    app = MainApp(gui)
    app.run()