📊 AI Analytics Dashboard
Interaktywny dashboard analityczny zbudowany w oparciu o FastAPI, PostgreSQL, React, Vite i model ML do prognozowania sprzedaży.

Projekt umożliwia:

zarządzanie klientami

rejestrowanie sprzedaży

analizę danych

generowanie prognoz sprzedaży

wizualizację danych na frontendzie

🚀 Funkcjonalności
🧩 Backend (FastAPI)
CRUD dla klientów

CRUD dla sprzedaży

automatyczne tworzenie tabel w PostgreSQL

endpointy analityczne

endpoint prognozy sprzedaży (ML)

dokumentacja Swagger:
👉 http://127.0.0.1:8000/docs

📊 Frontend (React + Vite)
dashboard sprzedaży

formularze dodawania klientów i sprzedaży

wykresy i statystyki

komunikacja z backendem przez REST API

🗄 Baza danych (PostgreSQL)
tabela customers

tabela sales

relacja 1‑wiele (customer → sales)

🧠 Architektura systemu
Kod
```
┌──────────────────────────┐
│        Frontend          │
│   React + Vite + Axios   │
└──────────────┬───────────┘
               │ REST API
               ▼
┌──────────────────────────┐
│         FastAPI          │
│  /customers /sales /ml   │
└──────────────┬───────────┘
               │ SQLAlchemy ORM
               ▼
┌──────────────────────────┐
│       PostgreSQL         │
│ customers / sales tables │
└──────────────────────────┘
```

📁 Struktura projektu
Kod

```
ai-analytics-dashboard/
│
├── backend/
│   ├── app/
│   │   ├── main.py
│   │   ├── models.py
│   │   ├── schemas.py
│   │   ├── crud.py
│   │   ├── database.py
│   │   └── ml.py
│   ├── .env
│   ├── requirements.txt
│   └── README.md
│
└── frontend/
    ├── src/
    ├── public/
    ├── package.json
    ├── vite.config.js
    └── README.md
```
    
🔧 Instalacja i uruchomienie
1️⃣ Backend
Wejdź do folderu backend:
cd backend
Utwórz i aktywuj środowisko:
python -m venv .venv
.\.venv\Scripts\activate
Zainstaluj zależności:
pip install -r requirements.txt
Skonfiguruj .env:
Kod
DB_USER=sales_user
DB_PASS=sales_password
DB_HOST=localhost
DB_NAME=sales_db
Uruchom backend:
uvicorn app.main:app --reload
Backend działa na:

👉 http://127.0.0.1:8000  
👉 Dokumentacja: http://127.0.0.1:8000/docs

2️⃣ Frontend
Wejdź do folderu frontend:
cd frontend
Zainstaluj zależności:
npm install
Uruchom aplikację:
npm run dev
Frontend działa na:

👉 http://localhost:5173

📡 API Endpoints
👤 Customers
Metoda	Endpoint	Opis
GET	/customers	lista klientów
POST	/customers	dodaj klienta
GET	/customers/{id}	pobierz klienta
DELETE	/customers/{id}	usuń klienta


💰 Sales
Metoda	Endpoint	Opis
GET	/sales	lista sprzedaży
POST	/sales	dodaj sprzedaż
GET	/sales/{id}	pobierz sprzedaż
DELETE	/sales/{id}	usuń sprzedaż


📈 Analytics
Endpoint	Opis
GET /customers/analysis	analiza klientów
GET /sales/forecast	prognoza sprzedaży


🧪 Testy
Projekt zawiera testy jednostkowe i integracyjne:
pytest
🧑‍💻 Autor
Projekt przygotowany przez Małgorzatę  
Repozytorium: https://github.com/Domis123-cpu/ai-analytics-dashboard


















🎉 Dlaczego ten projekt jest wartościowy?
pokazuje praktyczną integrację FastAPI + PostgreSQL + React

zawiera pełny pipeline CRUD + ML

ma czytelną architekturę

jest gotowy do rozbudowy o:

logowanie

dashboardy BI

modele ML

RAG

integracje z chmurą
