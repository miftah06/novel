Certainly! Here's an updated `readme.md` to reflect the usage of the scripts:

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