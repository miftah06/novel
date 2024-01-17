from weasyprint import HTML

def convert_html_to_pdf(html_file, output_pdf):
    HTML(string=html_file).write_pdf(output_pdf)

def main():
    # Menggunakan nama file yang sesuai dengan output dari skrip HTML
    input_html_file = 'output-cover.html'
    output_pdf_file = 'output-cover.pdf'

    # Membaca isi file HTML
    with open(input_html_file, 'r', encoding='utf-8') as html_file:
        html_content = html_file.read()

    # Mengonversi HTML ke PDF
    convert_html_to_pdf(html_content, output_pdf_file)

    print(f"File PDF telah dibuat: {output_pdf_file}")

if __name__ == "__main__":
    main()
