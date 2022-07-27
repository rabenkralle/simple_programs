# Movie lover
# Demonstration of Check Buttons

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
        self.likes_comedy = BooleanVar()
        Checkbutton(self, 
                    text="Comedy", variable=self.likes_comedy, 
                    command=self.update_text).grid(row=2, column=0, sticky=W)

        self.likes_drama = BooleanVar()
        Checkbutton(self,
                    text="Drama", variable=self.likes_drama, 
                    command=self.update_text).grid(row=3, column=0, sticky=W)

        self.likes_action = BooleanVar()
        Checkbutton(self, 
                    text="Action", variable=self.likes_action, 
                    command=self.update_text).grid(row=4, column=0, sticky=W)
        self.result_txt = Text(self, width=40, height=5, wrap=WORD)
        self.result_txt.grid(row=5, column=0, columnspan=3)

    def update_text(self):
        likes = ""
        if self.likes_comedy.get():
            likes += "You like comedies!\n"
        if self.likes_drama.get():
            likes += "You prefer dramas.\n"
        if self.likes_action.get():
            likes += "You're Goddamn action lover!\n"
        self.result_txt.delete(0.0, END)
        self.result_txt.insert(0.0, likes)

    
root = Tk()
root.title("Movie lover")
app = Application(root)
root.mainloop()
