import PyPDF2
import nltk
nltk.download('stopwords')
nltk.download('punkt')

from PyPDF2 import PdfReader
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize, RegexpTokenizer
from collections import Counter

tratar_texto = True

pdf_file = open("articles/5.pdf", 'rb')

pdf_reader = PyPDF2.PdfReader(pdf_file)
text = ''

for i in range(len(pdf_reader.pages)):
    page = pdf_reader.pages[i]
    text += page.extract_text()

text = text.lower()
words = word_tokenize(text)
sentences = sent_tokenize(text)
sentences_treatment = []

for sentence in sentences:
     sentences_treatment.append(sentence.replace('\n', " "))

texto = []
references = []
bag_of_words = []
most_commons = []
reference = False

list_words = ['idea','inspired','analyzed','have seen','organized','developed','proposes','approach','develop','introduced','contribute','explain','introduces']
list_problems = ['building','accepts','solving','challenge','issue','problem','obstacle','dilemma','difficulty','barrier','impediment','hurdle','complication']
list_methods = ['method', 'methodology', 'interviews', 'survey', 'content analysis']
list_contributions = ['type of teaching']

def remove_references(reference):
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

def text_treatment(word):
    reference = []
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
        
def get_objective(sentences, list_words):
    objective = ''
    for sentence in sentences:
        s = sentence.replace('\n', '')
        if(any(substring in s for substring in list_words)):
            objective = sentence
            break
    print(objective)    

def get_problem(sentences, list_problems):
    problem = ''
    for sentence in sentences:
        s = sentence.replace('\n', '')
        if(any(substring in s for substring in list_problems)):
            problem = sentence
            break
    print(problem)   

def get_method(sentences, list_methods):
    method = ''
    for sentence in sentences:
        s = sentence.replace('\n', '')
        if(any(substring in s for substring in list_methods)):
            method = sentence
            break
    print(method)

def get_contribution(sentences, list_contributions):
    contribution = ''
    for sentence in sentences:
        s = sentence.replace('\n', '')
        if(any(substring in s for substring in list_contributions)):
            contribution = sentence
            break
    print(contribution)    


bag_of_words = Counter(texto)
most_commons = bag_of_words.most_common(10)
#remove_references(words)
#text_treatment(words)
#get_objective(sentences,list_words)
#get_problem(sentences,list_problems)
#get_method(sentences,list_methods)
get_contribution(sentences,list_contributions)
#print(words)



