from analyze import analyzeText
from tika import parser
import os
import shutil

def handlePDF(filename):
    rawText = parser.from_file('files\\' + filename)
    #rawText = {'content' : []}
    data = analyzeText(rawText['content'])
    return data

#import ebooklib
#from ebooklib import epub
from zipfile import ZipFile

def handleEPUB(filename):
    fullText = open('files/fullText', 'a+', encoding='utf-8', errors = 'ignore')
    with ZipFile('files/' + filename, 'r') as zip:
        zip.extractall()
        #print(zip.namelist())
        for name in zip.namelist():
            if '.' not in name:
                continue
            ext = name.rsplit('.', 1)[1].lower()
            if ext == 'html' or ext == 'xhtml':
                #print(name, ext)
                local = open(name, "r", encoding='utf-8', errors = 'ignore')
                #print(analyzeText(local))
                fullText.write(local.read())
                local.close()
    fullText.close()
    fullText = open('files/fullText', 'r', encoding='utf-8', errors = 'ignore')
    data = analyzeText(fullText)
    fullText.close()
    os.remove('files/fullText')
    if os.path.isdir('OEBPS'):
        shutil.rmtree('OEBPS')
    zip.close()
    #print(data)
    return data

        