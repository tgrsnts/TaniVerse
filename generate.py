import csv
from jinja2 import Environment, FileSystemLoader

# Load data dari file CSV
data = []
with open('produk.csv', newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        # Pastikan kolom 'specifications' adalah list
        row['specifications'] = row['specifications'].split(';')  # Misalnya, jika spesifikasi dipisahkan dengan ';'
        data.append(row)

# Load template HTML
env = Environment(loader=FileSystemLoader('.'))
template = env.get_template('template.html')

# Iterasi untuk setiap item dalam data dan generate file HTML
for idx, item in enumerate(data, 1):
    # Render template dengan data untuk setiap file
    output = template.render(
        title=item['name'],
        heading=item['name'],
        content=item['description'],
        price=item['price'],
        specifications=item['specifications']
    )
    
    # Simpan hasil ke file HTML, misalnya 'output1.html', 'output2.html', dst.
    filename = f'detail_{item["name"].lower()}_baru.html'
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(output)

    print(f"File {filename} berhasil digenerate!")
