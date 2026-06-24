from sqlalchemy import Column, Integer, String, Float, Date, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base

class Customer(Base):
    __tablename__ = "customers"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    segment = Column(String, index=True)
    country = Column(String, index=True)

    sales = relationship("Sale", back_populates="customer")

class Sale(Base):
    __tablename__ = "sales"

    id = Column(Integer, primary_key=True, index=True)
    customer_id = Column(Integer, ForeignKey("customers.id"))
    date = Column(Date, index=True)
    amount = Column(Float)
    product = Column(String, index=True)

    customer = relationship("Customer", back_populates="sales")
