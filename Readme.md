Novel-Generator adalah skrip sederhana untuk menghasilkan Novel acak dalam bentuk ke pdf, untuk mengeditnya bisa ubah dulu
ke dalam bentuk txt atau docx dengan pdf converter tools . Skrip ini memungkinkan pengguna untuk membuat sejumlah soal pilihan ganda dengan variasi yang dapat dikonfigurasi.
Cara Menggunakan

    Pastikan Python sudah terinstal di sistem Anda. Jika belum, Anda dapat mengunduhnya dari python.org.

    Unduh proyek ini ke sistem Anda atau gunakan perintah git clone:

    bash
git clone https://github.com/miftah06/novel.git

cd novel

python nulis.py

```markdown
# Novel Generator Scripts

## `hasilkan.py`

This script generates object names based on keywords stored in `katakunci.txt`. It generates 10,000 object names and saves them to `katakunci.txt`.

```bash
python hasilkan.py
```

## `generator.py`

This script generates object names based on keywords stored in `katakunci.txt` and saves them to a CSV file (`katakunci.csv`). It generates 8,000 object names.

```bash
python generator.py
```

## `proses.py`

This script processes keywords and performs natural language processing using the NLTK library. It ensures that the NLTK words package is up-to-date.

```bash
python proses.py
```

## `Cara menghasilkan novel dalam bentuk pdf`

This script constructs a novel narrative based on user input, processed keywords from CSV and TXT files, and randomizes the synopsis. It saves the output in both HTML (`output_novel.html`) and PDF (`novel.pdf`) formats.

## WINDOWS

```bash
python wnulis.py
```
## TERMUX


```bash
python nulis.py
```

### Requirements


```bash
pip install -r requirements.txt
```

- NLTK
- pdfkit
- random
- numpy
- pandas

### Usage

1. Run `hasilkan.py` to generate object names.
2. Run `generator.py` to generate object names in CSV format.
3. Run `proses.py` to ensure NLTK is up-to-date.
4. Run `wnulis.py` atau `nulis.py` to create a novel based on user input and generated object names.

### Example Workflow

```bash
python hasilkan.py
python generator.py
python proses.py
python wnulis.py
```

The generated novel content will be saved in both HTML (`output_novel.html`) and PDF (`novel.pdf`) formats.
```

Feel free to adjust this readme according to your project's structure and additional details!