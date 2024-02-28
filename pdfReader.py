import PyPDF2
import nltk
nltk.download('stopwords')
nltk.download('punkt')

from PyPDF2 import PdfReader
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize, RegexpTokenizer
from collections import Counter

pdf_file = open("download.pdf", 'rb')

pdf_reader = PyPDF2.PdfReader(pdf_file)
text = ''
tokenizer = RegexpTokenizer(r'\w+')

for i in range(len(pdf_reader.pages)):
    page = pdf_reader.pages[i]
    text += page.extract_text()

'''
    tratar texto limpo
    retirar as referencias
'''

words = tokenizer.tokenize(text)
texto = []
references = []
reference = False
for word in words:
    if word == 'REFERENCES':
        reference = True
    if reference:
        if word == 'Authorized':
            references.pop()
            break
        references.append(word)
    else:
        texto.append(word.lower())
    
bag_of_words = Counter(texto).most_common(10)
#print(texto)
print(references)
print(bag_of_words)

'''
    stop words, lematizacao, stemming

'''
text = text.lower()

stop_words = stopwords.words('english')
# print(stop_words)

palavras = tokenizer.tokenize(text)
# print(words)

texto_limpo = []
references = []
reference = False

for word in palavras:
    if (word not in stop_words):
        texto_limpo.append(word)
        if(word == 'references'):
            reference = True
    elif (word not in stop_words) and reference:
        if word == 'authorized':
            references.pop()
            break
        references.append(word)
    
# print(texto_limpo)
# print(references)

porter = nltk.PorterStemmer()
counts = [porter.stem(w) for w in texto_limpo]

print(Counter(counts).most_common(10))
