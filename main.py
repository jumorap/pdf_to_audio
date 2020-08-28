import pyttsx3
import PyPDF2
from tkinter.filedialog import *

# We question to user what file require transform to audiobook
# with [pdf_file], after we send it to be read in [pdf_reader]
# and [pages] count the number of pages to be used in the loop
pdf_file = askopenfilename()
pdf_reader = PyPDF2.PdfFileReader(pdf_file)
pages = pdf_reader.numPages

# We extract the text in the pages and be started the audio-text player
for number in range(1, pages):
    page = pdf_reader.getPage(number)
    text = page.extractText()
    player = pyttsx3.init()

    print(text)

    player.say(text)
    player.runAndWait()

