import PyPDF2
import nltk
import json
import os

nltk.download('stopwords')
nltk.download('punkt')

from PyPDF2 import PdfReader
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize, RegexpTokenizer
from collections import Counter

tratar_texto = True

def process_pdf(pdf_file_path):
    pdf_file = open(pdf_file_path, 'rb')
    pdf_reader = PyPDF2.PdfReader(pdf_file)
    tokenizer = RegexpTokenizer(r'\w+')
    text = ''

    for page in pdf_reader.pages:
        text += page.extract_text()

    text = text.replace('\n', '')
    text = text.replace('\r', '')
    text = text.lower()
    words = tokenizer.tokenize(text)
    sentences = sent_tokenize(text)
    sentences_treatment = []

    for sentence in sentences:
        sentences_treatment.append(sentence.replace('\n', " "))

    texto = []
    references = []
    bag_of_words = []
    most_commons = []
    objective = ''
    problem = ''
    method = ''
    contribution = ''
    reference = False

    list_words = ['idea', 'inspired', 'analyzed', 'have seen', 'organized', 'developed', 'proposes', 'approach', 'develop', 'introduced', 'contribute', 'explain', 'introduces']
    list_problems = ['building', 'accepts', 'solving', 'challenge', 'issue', 'problem', 'obstacle', 'dilemma', 'difficulty', 'barrier', 'impediment', 'hurdle', 'complication']
    list_methods = ['method', 'methodology', 'interviews', 'survey', 'content analysis']
    list_contributions = ['type of teaching', 'contribution', 'contributions', 'findings', 'results', 'insights', 'conclusions', 'implications', 'significance', 'impact', 'relevance', 'discoveries', 'advances', 'key points', 'novelty', 'originality']

    def remove_references(reference):
        for i, word in enumerate(words):
            if (word == 'r' and words[i + 1] == 'eferences') or (word == 'references' and words[i + 1] == '1'):
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
                if (word == 'r' and words[i + 1] == 'eferences') or (word == 'references' and words[i + 1] == '1'):
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
        for sentence in sentences:
            s = sentence.replace('\n', '')
            if (any(substring in s for substring in list_words)):
                return sentence

    def get_problem(sentences, list_problems):
        for sentence in sentences:
            s = sentence.replace('\n', '')
            if (any(substring in s for substring in list_problems)):
                return sentence

    def get_method(sentences, list_methods):
        for sentence in sentences:
            s = sentence.replace('\n', '')
            if (any(substring in s for substring in list_methods)):
                return sentence

    def get_contribution(sentences, list_contributions):
        for sentence in sentences:
            s = sentence.replace('\n', '')
            if (any(substring in s for substring in list_contributions)):
                return sentence

    bag_of_words = Counter(words)
    most_commons = bag_of_words.most_common(10)
    objective = get_objective(sentences, list_words)
    problem = get_problem(sentences, list_problems)
    method = get_method(sentences, list_methods)
    contribution = get_contribution(sentences, list_contributions)

    article = {
        "data": {
            "name": pdf_file_path,
            "bag_of_words": bag_of_words,
            "most_commons": most_commons,
            "objective": objective,
            "problem": problem,
            "method": method,
            "contribution": contribution
        }
    }

    return article

# List to hold processed articles
articles = []

# Directory containing PDF files
pdf_directory = "articles/"

# Process each PDF file in the directory
for filename in os.listdir(pdf_directory):
    if filename.endswith(".pdf"):
        pdf_path = os.path.join(pdf_directory, filename)
        article_data = process_pdf(pdf_path)
        articles.append(article_data)

# Write all articles to JSON
with open("datafile.json", "w") as write:
    json.dump(articles, write)
