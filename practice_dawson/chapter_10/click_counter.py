from tkinter import *

class Application(Frame):
    def __init__(self, master):
        super(Application, self).__init__(master)
        self.grid()
        self.bttns_click = 0 # Количество нажатий на кнопку
        self.create_widget()

    def create_widget(self):
        self.bttn = Button(self)
        self.bttn['text'] = 'Click count: 0'
        self.bttn['command'] = self.update_count
        self.bttn.grid()
    
    def update_count(self):
        self.bttns_click += 1
        self.bttn['text'] = 'Click count: ' + str(self.bttns_click)


root = Tk()
root.title('Click counter')
root.geometry('200x50')
app = Application(root)
root.mainloop()