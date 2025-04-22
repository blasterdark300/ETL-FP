import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")  # Contoh: postgresql://username:password@localhost:5432/nama_db
