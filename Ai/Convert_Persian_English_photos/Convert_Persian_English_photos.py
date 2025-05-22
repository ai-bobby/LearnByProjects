from PIL import Image
import pytesseract
import pathlib
# from googletrans import Translator
from deep_translator import GoogleTranslator
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

text = ""
# ans = input("Do you want the photo to br the translate into persian?(y/n): ")

for path in pathlib.Path(r"D:\python_projects\Ai\Convert_Persian_English_photos\per_pics").iterdir():
    if path.is_file():
        img = path
        text += pytesseract.image_to_string(Image.open(img),lang='fas')
        text += 50 * '-' + "\n"

for path in pathlib.Path(r"D:\python_projects\Ai\Convert_Persian_English_photos\eng_pics").iterdir():
    if path.is_file():
        img = path
        eng = pytesseract.image_to_string(Image.open(img),lang='eng')

        if 'y' in (ans := input("Do you want the photo to br the translate into persian?(y/n): ").lower()):
            translated = GoogleTranslator(source='auto', target='fa').translate(eng)
            text += translated 
            text += "\n"

        else:
            text += eng
            text += "\n"


        text += 50 * '-' 

with open(r"D:\python_projects\Ai\Convert_Persian_English_photos\text.txt",encoding='utf8',mode='w') as f:
    f.write(text) 