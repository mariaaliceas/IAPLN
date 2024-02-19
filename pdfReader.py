import PyPDF2
from PyPDF2 import PdfReader

arquivo = PdfReader("download.pdf")
page = arquivo.pages[0]
number_of_pages = len(arquivo.pages)
lista = list(arquivo)

def removeStopWords(arquivo):

     stopWords = [" is "," a ", " the ", " are "]

     while number_of_pages < -1:
          print("TESTE")


removeStopWords(arquivo)

# print(type(arquivo))

# from PyPDF2 import PdfReader

# reader = PdfReader("download.pdf")
# page = reader.pages[0]
# number_of_pages = len(reader.pages)


# print(number_of_pages)

# def removeStopWords(reader):

#     stopWords = [" is "," a ", " the ", " are "]

#     while reader < 
#     if reader == stopWords:
#         print(stopWords) 


