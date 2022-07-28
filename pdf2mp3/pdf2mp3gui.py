from gc import is_finalized
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
        print(filename)
        showinfo(
            title='Selected File',
            message=filename
        )
        with pdfplumber.PDF(open(file=filename, mode='rb')) as pdf:
            pages = [page.extract_text() for page in pdf.pages]
        
        pdf_text = ''.join(pages)
        pdf_text = pdf_text.replace('\n', '')

        audio_file = gTTS(text=pdf_text, lang='ru', slow=False)
        audio_name = Path(filename).stem
        audio_file.save(f'{audio_name}.mp3')


root = Tk()
root.title("Guess My Number")
app = Application(root)
root.mainloop()

# def pdf2mp3(file_path, lang):
#     if Path(file_path).is_file() and Path(file_path).suffix == '.pdf':
#         with pdfplumber.PDF(open(file=file_path, mode='rb')) as pdf:
#             pages = [page.extract_text() for page in pdf.pages]

#         pdf_text = ''.join(pages)
#         pdf_text = pdf_text.replace('\n', '')

#         audio_file = gTTS(text=pdf_text, lang=lang, slow=False)
#         audio_name = Path(file_path).stem
#         audio_file.save(f'{audio_name}.mp3')

#         return f'{audio_name}.mp3 saved!'
#     else:
#         return 'File not exists'