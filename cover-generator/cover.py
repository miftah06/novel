import os
import pandas as pd
from bs4 import BeautifulSoup
from fpdf import FPDF
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image

def validate_length(judul, Novel):
    while len(judul) != len(Novel[0]):
        print("Panjang judul tulisan Novel dan salah satu dari tulisan opsional harus sama.")
        judul = input("Masukkan judul: ").strip()

    # Menerima input untuk setiap opsional
    opsional = []
    for i in range(4):
        prompt = f"Opsional berupa keterangan misal: ex: \n 1.Berangkat dari kisah bla bla,\n 2. Di buat oleh xxx, \n 3. untuk xxx \n 4. fantasy story by xxx...\n dengan jumlah kata yang harus sama ya! \n  {i + 1}: "
        input_opsional = input(prompt).strip()
        opsional.append(input_opsional)

    # Menambahkan input judul_karya dan jenis_karyatulis
    judul_karya = input("Masukkan judul karya: ").strip()
    jenis_karyatulis = input("Masukkan jenis karya tulis: ").strip()

    return judul, opsional, judul_karya, jenis_karyatulis

def generate_pdf(data):
    doc = SimpleDocTemplate("output-cover.pdf", pagesize=letter)
    styles = getSampleStyleSheet()

    content = []

    # Add title
    title_text = "<br/><br/><br/>"
    content.append(Paragraph(title_text, styles['Title']))

    # Add cover image
    cover_image_url = data['Logo'][0]
    cover_image = Image(cover_image_url, width=400, height=400)
    content.append(cover_image)

    # Add details
    details_text = f"<br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/>"
    details_text += f"<font size='14'>{data['Judul_karya'][0]}</font><br/><br/>"
    details_text += f"<font size='12'>{data['Opsional 1'][0]}</font><br/>"
    details_text += f"<font size='12'>{data['Opsional 2'][0]}</font><br/>"
    details_text += f"<font size='12'>{data['Opsional 3'][0]}</font><br/>"
    details_text += f"<font size='12'>{data['Opsional 4'][0]}</font><br/><br/>"
    details_text += f"<font size='12'>Oleh: {data['Oleh'][0]}</font><br/>"
    details_text += f"<font size='12'>{data['NIM'][0]}</font><br/>"
    details_text += f"<font size='12'>{data['Universitas'][0]}</font><br/>"
    details_text += f"<font size='12'>{data['Tahun'][0]}</font>"

    content.append(Paragraph(details_text, styles['BodyText']))

    doc.build(content)

def main():
    print("Selamat datang!\n untuk judul kita batasi jadi 8 kalimat \n dan tidak boleh berkereta api!")

    # Meminta input dari pengguna
    judul, opsional, judul_karya, jenis_karyatulis = validate_length("", [[] for _ in range(4)])  # Menyesuaikan dengan perubahan dalam validate_length
    logo = input("Masukkan Gambar Cover (URL): ").strip()

    oleh = input("Masukkan nama: ").strip()
    nim = input("Masukkan Nomor Peserta/ Inisial: ").strip()
    fakultas = input("Masukkan Jenis Tema: ").strip()
    universitas = input("Masukkan Copyrighting: ").strip()
    tahun = input("Masukkan tahun (contoh: 2024): ").strip()

    # Membuat DataFrame dari input
    data_dict = {
        'Logo': [logo],
        'Opsional 1': [opsional[0]],
        'Opsional 2': [opsional[1]],
        'Opsional 3': [opsional[2]],
        'Opsional 4': [opsional[3]],
        'Oleh': [oleh],
        'NIM': [nim],
        'Fakultas': [fakultas],
        'Universitas': [universitas],
        'Tahun': [tahun],
        'Judul_karya': [judul_karya],
        'Jenis_karyatulis': [jenis_karyatulis]
    }

    # Membuat file HTML dari data
    html_content = generate_html(data_dict)

    # Menyimpan HTML ke dalam file
    with open('output-cover.html', 'w', encoding='utf-8') as html_file:
        html_file.write(html_content)

    print("\nProses selesai. File HTML yang menawan tersedia di output-cover.html.")

    # Membuat file PDF dari data
    generate_pdf(data_dict)

