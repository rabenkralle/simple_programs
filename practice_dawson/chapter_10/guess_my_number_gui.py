# Guess My Number
#
# The computer picks a random number between 1 and 100
# The player tries to guess it and the computer lets
# the player know if the guess is too high, too low
# or right on the money

import random  
from tkinter import *


class Application(Frame):
    # GUI application where player tries to guess random number. 
    def __init__(self, master):
        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()
        self.tries = 1
        self.the_number = random.randint(1, 100)

    def create_widgets(self):
        Label(self, text="Try to guess a number between 1 and 100").grid(row=0, 
        column=0, columnspan=2, sticky=W)
        Label(self, text="Your number:").grid(row=1, column=0, sticky=W)
        self.your_number = Entry(self)
        self.your_number.grid(row=1, column=1, sticky=W)
        Button(self, text="Guess a number", command=self.guess_number).grid(row=2, 
        column=0, sticky=W)
        self.answer_txt = Text(self, width=40, height=3, wrap=WORD)
        self.answer_txt.grid(row=3, column=0, columnspan=4)

    def guess_number(self):
        guess = int(self.your_number.get())
        
       
        if guess > self.the_number:
            self.answer_txt.delete(0.0, END)
            self.answer_txt.insert(0.0, 'Lower...')
        elif guess < self.the_number:
            self.answer_txt.delete(0.0, END)
            self.answer_txt.insert(0.0, 'Higher...')
        else:
            final_text = f"You guessed it!  The number was {self.the_number}. \
            And it only took you {self.tries} tries!"
            self.answer_txt.delete(0.0, END)
            self.answer_txt.insert(0.0, final_text)    
            self.the_number = random.randint(1, 100)
            self.tries = 0

        self.tries += 1
        

root = Tk()
root.title("Guess My Number")
app = Application(root)
root.mainloop()


        
