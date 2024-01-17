import csv

def generate_html(data):
    # Template HTML dengan Bootstrap dan estetika yang ditingkatkan
    template = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>{data['Judul'][0]}</title>
        <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css">
        <style>
            body {{
                margin: 4%;
                font-family: 'Arial', sans-serif;
                background-color: #f8f9fa; /* Warna latar belakang yang lembut */
            }}
            .container {{
                margin: auto;
                width: 80%;
                background-color: #ffffff; /* Warna latar belakang konten */
                padding: 20px;
                border-radius: 10px; /* Border-radius untuk tampilan lebih bulat */
                box-shadow: 0 0 10px rgba(0, 0, 0, 0.1); /* Efek bayangan untuk efek 3D */
            }}
            h1 {{
                text-align: center;
                color: #007bff; /* Warna judul yang menarik perhatian */
            }}
            .logo-container {{
                text-align: center;
                margin-bottom: 20px;
            }}
            .logo-container img {{
                max-width: 100%;
                height: auto;
                border-radius: 10px; /* Border-radius untuk gambar lebih bulat */
            }}
            p {{
                margin-bottom: 10px;
            }}
            .font-italic {{
                font-style: italic;
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <h1>{data['Judul'][0]}</h1>
            <div class="logo-container">
                <img src="{data['Logo'][0]}" alt="Logo" class="img-fluid">
            </div>
            <p>{data['Teks'][0]}</p>
            <p class="font-italic">Oleh: {data['Oleh'][0]}</p>
            <p>Numerik: {data['Input Numerik'][0]}</p>
            <p>Input 1: {data['Input 1'][0]}</p>
            <p>Input 2: {data['Input 2'][0]}</p>
            <p>Tahun: {data['Tahun'][0]}</p>
        </div>
    </body>
    </html>
    """

    return template

def builder():
    with open('output.csv', newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        data = {key: [] for key in reader.fieldnames}

        for row in reader:
            for key in reader.fieldnames:
                data[key].append(row[key].strip() if row[key] else '')

    with open('output.html', 'w', encoding='utf-8') as html_file:
        html_file.write(generate_html(data))

if __name__ == "__main__":
    builder()
