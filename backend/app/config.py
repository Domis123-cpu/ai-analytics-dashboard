import os
from dotenv import load_dotenv

load_dotenv()

DB_USER = os.getenv("DB_USER", "sales_user")
DB_PASS = os.getenv("DB_PASS", "sales_password")
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_NAME = os.getenv("DB_NAME", "sales_db")

DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}/{DB_NAME}"
