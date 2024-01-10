import nltk
import random
import pdfkit

nltk.download("words")

def process_keywords_from_csv(input_file):
    with open(input_file, "r", encoding="utf-8") as file:
        keywords_csv = file.read().lower().split(',')
    return list(set(keywords_csv))  # Remove duplicates and convert to list

def process_keywords_from_txt(input_file):
    with open(input_file, "r", encoding="utf-8") as file:
        keywords_txt = file.read().lower().split()
    return list(set(keywords_txt))  # Remove duplicates and convert to list

def construct_novel_html(title, synopsis, keywords_csv, keywords_txt):
    novel_content = [f"<h1>{title}</h1>\n\n"]

    # Adding the synopsis without randomizing words
    novel_content.append(f"<p><strong>Sinopsis:</strong> {synopsis}</p>\n\n")

    # Adding unique keywords from CSV to the plot
    for keyword in keywords_csv:
        novel_content.append(f"<p>{keyword}, </p>")

    # Adding unique keywords from TXT to the plot
    for keyword in keywords_txt:
        novel_content.append(f"<p>{keyword}... </p>")

    # Closing statement
    closing_statement = "Terima kasih atas perhatiannya. Semoga Anda menikmati cerita ini."
    novel_content.append(f"<p>{closing_statement}</p>")

    # Save the constructed novel content to a file
    save_novel_to_file(novel_content)

def save_novel_to_file(novel_content):
    with open("output_novel.html", "w", encoding="utf-8") as file:
        file.writelines(novel_content)

    print("Novel content saved to 'output_novel.html.'")

def generate_pdf(title):
    pdf_filename = "novel.pdf"

    # Convert HTML to PDF with custom CSS for better aesthetics
    options = {
        'page-size': 'Letter',
        'margin-top': '50px',
        'margin-right': '50px',
        'margin-bottom': '50px',
        'margin-left': '50px',
        'encoding': "UTF-8",
        'no-outline': None,
    }
    pdfkit.from_file("output_novel.html", pdf_filename, options=options)

    print(f"PDF generated successfully: {pdf_filename}")

# Example usage:
judul_cerita = input("Masukkan judul cerita: ")
sinopsis = input("Masukkan sinopsis cerita: ")

# Process keywords from CSV and TXT
keywords_csv = process_keywords_from_csv("katakunci.csv")
keywords_txt = process_keywords_from_txt("katakunci.txt")

# Construct novel narrative based on keywords
construct_novel_html(judul_cerita, sinopsis, keywords_csv, keywords_txt)

# Generate PDF with enhanced aesthetics
generate_pdf(judul_cerita)
