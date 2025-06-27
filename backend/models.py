from sqlalchemy import Column, Integer, String, Float
from database import Base

class Product(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    price = Column(Float)
    sale_price = Column(Float)
    rating = Column(Float)
    feedbacks = Column(Integer)
