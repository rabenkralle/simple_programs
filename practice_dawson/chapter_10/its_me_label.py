from tkinter import *
# Создание базового окна
root = Tk()
root.title("It's me, label!")
root.geometry('200x50')

# Рамка внутри окна для размещения других элементов
app = Frame(root)
app.grid()

# Создание метки внутри рамки
lbl = Label(app, text = "It's me!")
lbl.grid()

root.mainloop()
