"""
    All the explaination in
    https://realpython.com/python-gui-tkinter/
    https://medium.com/swlh/easy-steps-to-create-an-executable-in-python-using-pyinstaller-cc48393bcc64
"""
from dataclasses import dataclass
import tkinter as tk

from utils.app_interface import AppInterface


class SimpleApp(AppInterface):
    def __init__(self, root):
        self.root = root     
    
    def run(self):
        self.frm_left = tk.Frame(self.root,bg="black")
        self.frm_left.pack(side=tk.LEFT)
        self.frm_right = tk.Frame(self.root,bg="black")
        self.frm_right.pack(side=tk.RIGHT)

        label = self.create_label(self.frm_left, text="Write smth:")
        label.pack()
        entry = self.create_entry(self.frm_left)
        entry.pack()
        name = entry.get()
        btn_clean = self.create_button(self.frm_right, text="Clean")
        btn_clean.bind("<Button-1>", lambda event: entry.delete(0, tk.END))
        btn_clean.pack()
        
        btn_insert = self.create_button(self.frm_right, text="Insert")
        btn_insert.bind("<Button-1>", lambda event: entry.insert(0, "Python is cool"))
        btn_insert.pack()
        
        btn_back = self.create_button(self.frm_left, text="Back")
        btn_back.bind("<Button-1>", lambda event: self.back())
        btn_back.pack()

    def back(self):
        self.destroy()      

if "__main__" == __name__:
    root = tk.Tk()
    root.title("Main app")
    root.geometry("400x400")
    root.configure(bg="black")
    app = SimpleApp(root)
    app.run()
    root.mainloop()
    