def generate_html(data):
    # Membaca URL gambar cover dari file external
    with open('cover_image_url.txt', 'r') as url_file:
        cover_image_url = url_file.read().strip()

    # Template HTML dengan Bootstrap dan estetika yang ditingkatkan
    template = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <link rel="stylesheet" href="styles.css">
        <title>{data['Judul_karya'][0]}</title>
        <style>
            body {{
                margin: 0;
                font-family: 'Times New Roman', serif;
                color: white;
            }}
            .background {{
                position: fixed;
                top: 0;
                left: 0;
                width: 100%;
                height: 100%;
                overflow: hidden;
                z-index: -1;
            }}
            .background-image {{
                width: 100%;
                height: auto;
                filter: brightness(70%) opacity(0.7);
            }}
            .content {{
                position: relative;
                text-align: center;
                padding: 20px;
                z-index: 1;
            }}
            .centered-image {{
                max-width: 100%;
                height: auto;
                margin-top: 86px;
                margin-left: auto;
                margin-right: auto;
                display: block;
            }}
            h1 {{
                font-size: 3em;
                line-height: 1.2em;
                margin-bottom: 20px;
            }}
            p.optional {{
                font-size: 1.5em;
                line-height: 1.5em;
                margin-bottom: 10px;
            }}
            p.highlighted {{
                background-color: red;
                padding: 5px;
                display: inline-block;
                border-radius: 5px;
            }}
            .author span,
            .university,
            .year,
            .student-id span {{
                background-color: red;
                padding: 5px;
                display: inline-block;
                border-radius: 5px;
                margin-bottom: 10px;
            }}
            /* Add additional styles or modify existing ones based on your design preferences */
        </style>
    </head>
    <body>
        <div class="background">
            <img src="{cover_image_url}" alt="Cover Image" class="background-image">
        </div>
        <div class="content">
            <img src="{cover_image_url}" alt="Cover Image" class="centered-image">
            <h1>{data['Judul_karya'][0]}</h1>
            <p class="optional">{data['Opsional 1'][0]}</p>
            <p class="optional">{data['Opsional 2'][0]}</p>
            <p class="optional">{data['Opsional 3'][0]}</p>
            <p class="optional">{data['Opsional 4'][0]}</p>
            <p class="optional highlighted">Oleh: <span>{data['Oleh'][0]}</span></p>
            <p class="optional">{data['NIM'][0]}</p>
            <p class="optional university">{data['Universitas'][0]}</p>
            <p class="optional year">{data['Tahun'][0]}</p>
        </div>
    </body>
    </html>
    """

    # Hapus ". nan." dari teks
    template = template.replace(". nan.", "")

    return template

def main():
    print("Selamat datang!\n untuk judul kita batasi jadi 8 kalimat \n dan tidak boleh berkereta api!")

    # Meminta input dari pengguna
    judul, opsional, judul_karya, jenis_karyatulis = validate_length("", [[] for _ in range(4)])  # Menyesuaikan dengan perubahan dalam validate_length
    logo = input("Masukkan Gambar Cover (URL): ").strip()

    oleh = input("Masukkan nama: ").strip()
    nim = input("Masukkan Nomor Peserta/ Inisial: ").strip()
    fakultas = input("Masukkan Jenis Tema: ").strip()
    universitas = input("Masukkan Copyrighting: ").strip()
    tahun = input("Masukkan tahun (contoh: 2024): ").strip()

    # Membuat DataFrame dari input
    data_dict = {
        'Logo': [logo],
        'Opsional 1': [opsional[0]],
        'Opsional 2': [opsional[1]],
        'Opsional 3': [opsional[2]],
        'Opsional 4': [opsional[3]],
        'Oleh': [oleh],
        'NIM': [nim],
        'Fakultas': [fakultas],
        'Universitas': [universitas],
        'Tahun': [tahun],
        'Judul_karya': [judul_karya],
        'Jenis_karyatulis': [jenis_karyatulis]
    }

    # Menyimpan PDF
    generate_pdf(data_dict)
    print(f"\nProses selesai. File PDF tersedia di output-cover.pdf.")

    # Menyimpan URL gambar cover ke file external untuk digunakan dalam HTML
    with open('cover_image_url.txt', 'w') as url_file:
        url_file.write(logo)

    # Membuat file HTML dari data
    html_content = generate_html(data_dict)

    # Menyimpan HTML ke dalam file
    with open('output-cover.html', 'w', encoding='utf-8') as html_file:
        html_file.write(html_content)

    print("\nProses selesai. File HTML yang menawan tersedia di output-cover.html.")

if __name__ == "__main__":
    main()
