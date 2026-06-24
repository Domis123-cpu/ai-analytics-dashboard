from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from datetime import date

from .database import Base, engine, get_db
from . import models, schemas, crud, ml

Base.metadata.create_all(bind=engine)

app = FastAPI(title="AI Analytics Dashboard")

@app.post("/customers", response_model=schemas.Customer)
def create_customer(customer: schemas.CustomerCreate, db: Session = Depends(get_db)):
    return crud.create_customer(db, customer)

@app.get("/customers", response_model=list[schemas.Customer])
def list_customers(db: Session = Depends(get_db)):
    return crud.get_customers(db)

@app.post("/sales", response_model=schemas.Sale)
def create_sale(sale: schemas.SaleCreate, db: Session = Depends(get_db)):
    return crud.create_sale(db, sale)

@app.get("/sales", response_model=list[schemas.Sale])
def list_sales(db: Session = Depends(get_db)):
    return crud.get_sales(db)

@app.get("/forecast")
def forecast(target_date: date, db: Session = Depends(get_db)):
    pred = ml.predict_sales(db, target_date)
    return {"date": target_date, "predicted_amount": pred}

@app.get("/customers/analysis")
def customers_analysis(db: Session = Depends(get_db)):
    return ml.customer_analysis(db)

@app.get("/recommendations")
def recommendations(db: Session = Depends(get_db)):
    return ml.ai_recommendations(db)
