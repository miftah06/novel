import pandas as pd
import numpy as np
import random

def generate_object_names(keywords_file, num_objects=1000):
    # Membaca kata kunci dari file dengan menggunakan encoding 'utf-8' dan menangani kesalahan dekoding
    with open(keywords_file, 'r', encoding='utf-8', errors='ignore') as file:
        keywords = file.read().splitlines()

    # Memastikan jumlah kata kunci cukup untuk menghasilkan objek
    if len(keywords) < 5000:
        raise ValueError("Jumlah kata kunci harus minimal 5000 untuk menghasilkan objek.")

    # Menghasilkan nama objek secara acak
    object_names = []
    for _ in range(num_objects):
        first_word = random.choice(keywords)
        second_word = random.choice(keywords)
        object_name = f"{first_word} {second_word}".rstrip()  # Remove trailing spaces
        object_names.append(object_name)

    # Membuat DataFrame dengan nama objek
    data = {'Nama Objek Jawaban': object_names}
    df = pd.DataFrame(data)

    return df

# Contoh penggunaan
keywords_file = 'katakunci.txt'  # Ganti dengan file yang berisi kata kunci
num_objects_to_generate = 8000  # Ganti dengan jumlah objek yang ingin dihasilkan
generated_objects = generate_object_names(keywords_file, num_objects_to_generate)

# Menyimpan DataFrame ke file CSV
generated_objects.to_csv('katakunci.csv', index=False)

print(f"{num_objects_to_generate} Nama objek telah disimpan ke dalam katakunci.csv")
