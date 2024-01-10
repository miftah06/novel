import nltk
from nltk.corpus import words

nltk.download("words")

def process_keywords(input_file):
    with open(input_file, "r", encoding="utf-8") as file:
        keywords = file.read().lower().split()

    indonesian_words = set(words.words())
    filtered_keywords = [word for word in keywords if word in indonesian_words]

    return filtered_keywords

# Gunakan fungsi di atas untuk memproses kata dari KBI.pdf atau katakunci.txt
keywords = process_keywords("katakunci.csv")  # Gantilah dengan nama file yang sesuai

# Sekarang keywords berisi kata-kata bahasa Indonesia yang valid dari dokumen input Anda
