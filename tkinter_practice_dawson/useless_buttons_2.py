# Создание класса в оконном приложении
from tkinter import *

class Application(Frame):
    # GUI приложение с тремя бесполезными кнопками

    def __init__(self, master):

        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        self.bttn1 = Button(app, text="I don't do anything")
        self.bttn1.grid()

        self.bttn2 = Button(app)
        self.bttn2.grid()
        self.bttn2.configure(text="Me too!")


        self.bttn3 = Button(app)
        self.bttn3.grid()
        self.bttn3["text"] = "Also I!"