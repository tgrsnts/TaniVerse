from bs4 import BeautifulSoup
import csv

# Fungsi untuk mengekstrak data dari HTML
def extract_product_data(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    
    # Ekstrak nama produk
    product_name = soup.find('p', class_='text-2xl font-bold').text.strip()
    
    # Ekstrak harga produk
    product_price = soup.find('p', class_='lg:text-3xl font-bold').text.strip()
    
    # Ekstrak deskripsi produk
    # Mengambil elemen <p> kedua setelah nama dan harga
    description = soup.find('div', class_='flex flex-col w-full lg:w-2/3 px-4 mt-4 lg:mt-0 gap-2 rounded-lg transition duration-300 font-poppins')
    if description:
        product_description = description.find_all('p')[4].text.strip()  # Mengambil elemen <p> kedua
    else:
        product_description = 'Deskripsi tidak ditemukan'  # Jika tidak ada container
    
    # Ekstrak spesifikasi produk
    specifications = []
    spec_list = soup.find('ul', class_='list-decimal list-inside')
    if spec_list:
        for li in spec_list.find_all('li'):
            specifications.append(li.text.strip())
    
    return {
        'name': product_name,
        'price': product_price,
        'description': product_description,
        'specifications': specifications
    }

# Fungsi untuk menyimpan data ke file CSV
def save_product_data_to_csv(products, filename):
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['name', 'price', 'description', 'specifications']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()  # Menulis header
        for product in products:
            writer.writerow({
                'name': product['name'],
                'price': product['price'],
                'description': product['description'],
                'specifications': '; '.join(product['specifications'])  # Gabungkan spesifikasi menjadi satu string
            })

# Contoh penggunaan
html_files = ['detail_bayam.html',
'detail_brokoli.html',
'detail_buncis.html',
'detail_cabaikeriting.html',
'detail_cabairawit.html',
'detail_cal-ha.html',
'detail_impresol.html',
'detail_jagung.html',
'detail_kacangpanjang.html',
'detail_kalinet.html',
'detail_kangkung.html',
'detail_kol.html',
'detail_labusiam.html',
'detail_mordenfol.html',
'detail_orinit.html',
'detail_paria.html',
'detail_powersoil.html',
'detail_sawi.html',
'detail_selada.html',
'detail_terong.html',
'detail_timun.html',
'detail_tomat.html',
'detail_vigorin.html',
'detail_vitaron.html',]  # Ganti dengan daftar file HTML
output_csv_file = 'produk.csv'  # Nama file CSV output
products = []

for html_file in html_files:
    with open(html_file, 'r', encoding='utf-8') as f:
        html_content = f.read()
        product_data = extract_product_data(html_content)
        products.append(product_data)  # Tambahkan data produk ke list

# Simpan semua produk ke dalam satu file CSV
save_product_data_to_csv(products, output_csv_file)

print("Data produk telah diekstrak dan disimpan ke dalam file CSV.")
