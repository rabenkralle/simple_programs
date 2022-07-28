# Movie lover 2
# Demonstration of Radio Buttons

from tkinter import *
from turtle import st

from pyparsing import col
class Application(Frame):

    def __init__(self, master):
        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        Label(self, text="Choose genres").grid(row=0, column=0, sticky=W)
        Label(self, text="Choose what you like:")
        self.favorite = StringVar()
        self.favorite.set(None)
        Radiobutton(self, 
                    text="Comedy", variable=self.favorite, value="comedy.",
                    command=self.update_text).grid(row=2, column=0, sticky=W)

        Radiobutton(self,
                    text="Drama", variable=self.favorite, value="drama.",
                    command=self.update_text).grid(row=3, column=0, sticky=W)

        Radiobutton(self, 
                    text="Action", variable=self.favorite, value="action.",
                    command=self.update_text).grid(row=4, column=0, sticky=W)
        self.result_txt = Text(self, width=40, height=5, wrap=WORD)
        self.result_txt.grid(row=5, column=0, columnspan=3)

    def update_text(self):
        message = "Your favorite genre is "
        message += self.favorite.get()
        self.result_txt.delete(0.0, END)
        self.result_txt.insert(0.0, message)

    
root = Tk()
root.title("Movie lover 2")
app = Application(root)
root.mainloop()
