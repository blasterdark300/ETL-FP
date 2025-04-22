# ETL-FP (ETL Final Project)

## 📌 Deskripsi
Proyek ini merupakan implementasi proses ETL (Extract, Transform, Load) yang mengambil data fashion dari website, melakukan pembersihan serta transformasi data, lalu menyimpannya ke dalam format CSV, PostgreSQL, dan Google Sheets.

## 🛠️ Fitur
- Web scraping data fashion menggunakan `BeautifulSoup`
- Transformasi data (cleaning dan formatting)
- Export data ke:
  - CSV
  - PostgreSQL
  - Google Sheets

## 🧰 Teknologi
- Python
- BeautifulSoup
- Pandas
- PostgreSQL
- Google Sheets API
- psycopg2
- gspread

## 📦 Instalasi

1. **Clone repository:**
   ```bash
   git clone https://github.com/blasterdark300/ETL-FP.git
   cd ETL-FP
2. Install dependencies:

bash
Copy
Edit

3. Setup environment:

Siapkan file google-sheets-api.json untuk autentikasi Google Sheets API
(jika belum punya silahkan bikin di Kunjungi: https://console.cloud.google.com)

Buat database PostgreSQL dengan nama etlfp_db dan pastikan username/password sudah benar di script


 Struktur Folder
ETL-FP/
├── etl.py
├── requirements.txt
├── google-sheets-api.json
├── output/
│   └── hasil.csv
└── README.md

✍️ Kontributor
blasterdark300
