from gc import is_finalized
import pdfplumber
from gtts import gTTS
from pathlib import Path


def pdf2mp3(file_path, lang):
    if Path(file_path).is_file() and Path(file_path).suffix == '.pdf':
        with pdfplumber.PDF(open(file=file_path, mode='rb')) as pdf:
            pages = [page.extract_text() for page in pdf.pages]

        pdf_text = ''.join(pages)
        pdf_text = pdf_text.replace('\n', '')

        audio_file = gTTS(text=pdf_text, lang=lang, slow=False)
        audio_name = Path(file_path).stem
        audio_file.save(f'{audio_name}.mp3')

        return f'{audio_name}.mp3 saved!'
    else:
        return 'File not exists'

def main():
    file_path = input("Enter a path: ")
    lang = input("Enter language ('ru' or 'en'): ")
    print(pdf2mp3(file_path, lang))


if __name__ == '__main__':
    main()

