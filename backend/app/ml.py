import pandas as pd
from sqlalchemy.orm import Session
from sklearn.linear_model import LinearRegression
from datetime import date
from .models import Sale

_model = None

def train_sales_forecast_model(db: Session):
    global _model
    sales = db.query(Sale).all()
    if not sales:
        return None

    data = [{
        "day": s.date.toordinal(),
        "amount": s.amount
    } for s in sales]

    df = pd.DataFrame(data)
    X = df[["day"]]
    y = df["amount"]

    model = LinearRegression()
    model.fit(X, y)
    _model = model
    return model

def predict_sales(db: Session, target_date: date):
    global _model
    if _model is None:
        train_sales_forecast_model(db)
    if _model is None:
        return None

    day = target_date.toordinal()
    pred = _model.predict([[day]])[0]
    return float(pred)

def customer_analysis(db: Session):
    sales = db.query(Sale).all()
    if not sales:
        return {}

    data = [{
        "customer_id": s.customer_id,
        "amount": s.amount
    } for s in sales]

    df = pd.DataFrame(data)
    summary = df.groupby("customer_id")["amount"].sum().reset_index()
    summary = summary.sort_values("amount", ascending=False)
    return summary.to_dict(orient="records")

def ai_recommendations(db: Session):
    customers = customer_analysis(db)
    if not customers:
        return []

    top_customers = customers[:3]
    recs = []
    for c in top_customers:
        recs.append({
            "customer_id": c["customer_id"],
            "recommendation": "Zaproponuj rabat dla klienta o wysokiej wartości sprzedaży."
        })
    return recs
