from tkinter import *

import gui
from gui import *

class Question2:
    def Quest2(self):
        self.window2 = (gui.window)
        self.window2.geometry("1280x720")
        self.window2.title("Iglok Quiz Game")
        self.window2.config(background="#BAC6CF")

        self.labelw2 = Label(self.window2, text="Iglok Quiz Game", font=('Arial',  40, 'bold'),fg='#625FEA', bg="#BAC6CF",)
        self.labelw2.pack()
        self.labelw21 = Label(self.window2, text="2. Jaka postać jest najniższa?? ", font=('Arial', 20), pady=25, bg="#BAC6CF")
        self.labelw21.pack()
        self.window2.mainloop()