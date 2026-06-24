from datetime import date
from pydantic import BaseModel

class CustomerBase(BaseModel):
    name: str
    segment: str
    country: str

class CustomerCreate(CustomerBase):
    pass

class Customer(CustomerBase):
    id: int
    class Config:
        orm_mode = True

class SaleBase(BaseModel):
    customer_id: int
    date: date
    amount: float
    product: str

class SaleCreate(SaleBase):
    pass

class Sale(SaleBase):
    id: int
    class Config:
        orm_mode = True
