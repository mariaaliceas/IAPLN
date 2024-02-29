import PyPDF2
import nltk
nltk.download('stopwords')
nltk.download('punkt')

from PyPDF2 import PdfReader
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize, RegexpTokenizer
from collections import Counter

tratar_texto = True

pdf_file = open("articles/1.pdf", 'rb')

pdf_reader = PyPDF2.PdfReader(pdf_file)
text = ''
tokenizer = RegexpTokenizer(r'\w+')

for i in range(len(pdf_reader.pages)):
    page = pdf_reader.pages[i]
    text += page.extract_text()

text = text.lower()
words = tokenizer.tokenize(text)
texto = []
references = []
bag_of_words = []
most_commons = []
reference = False

for i, word in enumerate(words):
    if (word == 'r' and words[i+1] == 'eferences') or (word == 'references' and words[i+1] == '1'):
        reference = True
    if reference:
        if word == 'authorized':
            references.pop()
            break
        references.append(word.lower())
    else:
        texto.append(word.lower())

if not tratar_texto:
    True
else:
    stop_words = stopwords.words('english')

    for word in words:
        if (word == 'r' and words[i+1] == 'eferences') or (word == 'references' and words[i+1] == '1'):
                reference = True
        if (word not in stop_words) and not reference:
            texto.append(word)
        elif (word not in stop_words) and reference:
            if word == 'authorized':
                references.pop()
                break
            references.append(word)

    porter = nltk.PorterStemmer()
    stemm_words = [porter.stem(w) for w in texto]
    # print(stemm_words)

bag_of_words = Counter(texto)
most_commons = bag_of_words.most_common(10)
print(texto)
#print(references)
#print(bag_of_words)
#print(most_commons)
