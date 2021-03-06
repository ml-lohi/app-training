import threading
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk  
import numpy as np
import time
from utils.app_interface import AppInterface
from utils.helper import fft

class MatplotlibApp(AppInterface):
    def __init__(self, root=None):
        self.root = root
        self.plotFrame = tk.Frame(self.root, bg="black")
        self.plotFrame.pack(side = tk.RIGHT)
        self.buttonFrame = tk.Frame(self.root, bg="black")
        self.buttonFrame.pack(side = tk.LEFT)
        self.plot_active= True
        self.xdata = []
        self.ydata = []
        self.br = 0
        self.strVarBr = tk.StringVar()
        self._reset_hr_br()

    def _reset_hr_br(self) :
        self.strVarBr.set(f"Some counter: {self.br}")
        self.root.update()
    
    def run(self):
        fig,axs=plt.subplots(2,1,figsize=(2,3))
        fig.patch.set_facecolor('xkcd:black')
        fig.tight_layout()
        canvas=FigureCanvasTkAgg(fig,master=self.plotFrame)
        canvas.get_tk_widget().grid(row=0,column=1)
        canvas.draw()
        self.thread = threading.Thread(target=self._process, args=(canvas,axs))
        self.thread.setDaemon(True)
        self.thread.start()
        
        self.button_stop = self.create_button(self.buttonFrame, text="Stop")
        self.button_stop.bind("<Button-1>", lambda event: self.stop_plotting())
        self.button_stop.pack()
        self.button_start = self.create_button(self.buttonFrame, text="Start")
        self.button_start.bind("<Button-1>", lambda event: self.start_plotting())
        self.button_start.pack()
        self.button_start = self.create_button(self.buttonFrame, text="Restart")
        self.button_start.bind("<Button-1>", lambda event: self.restart())
        self.button_start.pack()
        
        lbl = self.create_label_var(self.buttonFrame, textvariable=self.strVarBr)
        lbl.pack()
    
    def stop_plotting(self):
        self.plot_active = False
    
    def start_plotting(self):
        self.plot_active = True
    
    def restart(self):
        self.x = 0
        self.xdata = []
        self.ydata = []
        self.br = 0
        
    def _process(self, canvas, axs):
        for ax in axs:
            ax.set_facecolor('xkcd:black')
            color = "white"
            ax.xaxis.label.set_color(color)
            ax.yaxis.label.set_color(color)
            ax.tick_params(axis='x', colors=color)
            ax.tick_params(axis='y', colors=color)
        self.x = 0
        while True:
            if self.plot_active:
                self.xdata.append(self.x)
                self.ydata.append(np.sin(self.x*np.pi))
                fftx,ffty = fft(np.array(self.ydata))
                self._plot(canvas,axs, fftx,ffty)
                time.sleep(0.1)
                self.br = self.br + 1
                self._reset_hr_br()
                self.x = self.x + 0.1

    def _plot(self, canvas,axs,fftx,ffty):
        for i, ax in enumerate(axs):
            ax.clear()         # clear axes from previous plot
            if i == 1:
                ax.plot(fftx,ffty, color = "green")
            else:
                ax.plot(self.xdata,self.ydata, color = "green")
        
        canvas.draw()
    
if "__main__" == __name__:
    root=tk.Tk()
    root.title("Main app")
    root.geometry("400x400")
    root.configure(bg="black")
    app=MatplotlibApp(root=root)
    app.run()
    root.mainloop()
    