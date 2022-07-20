from tkinter import *

class Application(Frame):
    def __init__(self, master):
        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        # Создаем кнопку, текстовое поле и текстовую область
        self.inst_lbl = Label(self, text=' To know the secret of long life, put password')
        self.inst_lbl.grid(row=0, column=0, columnspan=2, sticky=W)
        self.pw_lbl = Label(self, text='Password: ')
        self.pw_lbl.grid(row=1, column=0, sticky=W)
        self.pw_ent = Entry(self)
        self.pw_ent.grid(row=1, column=1, sticky=W)
        self.submit_bttn = Button(self, text='Show secret', command=self.reveal)
        self.submit_bttn.grid(row=2, column=0, sticky=W)
        self.secret_text = Text(self, width=35, height=5, wrap=WORD)
        self.secret_text.grid(row=3, column=0, columnspan=2, sticky=W)

    def reveal(self):
        contents = self.pw_ent.get()
        if contents == 'secret':
            message = 'Чтобы дожить до 100 лет, наджо сначала дожить до 99, ' \
                'а потом вести себя ОЧЕНЬ осторожно.'
        else:
            message='Вы ввели неправильный пароль, так что я не могу' \
                'с вами поделиться секретом.'

        self.secret_text.delete(0.0, END)
        self.secret_text.insert(0.0, message)


root = Tk()
root.title('Долгожитель')
root.geometry('350x150')
app = Application(root)
root.mainloop()

