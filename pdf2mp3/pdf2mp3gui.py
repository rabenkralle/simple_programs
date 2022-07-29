# pdf 2 mp3 converter версия с GUI


from gc import is_finalized
from matplotlib.pyplot import text
import pdfplumber
from gtts import gTTS
from pathlib import Path
from tkinter import Button, filedialog as fd, ttk
from tkinter.messagebox import showinfo
from tkinter import *


class Application(Frame):
    def __init__(self, master):
        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        Label(self, text="Choose pdf file").grid(row=0, 
        column=0, columnspan=2, sticky=W)
        Label(self, text="Choose language:").grid(row=1, column=0, sticky=W)
        self.body_part = StringVar()
        self.body_part.set(None)
        body_parts = ["English", "Russian"]
        column = 1
        for part in body_parts:
            Radiobutton(self, text=part, variable=self.body_part, 
            value=part).grid(row=1, column=column, sticky=W)
            column += 1
        ttk.Button(self, text="Open file", command=self.select_file).grid(row=2, 
        column=0, sticky=W)
        
    def select_file(self):
        filetypes = (
            ('pdf files', '*.pdf'),
            ('All files', '*.*')
        )

        filename = fd.askopenfilename(
            title='Open a file',
            initialdir='/',
            filetypes=filetypes)
        
        showinfo(
            title='Selected File',
            message=filename
        )

        if self.body_part.get() == 'English':
            lang = 'en'
        else:
            lang = 'ru'

        if Path(filename).is_file() and Path(filename).suffix == '.pdf':
            with pdfplumber.PDF(open(file=filename, mode='rb')) as pdf:
                pages = [page.extract_text() for page in pdf.pages]
            
            pdf_text = ''.join(pages)
            pdf_text = pdf_text.replace('\n', '')

            audio_file = gTTS(text=pdf_text, lang=lang, slow=False)
            audio_name = Path(filename).stem
            audio_file.save(f'{audio_name}.mp3')
            showinfo(
                title='Saved',
                message=f'{audio_name}.mp3 saved'
            )
        else:
            showinfo(
                title='Error',
                message='Choose PDF file')


root = Tk()
root.title("Guess My Number")
app = Application(root)
root.mainloop()

