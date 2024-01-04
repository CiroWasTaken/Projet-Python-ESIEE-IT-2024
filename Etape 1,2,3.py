from collections import Counter
import re
import requests
from bs4 import BeautifulSoup

# Etape 1: Extraction de mots et comptage d'occurrences
def extract_words_and_count(text):
    # Suppression de la ponctuation et mise en minuscule
    words = re.findall(r'\b\w+\b', text.lower())
    return dict(Counter(words))

# Etape 2: Filtrage des mots parasites
def filter_stopwords(word_dict, stopwords):
    return {word: count for word, count in word_dict.items() if word not in stopwords}

# Etape 3: Récupération des mots parasites à partir d'un fichier
def get_stopwords_from_file(file_path):
    with open(file_path, 'r') as file:
        stopwords = file.read().splitlines()
    return stopwords

# Exemple de texte pour tester les fonctions
sample_text = "Ceci est un exemple de texte pour tester l'extraction de mots. Les mots parasites comme et, ou, le, la, les seront retirés."

# Test des fonctions
word_count = extract_words_and_count(sample_text)
print("Comptage des mots :", word_count)

# Supposons que nous ayons un fichier 'stopwords.csv' avec des mots parasites
simulated_stopwords = ['et', 'ou', 'le', 'la', 'les', 'un', 'une', 'de', 'des', 'pour', 'l']

filtered_words = filter_stopwords(word_count, simulated_stopwords)
print("Mots après filtrage :", filtered_words)
