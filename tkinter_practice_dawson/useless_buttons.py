from tkinter import *

root = Tk()
root.title("Useless buttons")
root.geometry("200x85")
app = Frame(root)
app.grid()

# Создание кнопки
bttn1 = Button(app, text="I don't do anything")
bttn1.grid()

bttn2 = Button(app)
bttn2.grid()
bttn2.configure(text="Me too!")


bttn3 = Button(app)
bttn3.grid()
bttn3["text"] = "Also I!"

root.mainloop()