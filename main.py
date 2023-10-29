import requests
from bs4 import BeautifulSoup
import pandas as pd

# Inisialisasi list untuk menyimpan data
product_names = []
product_images = []
product_details = []
product_stocks = []

# Mengatur headers dan URL (Contoh URL, ganti sesuai kebutuhan)
headers = {
    "User-Agent": "Mozilla/5.0",
}
url = 'https://shopee.co.id/search?keyword=contoh'

# Request ke Shopee
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, 'html.parser')

# Scraping data (contoh selector, ganti sesuai kebutuhan)
for product in soup.select('.product-item'):
    name = product.select_one('.product-name').text if product.select_one('.product-name') else 'N/A'
    image = product.select_one('.product-image img')['src'] if product.select_one('.product-image img') else 'N/A'
    detail = product.select_one('.product-detail').text if product.select_one('.product-detail') else 'N/A'
    stock = product.select_one('.product-stock').text if product.select_one('.product-stock') else 'N/A'
    
    product_names.append(name)
    product_images.append(image)
    product_details.append(detail)
    product_stocks.append(stock)

# Simpan ke Excel
df = pd.DataFrame({
    'Nama Produk': product_names,
    'Gambar Produk': product_images,
    'Detail Keterangan': product_details,
    'Jumlah Stok': product_stocks,
})

df.to_excel('shopee_products.xlsx', index=False)
